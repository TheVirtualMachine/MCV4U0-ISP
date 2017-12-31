from RiemannGrapher import graph
from numpy import *

def f(x): return e * x
graph(f, lower=-5, upper=5, n=200, handed='left', plotSum=True)
