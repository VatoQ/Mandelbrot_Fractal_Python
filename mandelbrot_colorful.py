from numba import jit

MANDELBROT_ITERATIONS = 2500

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

