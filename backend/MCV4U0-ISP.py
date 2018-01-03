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

from Debug import logMessage
from Debug import DEBUG_MODE

import json
from flask import Flask, request, abort

import sympy as sp
from sympy.abc import *
from sympy.integrals.manualintegrate import integral_steps

from latex2sympy.process_latex import process_sympy

from RiemannGrapher import graph

from StepProcessor import getStepTree

app = Flask(__name__)  # Create application instance.

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseInput(f, n, handed, lower, upper, plotSum):
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
	return (f, n, handed, lower, upper, plotSum)

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

	# Lambda is a reserved word in Python, so SymPy uses the alternate
	# spelling of "lamda".
	variables.remove("lambda")
	variables.append("lamda")

	# Remove other special cases from the list.
	variables.remove("e")
	variables.remove("E")
	variables.remove("x")
	variables.remove("pi")

	# Replace variables in function with 1.
	removedVariables = []
	for var in variables:
		if (sp.Symbol(var) in function.free_symbols):
			function = function.subs(var, 1)
			removedVariables.append(var)

	# Return function and list of removed variables as a tuple.
	return (function, removedVariables)

@app.route("/api")
def index():
	logMessage("")
	logMessage("")
	logMessage("")
	# Read the input.
	f = request.args.get("f")
	n = request.args.get("n")
	handed = request.args.get("handed")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	plotSum = request.args.get("sum")

	# Parse and error check the input.
	parsed = parseInput(f, n, handed, lower, upper, plotSum)

	if (None in parsed): # If there was an error parsing the input
		abort(400)

	# Unpack the parsed tuple.
	f, n, handed, lower, upper, plotSum = parsed

	# Create the functions.
	try:
		sympyFunction = convertInput(f)
		stupidFunction, removedVariables = stupidifyFunction(sympyFunction)
	except Exception:
		abort(400)

	# Calculate the integrals.
	indefiniteIntegral = sp.integrate(sympyFunction, x, manual=True)
	definiteIntegral = sp.integrate(sympyFunction, (x, lower, upper), manual=True)

	# Graph the image.
	lambdaFunction = sp.lambdify(x, stupidFunction)
	try:
		graphImage = graph(lambdaFunction, n=n, handed=handed, lower=float(lower), upper=float(upper), plotSum=plotSum)
	except Exception:
		# Send back "501 error" instead of actually having an error to aid in debugging.
		# I will change this to abort(501) later.
		graphImage = "501 error"
		#abort(501)

	# Format the results into a dictionary which later is converted to JSON.
	results = {}
	results["function"] = "$${}$$".format(sp.latex(sympyFunction))
	results["integral"] = "$${}$$".format(sp.latex(indefiniteIntegral))
	results["sum"] = "$${}$$".format(sp.latex(definiteIntegral))
	results["graph"] = graphImage
	results["note"] = ""
	if (len(removedVariables) > 0):
		results["note"] = "The following variables had their values replaced with 1 in order to graph the function: " + str(removedVariables)

	logMessage("==========")
	#logMessage(len(integral_steps(sympyFunction, x).alternatives[1]))
	logMessage("==========")

	results["steps"] = getStepTree(integral_steps(sympyFunction, x))

	return json.JSONEncoder().encode(results) # Return the results.
	
app.run(debug=DEBUG_MODE)
