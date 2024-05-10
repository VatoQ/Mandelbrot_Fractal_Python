from numba import jit

"""
Interesting Julia params:
0.25005+0j
-0.4+0.59j
"""

MANDELBROT_ITERATIONS = 2500
START = -0.4+0.59j


@jit
def mandelbrot_colorfult(z: complex) -> float:
    x = 0+0j
    for i in range(MANDELBROT_ITERATIONS):
        #if abs(x) > 10000:
        #    break
        x = x**2 + z

        if abs(x) > 100000:
            return i
        

    return MANDELBROT_ITERATIONS

@jit
def julia(z: complex) -> float:
    for i in range(MANDELBROT_ITERATIONS):
        z = z**2 + START

        if abs(z) > 100:
            return i

    return MANDELBROT_ITERATIONS