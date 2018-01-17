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

from MathJaxProcessor import *

from sympy import latex
from sympy import integrate
from sympy.abc import x

from Step import Step
from Step import PLACEHOLDER_CONST

RULE_NAME = "power rule"
RULE_FORMULA = "\\int x^{0} \\, dx = \\frac{{ x^{{ {0}+ 1 }} }}{{ {0}+1 }}"
RULE_FORMULA_FULL = "\\int x^{{ {0} }} \\, dx = \\frac{{ x^{{ {0}+ 1 }} }}{{ {0}+1 }} = {1}"
RULE_RESTRICTION = "{0} \\neq -1"

class PowerStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.ruleFormulaFull = RULE_FORMULA_FULL
		self.exponent = latex(self.step.exp)
		self.ruleRestriction = RULE_RESTRICTION

	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that: {} as long as {}. ".format(self.ruleName, displayMath(self.ruleFormula.format(PLACEHOLDER_CONST)), inlineMath(self.ruleRestriction.format(PLACEHOLDER_CONST)))

		exponentSub = "{} = {}".format(PLACEHOLDER_CONST, self.exponent)
		sub = "Here, {}. ".format(inlineMath(exponentSub))

		solution = "So: {}".format(displayMath(self.ruleFormulaFull.format(self.exponent, latex(integrate(self.step.context, x)))))
		return "{}{}{}".format(rule, sub, solution)
