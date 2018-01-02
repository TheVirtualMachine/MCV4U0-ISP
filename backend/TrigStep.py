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
from sympy import integrate
from sympy import sin
from sympy import cos
from sympy import csc
from sympy import sec

from Step import Step
from Step import PLACEHOLDER_CONST

RULE_NAME = "trig rule"
RULE_FORMULA = "\\int {0} \\, dx = {1}"


class TrigStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.function = latex(self.step.func)
		self.formula = self.step.context
		self.argument = self.step.arg
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		return "The {} tells us that {}.".format(RULE_NAME, RULE_FORMULA.format(self.function, latex(integrate(self.formula, self.argument))))
