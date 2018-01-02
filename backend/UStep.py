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

from Step import Step
from Step import PLACEHOLDER_DUMMY

RULE_NAME = "u rule"
RULE_FORMULA = "we can substitute in dummy variables to help us find the integral"

class UStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		print("----------")
		print("APPLYING U RULE")
		self.uVar = latex(step.u_var)
		self.uFunc = latex(step.u_func)
		self.constant = latex(step.constant)
		self.symbol = latex(step.symbol)
		self.sympySymbol = step.symbol
		self.inverseConstant = step.constant ** -1
		print("uVar: {}".format(self.uVar))
		print("uFunc: {}".format(self.uFunc))
		print("constant: {}".format(self.constant))
		print("symbol: {}".format(self.symbol))
		print("sympySymbol: {}".format(self.sympySymbol))
		print("inverseConstant: {}".format(self.inverseConstant))
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that {}.".format(self.ruleName, self.ruleFormula)
		
		uSub = "Let d{} = {}.".format(PLACEHOLDER_DUMMY, self.uFunc)
		#solution = "So, {}.".format(self.ruleFormula.format(self.symbol))
		#sub = "Here, {} = {}.".format(PLACEHOLDER_VAR, self.symbol)

		print("----------")
		return rule
		return "{}\n{}\n{}".format(rule, sub, solution)
