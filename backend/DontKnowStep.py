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
from sympy import integrate
from sympy import Integral
from sympy.integrals.risch import NonElementaryIntegral as NonElementaryIntegral
from sympy.abc import x

from Step import Step
from Step import PLACEHOLDER_CONST

RULE_NAME = "don't know rule"
RULE_FORMULA = "\\int {0} \\, dx = \\int {0} \\, dx"
RULE_DEFINED_FORMULA = "\\int {0} \\, dx = {1}"

class DontKnowStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.function = latex(self.step.context)
		self.sympyFunction = self.step.context
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		integral = integrate(self.sympyFunction, x)
		integralType = type(integral)
		rule = "I don't know how to show you the steps to integrate {}. ".format(inlineMath(self.function))
		step = ""
		solution = ""
		if (integralType is Integral or integralType is NonElementaryIntegral):
			step = "Since I can't do this, we will just define the integral in terms of itself. "
			solution = "So: {}".format(displayMath(latex(integral)))
		else:
			step = "I do know this integral, I just can't explain it. "
			solution = "Here it is: {}".format(displayMath(RULE_DEFINED_FORMULA.format(self.function, latex(integral))))
		return "{}{}{}".format(rule, step, solution)
