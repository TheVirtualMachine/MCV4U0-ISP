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

from Debug import logMessage

from sympy.integrals.manualintegrate import *

from ConstantStep import ConstantStep
from AddStep import AddStep
from PowerStep import PowerStep
from ConstantTimesStep import ConstantTimesStep
from DontKnowStep import DontKnowStep
from TrigStep import TrigStep
from ExpStep import ExpStep
from ReciprocalStep import ReciprocalStep
from UStep import UStep
from RewriteStep import RewriteStep
from PartsStep import PartsStep

# Return a list of steps.
def getStepTree(step):
	stepDict = {}
	stepDict["substeps"] = []
	if (type(step) is AddRule):
		logMessage("Appending add rule.")
		stepObj = AddStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		for substep in step.substeps:
			stepDict["substeps"].append(getStepTree(substep))
	elif (type(step) is ConstantRule):
		logMessage("Appending constant rule.")
		stepObj = ConstantStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
	elif (type(step) is PowerRule):
		logMessage("Appending power rule.")
		stepObj = PowerStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
	elif (type(step) is ConstantTimesRule):
		logMessage("Appending constant times rule.")
		stepObj = ConstantTimesStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		stepDict["substeps"].append(getStepTree(step.substep))
	elif (type(step) is TrigRule):
		logMessage("Appending trig rule.")
		stepObj = TrigStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
	elif (type(step) is ExpRule):
		logMessage("Appending exp rule.")
		stepObj = ExpStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
	elif (type(step) is ReciprocalRule):
		logMessage("Appending reciprocal rule.")
		stepObj = ReciprocalStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
	elif (type(step) is URule):
		logMessage("Appending u rule.")
		stepObj = UStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		stepDict["substeps"].append(getStepTree(step.substep))
	elif (type(step) is RewriteRule):
		logMessage("Appending rewrite rule.")
		stepObj = RewriteStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		stepDict["substeps"].append(getStepTree(step.substep))
	elif (type(step) is PartsRule):
		logMessage("Appending parts rule.")
		stepObj = PartsStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		stepDict["substeps"].append(getStepTree(step.v_step))
		stepDict["substeps"].append(getStepTree(step.second_step))
	else:
		logMessage("Appending don't know rule.")
		stepObj = DontKnowStep(step)
		stepDict["name"] = stepObj.getName()
		stepDict["text"] = stepObj.getText()
		if (type(step) is not DontKnowRule):
			logMessage("USING DON'T KNOW RULE WHEN ACTUAL RULE IS {}!".format(type(step)))
	return stepDict
