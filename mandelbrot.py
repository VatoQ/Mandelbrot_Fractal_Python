from numba import jit

MANDELBROT_ITERATIONS = 100

@jit
def mandelbrot_function(z: complex) -> bool:
    x = 0+0j
    is_in_set:bool = True
    for i in range(MANDELBROT_ITERATIONS):
        x = x**2 + z
        if abs(x) > 10:
            is_in_set = False
            break

    return is_in_set

    
