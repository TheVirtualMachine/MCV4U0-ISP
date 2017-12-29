# Check if the given string can be converted to a boolean.
def isBool(string):
	return string.lower() in ("true", "false")

# Check if the given string can be converted to a float.
def isFloat(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

# Check if the given string can be converted to an integer.
def isInt(string):
	try:
		int(string)
		return True
	except ValueError:
		return False
