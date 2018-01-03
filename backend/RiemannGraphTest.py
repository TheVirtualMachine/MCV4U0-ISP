from RiemannGrapher import graph
import numpy as np

def f(x): return 3  # e * x

g = graph(f, lower=-5, upper=5, n=200, handed='left', plotSum=True)

open('test.svg','w').write(g)
