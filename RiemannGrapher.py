'''Graphs function with a Riemman sum.'''
import io

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
		plot_sum: bool = False):
	'''graphs a function, along with a Riemann sum.'''

	diff = upper - lower
	if diff < 0:
		raise ValueError('Upper bound must be greater than lower bound.')

	width = diff / n

	if handed.lower() == 'left':
		offset = 0
	elif handed.lower() in ('center', 'centre'):
		offset = width / 2
	elif handed.lower() == 'right':
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
	if plot_sum:
		plt.plot(sum_x, sum_y, 'red')
	plt.xlim(lower, upper)
	buffer = io.BytesIO()
	plt.savefig(io, type='image/png')
	buffer.seek(0)

	return buffer
