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

RULE_NAME = "rewrite rule"
RULE_FORMULA = "equivalent functions will have equivalent integrals. This means that we can expand or factor functions before integrating them"

class RewriteStep(Step):

	# Initialize the step.
	def __init__(self, step):
		super().__init__(step, RULE_NAME, RULE_FORMULA)
		self.original = latex(Integral(self.step.context, self.step.symbol))
		self.rewritten = latex(Integral(self.step.rewritten, self.step.symbol))
	
	# Get the text for applying the rule.
	def getText(self) -> str:
		rule = "The {} says that {}.".format(self.ruleName, self.ruleFormula)
		solution = "We will write $${}$$ as $${}$$ and then integrate this.".format(self.original, self.rewritten)

		return "{}\n{}".format(rule, solution)
