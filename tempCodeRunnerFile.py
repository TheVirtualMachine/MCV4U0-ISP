from RiemannGrapher import graph
import numpy as np

def f(x): return x / np.sqrt(1+x*x)
graph(f, lower=-5, upper=5, n=200, handed='left', plot_sum=True)

