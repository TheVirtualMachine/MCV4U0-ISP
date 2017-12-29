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
from sympy import *
from sympy.abc import *
from sympy.integrals.manualintegrate import integral_steps

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

	sympyFunction = process_sympy(f)

	indefiniteIntegral = integrate(sympyFunction, x)

	steps = integral_steps(sympyFunction, x)
	print(steps)
	print(repr(steps))

	definiteIntegral = integrate(sympyFunction, (x, lower, upper))
	lambdaFunction = lambdify(x, sympyFunction)
	graphImage = graph(lambdaFunction, n=n, handed=handed, lower=lower, upper=upper, plotSum=plotSum)

	results = {}
	results["integral"] = latex(indefiniteIntegral)
	results["sum"] = latex(definiteIntegral)
	results["graph"] = graphImage

	return json.JSONEncoder().encode(results)
	
app.run(debug=True)
