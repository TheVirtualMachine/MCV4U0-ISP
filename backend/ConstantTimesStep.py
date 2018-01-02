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
from Step import PLACEHOLDER_FCN

RULE_NAME = "constant times rule"
RULE_FORMULA = "\\int {0}{1} \\, dx = {0} \\int {1} \\, dx"


class ConstantTimesStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.constant = latex(self.step.constant)
		self.other = latex(self.step.other)
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that {}.".format(self.ruleName, self.ruleFormula.format(PLACEHOLDER_VAR, PLACEHOLDER_FCN))
		sub = "Here, {} = {} and {} = {}".format(PLACEHOLDER_VAR, self.constant, PLACEHOLDER_FCN, self.other)
		solution = "So, {}".format(self.ruleFormula.format(self.constant, self.other))
		return "{}\n{}\n{}".format(rule, sub, solution)
