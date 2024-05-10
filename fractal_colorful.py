import math
import mandelbrot_colorful

class Fractal_Colorful:
    def __init__(self, 
    function, x_range: float, 
    y_range: float, 
    x_steps: int, 
    y_steps: int, 
    x_offset: float = 0, 
    y_offset: float = 0) -> None:
        self.function = function
        self.x_range = x_range / 2.0
        self.y_range = y_range / 2.0
        self.x_steps = x_steps
        self.y_steps = y_steps
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.calculate_stepsize()

    def calculate_stepsize(self):
        self.x_stepsize = (self.x_range * 2) / float(self.x_steps)
        self.y_stepsize = (self.y_range * 2) / float(self.y_steps)

    def make_fractal(self):
        """
        This Function creates an array of RGB values of a fractal within a given
        range and stepsize
        """
        result = []
        x = -self.x_range + self.x_offset
        while x < self.x_range + self.x_offset:
            row = []
            y = -self.y_range + self.y_offset
            while y < self.y_range + self.y_offset:
                z = complex(x, y)
                abs_value = self.function(z)
                color = (0, 0, 0)
                if abs_value < mandelbrot_colorful.MANDELBROT_ITERATIONS:
                    #print(abs_value)
                    if abs_value == float('inf'):
                        abs_value = 50

                    """
                    log_2 (obs_value + 55) is calculated to make prettier colors basically.
                    It makes it so that the colors are mainly in the green spectrum, 
                    where we can recognize more nuanced differences.
                    To see what it does graph the functions a, b, c:
                    
                    h(x) = log_2(x+55)

                    a(x)=-127.5*cos(h(x))+127.5
                    b(x)=127.5*sin(h(x))+127.5
                    c(x)=255*cos^2(h(x))
                    """
                    abs_value = math.log2(abs_value + 55)
                    Red = int(-127.5*math.cos(abs_value)+127.5)
                    Green = int(127.5*math.sin(abs_value)+127.5)
                    Blue = int(255*math.sin(abs_value)**2)
                    color = (Red, Green, Blue)
                row.append(color)
                y += self.y_stepsize
            result.append(row)
            x += self.x_stepsize
        return result