# MCV4U0 ISP is a program to teach integration using CAS systems and tables.
# Copyright (C) 2018 Vincent Macri and Oliver Daniel
#
# This file is part of MCV4U0 ISP.
#
# MCV4U0 ISP is free software: you can redistribute it and/or modify # it under the terms of the GNU General Public License as published by
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

from MathJaxProcessor import *

from sympy import latex

from Step import Step
from Step import PLACEHOLDER_CONST
from Step import PLACEHOLDER_FCN
from Step import PLACEHOLDER_VAR

RULE_NAME = "constant times rule"
RULE_FORMULA = "\\int {0}{1} \\, d{2} = {0} \\int {1} \\, d{2}"

class ConstantTimesStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.constant = latex(self.step.constant)
		self.other = latex(self.step.other)
		self.symbol = latex(self.step.symbol)
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that: {}".format(self.ruleName, displayMath(self.ruleFormula.format(PLACEHOLDER_CONST, PLACEHOLDER_FCN, PLACEHOLDER_VAR)))
		sub1 = inlineMath("{} = {}".format(PLACEHOLDER_CONST, self.constant))
		sub2 = inlineMath("{} = {}".format(PLACEHOLDER_FCN, self.other))
		sub = "Here, {} and {}. ".format(sub1, sub2)
		solution = "So: {}".format(displayMath(self.ruleFormula.format(self.constant, self.other, self.symbol)))
		return "{}{}{}".format(rule, sub, solution)
