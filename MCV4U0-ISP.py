import json
from flask import Flask, request, abort
from sympy import *

from latex2sympy.process_latex import process_sympy

from RiemannGrapher import graph
from ErrorChecking import isBool, isFloat, isInt

app = Flask(__name__) # Create application instance.

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseInput(f, n, handed, lower, upper, plotSum):
		#

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
				plot_sum = bool(plotSum)
			else:
				plot_sum = None

		return (f, n, handed, lower, upper, plotSum)

@app.route("/")
def index():
	f = request.args.get("f")
	n = request.args.get("n")
	handed = request.args.get("handed")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	plotSum = request.args.get("sum")

	print(f, n, handed, lower, upper, plotSum)

	parsed = parseInput(f, n, handed, lower, upper, plotSum)

	if (None in parsed): # If there was an error parsing the input
		abort(400)

	sympyFunction = process_sympy(f)
	print(sympyFunction)

	results = {}
	results.setdefault("integral", "x")
	results.setdefault("sum", 0)
	results.setdefault("graph", "")

	return json.JSONEncoder().encode(results)
	
app.run(debug=True)
