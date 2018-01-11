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

'''Graphs function with a Riemman sum.'''
from io import StringIO

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def graph(
		f: np.ufunc,
		n: int = 20,
		handed: str = 'left',
		lower: float = 0,
		upper: float = 20,
		pos_color: str = 'blue',
		neg_color: str = 'red',
		plotSum: bool = False):
	'''graphs a function, along with a Riemann sum.'''

	diff = upper - lower
	if diff < 0:
		raise ValueError('Upper bound must be greater than lower bound.')

	width = diff / n

	if handed == 'left':
		offset = 0
	elif handed in ('center', 'centre'):
		offset = width / 2
	elif handed == 'right':
		offset = width
	else:
		raise ValueError('Invalid sum handedness.')

	x = np.linspace(lower, upper, n * 20)
	y = np.fromiter(map(f, x), x.dtype)

	riemann_sum = 0
	sum_x = []
	sum_y = []

	fig, ax = plt.subplots(1)
	for i in np.linspace(lower, upper, num=n):
		val = f(i + offset)
		ax.add_patch(
			patches.Rectangle(
					(i, 0.0),
				width,
				val,
				alpha=0.5,
				color=pos_color if val >= 0 else neg_color
			)
		)
		riemann_sum += width * val
		sum_x.append(i)
		sum_y.append(riemann_sum)

	plt.plot(x, y)
	if plotSum:
		plt.plot(sum_x, sum_y, 'red')
	plt.xlim(lower, upper)

	image = StringIO()
	plt.savefig(image, format='svg')
	image.seek(0)
	svgText = image.getvalue()

	plt.close()

	sumText = "\\({}\\)".format(riemann_sum)

	return (svgText, sumText)
