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

from sympy import latex

from Step import Step
from Step import PLACEHOLDER_VAR

RULE_NAME = "constant rule"
RULE_FORMULA = "\\int {0} \\, dx = {0}x"


class ConstantStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.constant = latex(self.step.constant)
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		return "The {} says that {}.\nHere, {} = {}.\nSo, {}.".format(self.ruleName, self.ruleFormula.format(PLACEHOLDER_VAR), PLACEHOLDER_VAR, self.constant, self.ruleFormula.format(self.constant))
