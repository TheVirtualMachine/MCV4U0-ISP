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

import json
from flask import Flask, request, abort
import sympy as sp
from sympy.abc import *
from sympy.integrals.manualintegrate import integral_steps
import numpy

import math

from latex2sympy.process_latex import process_sympy

from RiemannGrapher import graph
from ErrorChecking import isBool, isFloat, isInt

app = Flask(__name__) # Create application instance.

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseInput(f, n, handed, lower, upper, plotSum):
		if (n is not None):
			if (isInt(n)):
				n = int(n)
			else:
				n = None

		validHandedValues = ["left", "center", "centre", "right"]
		if (handed is not None):
			handed = handed.lower()
			if (handed not in validHandedValues):
				handed = None

		if (lower is not None and upper is not None):
			if (isFloat(lower) and isFloat(upper)):
				lower = float(lower)
				upper = float(upper)

				if (lower > upper):
					lower = None
					upper = None
			else:
				lower = None
				upper = None
		
		if (plotSum is not None):
			if (isBool(plotSum)):
				plotSum = plotSum.lower() == "true"
			else:
				plotSum = None

		return (f, n, handed, lower, upper, plotSum)

# Convert the input function to a sympy function.
def convertInput(function):
	sympyedFunction = process_sympy(function).subs(e, E).subs("lambda", lamda)
	return sp.sympify(str(sympyedFunction))

# Stupidify the function by replacing constants and variables with actual values.
def stupidifyFunction(function):
	function = function.subs(pi, math.pi).subs(E, math.e)

	variables = list(string.ascii_letters) + list(greeks)

	# Lambda is a reserved word in Python, so SymPy uses the alternate spelling of "lamda".
	variables.remove("lambda")
	variables.append("lamda")

	# Remove other special cases from the list.
	variables.remove("e")
	variables.remove("E")
	variables.remove("x")
	variables.remove("pi")

	removedVariables = []
	for var in variables:
		if (sp.Symbol(var) in function.free_symbols):
			function = function.subs(var, 1)
			removedVariables.append(var)

	return (function, removedVariables)

@app.route("/")
def index():
	f = request.args.get("f")
	n = request.args.get("n")
	handed = request.args.get("handed")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	plotSum = request.args.get("sum")

	parsed = parseInput(f, n, handed, lower, upper, plotSum)

	if (None in parsed): # If there was an error parsing the input
		abort(400)

	f, n, handed, lower, upper, plotSum = parsed

	sympyFunction = convertInput(f)
	stupidFunction, removedVariables = stupidifyFunction(sympyFunction)

	# Calculate the integral.
	indefiniteIntegral = sp.integrate(sympyFunction, x)
	definiteIntegral = sp.integrate(sympyFunction, (x, lower, upper))

	# Graph the image.
	lambdaFunction = sp.lambdify(x, stupidFunction)
	graphImage = ""
	try:
		graphImage = graph(lambdaFunction, n=n, handed=handed, lower=lower, upper=upper, plotSum=plotSum)
	except:
		abort(400)

	steps = integral_steps(sympyFunction, x)

	# Format the results into a dictionary which later is converted to JSON.
	results = {}
	results["integral"] = sp.latex(indefiniteIntegral)
	results["sum"] = sp.latex(definiteIntegral)
	results["graph"] = graphImage
	results["note"] = ""
	if (len(removedVariables) > 0):
		results["note"] = "The following variables had their values replaced with 1 in order to graph the function: " + str(removedVariables)

	return json.JSONEncoder().encode(results)
	
app.run(debug=True)
