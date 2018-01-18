# MCV4U0 ISP is a program to teach integration using CAS systems and tables.
# Copyright (C) 2018 Vincent Macri and Oliver Daniel
#
# This file is part of MCV4U0 ISP.
#
# MCV4U0 ISP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MCV4U0 ISP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MCV4U0 ISP. If not, see <http://www.gnu.org/licenses/>.

import time
import json

from Debug import logMessage
from Debug import DEBUG_MODE

from MathJaxProcessor import inlineMath

from flask import Flask, request, abort
from flask_caching import Cache
from flask_cors import CORS

import sympy as sp
from sympy.abc import *
from sympy.integrals.manualintegrate import integral_steps

from latex2sympy.process_latex import process_sympy

from RiemannGrapher import graph

from StepProcessor import getStepTree

app = Flask(__name__) # Create application instance.
CORS(app, resources=r'\/(integrate|graph)\/*')
cache = Cache(app, config={"CACHE_TYPE": "simple"})

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseGraphInput(f, n, handed, lower, upper, plotSum, posCol, negCol):
	try:
		process_sympy(f)
	except Exception:
		f = None

	# Check and set the number of samples.
	try:
		n = int(n)
	except ValueError:
		n = None

	# Check and set the method of evaluating the Riemann sum.
	validHandedValues = ["left", "center", "centre", "right"]
	if (handed is not None):
		handed = handed.lower()
		if (handed not in validHandedValues):
			handed = None

	# Check and set the evaluation bounds of the sum.
	try:
		lower = sp.Rational(lower)
		upper = sp.Rational(upper)
	except TypeError:
		lower = None
		upper = None

	# Check and set the input for evaluating the running sum.
	if (plotSum is not None):
		if (plotSum.lower() in ("true", "false")):
			plotSum = plotSum.lower() == "true"
		else:
			plotSum = None

	# Return the input as a tuple.
	return (f, n, handed, lower, upper, plotSum, posCol, negCol)

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseIntegrateInput(f, lower, upper):
	try:
		process_sympy(f)
	except Exception:
		f = None

	# Check and set the evaluation bounds of the sum.
	try:
		lower = sp.Rational(lower)
		upper = sp.Rational(upper)
	except TypeError:
		lower = None
		upper = None

	# Return the input as a tuple.
	return (f, lower, upper)

# Convert the input function to a sympy function.
def convertInput(function):
	sympyedFunction = process_sympy(function).subs(e, E).subs("lambda", lamda)
	return sp.sympify(str(sympyedFunction))

# Stupidify the function by replacing constants and variables with actual
# values.
def stupidifyFunction(function):
	function = function.evalf()

	# List of possible variables.
	variables = list(string.ascii_letters) + list(greeks)

	# Lambda is a reserved word in Python, so SymPy uses the alternate spelling of "lamda".
	variables.remove("lambda")
	variables.append("lamda")

	# Remove other special cases from the list.
	variables.remove("e")
	variables.remove("E")
	variables.remove("x")
	variables.remove("pi")

	# Replace variables in function with 1.
	removedVariables = []
	for sym in function.free_symbols:
		if (str(sym) in variables):
			removedVariables.append(sp.latex(sym))
			function = function.subs(sym, 1)

	# Return function and list of removed variables as a tuple.
	return (function, removedVariables)

@cache.memoize(60)
def doGraphing(f, n, handed, lower, upper, plotSum, posCol, negCol):
	logMessage("Graphing")

	# Parse and error check the input.
	parsed = parseGraphInput(f, n, handed, lower, upper, plotSum, posCol, negCol)

	print(parsed)
	if (None in parsed): # If there was an error parsing the input
		print("400 error")
		abort(400)

	# Unpack the parsed tuple.
	f, n, handed, lower, upper, plotSum, posCol, negCol = parsed

	try:
		sympyFunction = convertInput(f)
		stupidFunction, removedVariables = stupidifyFunction(sympyFunction)
	except Exception:
		print("501 error")
		abort(501)

	results = {}
	results["note"] = ""
	if (len(removedVariables) > 0):
		removedText = ""
		for var in removedVariables[:-1]:
			removedText += "{},".format(var)
		removedText += "{} = 1".format(removedVariables[-1])
		results["note"] = "Assume that: {}.".format(inlineMath(removedText))

	# Graph the image.
	lambdaFunction = sp.lambdify(x, stupidFunction)
	try:
		results["graph"], results["sum"] = graph(lambdaFunction, n=n, handed=handed, lower=float(lower), upper=float(upper), plotSum=plotSum, pos_color=posCol, neg_color=negCol)
	except Exception:
		print("501 error")
		abort(501)
	return json.JSONEncoder().encode(results) # Return the results.

@app.route("/graph")
def graphRequest():
	startTime = time.time()

	# Read the input.
	f = request.args.get("f")
	n = request.args.get("n")
	handed = request.args.get("handed")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	plotSum = request.args.get("sum")
	posCol = request.args.get("pos")
	negCol = request.args.get("neg")

	result = doGraphing(f, n, handed, lower, upper, plotSum, posCol, negCol)
	endTime = time.time()
	logMessage("Graph time: {}".format(endTime - startTime))
	return result

@cache.memoize(60)
def doIntegration(f, lower, upper):
	logMessage("Integrating")

	# Parse and error check the input.
	parsed = parseIntegrateInput(f, lower, upper)

	if (None in parsed): # If there was an error parsing the input
		print("400 error")
		abort(400)

	# Unpack the parsed tuple.
	f, lower, upper = parsed

	# Create the functions.
	try:
		sympyFunction = convertInput(f)
		stupidFunction, removedVariables = stupidifyFunction(sympyFunction)
	except Exception:
		print("501 error")
		abort(501)

	# Calculate the integrals.
	indefiniteIntegral = sp.integrate(sympyFunction, x)
	definiteIntegral = sp.integrate(sympyFunction, (x, lower, upper))

	# Format the results into a dictionary which later is converted to JSON.
	results = {}
	results["function"] = sp.latex(sympyFunction)
	results["integral"] = sp.latex(indefiniteIntegral)
	results["definiteIntegral"] = sp.latex(definiteIntegral)
	results["approxDefiniteIntegral"] = sp.latex(definiteIntegral.evalf())
	results["steps"] = getStepTree(integral_steps(sympyFunction, x))

	return json.JSONEncoder().encode(results) # Return the results.

@app.route("/integrate")
def integrateRequest():
	startTime = time.time()

	# Read the input.
	f = request.args.get("f")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	
	result = doIntegration(f, lower, upper)
	endTime = time.time()
	logMessage("Integration time: {}".format(endTime - startTime))
	return result

if __name__ == '__main__':
	app.run(debug=DEBUG_MODE)
