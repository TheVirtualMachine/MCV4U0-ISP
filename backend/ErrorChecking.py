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
