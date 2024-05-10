import fractal_colorful as fractal
import fractal_frame as frame
import mandelbrot_colorful as mand
"""
start_frame = animator.Frame(0.15, 0.15, 700)

x_offset: float = -0.715
y_offset: float = -0.245

mandelbrot_func = mandelbrot.mandelbrot_function

anim = animator.Animator(mandelbrot_func, start_frame, start_frame, 20, x_offset, y_offset)

anim.make_animation()
anim.run()
"""
mand_func = mand.mandelbrot_colorfult

RANGE = 0.125 #0.0000000002

PIXELS = 500

X_OFFSET = -0.7151

Y_OFFSET = -0.2451

factory = fractal.Fractal_Colorful(
    mand_func, 
    RANGE, 
    RANGE * 2, 
    PIXELS, 
    PIXELS * 2, 
    X_OFFSET, 
    Y_OFFSET)

picture = frame.Frame_Drawer(factory)

picture.draw_frame()

picture.run()