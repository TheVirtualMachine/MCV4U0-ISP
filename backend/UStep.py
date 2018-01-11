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

from sympy import latex
from sympy import Integral

from Step import Step
from Step import PLACEHOLDER_DUMMY
from Step import DUMMY_SYMBOL

RULE_NAME = "u rule"
RULE_FORMULA = "we can substitute in dummy variables to help us find the integral"
SUB_FORMULA_1 = "d{0} = {1}d{2}"
SUB_FORMULA_2 = "d{2} = {1}d{0}"

class UStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.uVar = latex(self.step.u_var)
		self.uFunc = latex(self.step.u_func)
		self.constant = latex(self.step.constant)
		self.symbol = latex(self.step.symbol)
		self.inverseConstant = latex(self.step.constant ** -1)
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that {}.".format(self.ruleName, self.ruleFormula)
		
		uSub = "Let $${}$$.".format(SUB_FORMULA_1.format(PLACEHOLDER_DUMMY, self.inverseConstant, self.symbol))
		dxSub = "Then, $${}$$.".format(SUB_FORMULA_2.format(PLACEHOLDER_DUMMY, self.constant, self.symbol))

		integralFormula = latex(Integral(self.step.context))
		substitutedFormula = latex(Integral(self.step.context.subs(self.step.u_func, PLACEHOLDER_DUMMY), DUMMY_SYMBOL))

		solution = "So, $${} = {}$$.".format(integralFormula, substitutedFormula)

		return "{}\n{}\n{}\n{}".format(rule, uSub, dxSub, solution)
