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
from Step import PLACEHOLDER_CONST

RULE_NAME = "add rule"
RULE_FORMULA = "$$\\int f(x) + g(x) \\, dx = \\int f(x) dx + \\int g(x) dx$$"

class AddStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.formula = latex(self.step.context)
		self.substeps = self.step.substeps
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		applyRule = "$$\\int {} dx =".format(self.formula)

		first = True
		for substep in self.substeps:
			print("Substep is: " + str(substep))
			if first:
				applyRule += "\\int {} dx".format(latex(substep.context))
				first = False
			else:
				applyRule += " + \\int {} dx".format(latex(substep.context))
		applyRyle += "$$"
		
		return "The {} says that {}.\nThis means that we can integrate each term individually.\nSo, {}".format(self.ruleName, self.ruleFormula, applyRule)
