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
from sympy import diff
from sympy import Integral

from Step import Step
from Step import PLACEHOLDER_DUMMY
from Step import DUMMY_SYMBOL

PARTS_VAR_1 = "u"
PARTS_VAR_2 = "v"

PARTS_FORMULA_1 = "" + PARTS_VAR_1 + " = {}"
PARTS_FORMULA_2 = "d" + PARTS_VAR_2 + " = {}"

RULE_NAME = "parts rule"
RULE_FORMULA = "\\int {0}d{1} = {0}{1} - \\int {1}d{0}"

class PartsStep(Step):

	# x * e**x
	# u=x
	# dv=exp(x)
	# v_step=ExpRule(base=E, exp=x, context=exp(x), symbol=x)
	# second_step=ExpRule(base=E, exp=x, context=exp(x), symbol=x)
	# context=x*exp(x)
	# symbol=x

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.u = latex(self.step.u)
		self.dv = latex(self.step.dv)
		self.vStep = latex(self.step.v_step.context)
		self.secondStep = latex(self.step.second_step.context)
		self.context = latex(self.step.context)
		self.symbol = latex(self.step.symbol)
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that $${}$$.".format(self.ruleName, self.ruleFormula.format(PARTS_VAR_1, PARTS_VAR_2))
		letStatement = "Let $${}$$ and let $${}$$.".format(PARTS_FORMULA_1.format(self.u), PARTS_FORMULA_2.format(self.dv))

		duExpression = "d{} = {}".format(PARTS_VAR_1, latex(diff(self.step.u, self.step.symbol)))
		duStatement = "Differentiate $${}$$ to find that $${}$$.".format(PARTS_VAR_1, duExpression)

		dvIntegral = Integral(self.step.dv, self.step.symbol)

		dvExpression = "{0} = \\int d{0} = {1}".format(PARTS_VAR_2, latex(dvIntegral))
		dvStatement = "Next, we find $${}$$ as so: $${}$$".format(PARTS_VAR_2, dvExpression)
		

		return "{}\n{}\n{}\n{}".format(rule, letStatement, duStatement, dvStatement)
