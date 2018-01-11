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

from sympy import Symbol

PLACEHOLDER_CONST = "a"
PLACEHOLDER_VAR = "x"
PLACEHOLDER_FCN = "f\\left( {} \\right)".format(PLACEHOLDER_VAR)
PLACEHOLDER_DUMMY = "u"
DUMMY_SYMBOL = Symbol(PLACEHOLDER_DUMMY)

class Step:

	# Initialize the step.
	def __init__(self, step, ruleName : str, ruleFormula : str):
		self.step = step
		self.ruleName = ruleName
		self.ruleFormula = ruleFormula
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		return ("The {} says that {}.".format(self.ruleName, self.ruleFormula.format(PLACEHOLDER_VAR)))
	
	# Get the data to be returned in JSON.
	def getData(self) -> tuple:
		return (self.ruleName, self.getText())
