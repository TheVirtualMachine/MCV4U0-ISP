import os
from flask import Flask, request, abort
from RiemannGrapher import graph
from ErrorChecking import isBool, isFloat, isInt

app = Flask(__name__) # Create application instance.

# Parse input and do server-side checking.
# Return parsed parameters as a tuple, converted to the correct types.
# Parameters will be returned as "None" if they are invalid.
def parseInput(f, n, handed, lower, upper, plot_sum):
		# TODO: Parse function.

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
		
		if (plot_sum is not None):
			if (isBool(plot_sum)):
				plot_sum = bool(plot_sum)
			else:
				plot_sum = None

		return (f, n, handed, lower, upper, plot_sum)

@app.route("/")
def index():
	f = request.args.get("f")
	n = request.args.get("n")
	handed = request.args.get("handed")
	lower = request.args.get("lower")
	upper = request.args.get("upper")
	plot_sum = request.args.get("plot_sum")

	print(f, n, handed, lower, upper, plot_sum)

	parsed = parseInput(f, n, handed, lower, upper, plot_sum)

	if (None in parsed): # If there was an error parsing the input
		abort(400)
		


app.run(debug=True)
