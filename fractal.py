from numba import jit

class Fractal:
    def __init__(self, function, x_range: float, y_range: float, x_steps: int, y_steps: int, x_offset: float = 0, y_offset: float = 0) -> None:
        self.function = function
        self.x_range = x_range
        self.y_range = y_range
        self.x_steps = x_steps
        self.y_steps = y_steps
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.calculate_stepsize()

    def calculate_stepsize(self):
        self.x_stepsize = self.x_range / float(self.x_steps)
        self.y_stepsize = self.y_range / float(self.y_steps)


    def make_fractal(self):
        result = []
        x = -self.x_range / 2.0 + self.x_offset
        while x < self.x_range / 2.0 + self.x_offset:
            row = []
            y = -self.y_range / 2.0 + self.y_offset
            while y < self.y_range / 2.0 + self.y_offset:
                z = complex(x, y)
                is_in_set = self.function(z)
                row.append(is_in_set)
                y += self.y_stepsize
            result.append(row)
            x += self.x_stepsize
        return result

    