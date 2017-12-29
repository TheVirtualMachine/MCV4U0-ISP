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
	y = f(x)

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
				color=pos_color if val > 0 else neg_color
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

	return image.getvalue()
