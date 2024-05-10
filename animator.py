import math
import pygame
import fractal
from numba import jit
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PIXEL_SIZE = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Frame:
    def __init__(self, x_range: float, y_range:float, pixels: int) -> None:
        self.x_range = x_range
        self.y_range = y_range
        self.pixels = pixels

    

class Animator:
    def __init__(self, function, start: Frame, end: Frame, frames_count: int, x_offset: float, y_offset: float) -> None:
        self.fractal_function = function
        self.start_frame = start
        self.end_frame = end
        self.frames_count = frames_count
        self.frame_counter = 0
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.calculate_la_values()

    
    def next_frame(self, current_frame: Frame) -> Frame:
        x:float = current_frame.x_range
        y:float = current_frame.y_range

        next_x:float = self.start_frame.x_range + float(self.frame_counter) * self.lambda_ * self.direction_x
        next_y:float = self.start_frame.y_range + float(self.frame_counter) * self.lambda_ * self.direction_y

        pixels = self.start_frame.pixels

        next_frame = Frame(next_x, next_y, pixels)

        self.frame_counter += 1

        return next_frame

    def calculate_la_values(self) -> None:
        self.direction_x = self.end_frame.x_range - self.start_frame.x_range
        self.direction_y = self.end_frame.y_range - self.start_frame.y_range

        self.vector_length = math.sqrt(self.direction_x ** 2 + self.direction_y ** 2)
        self.lambda_ = 1.0 / self.frames_count



    def make_frame(self):
        frame = self.start_frame
        factory = fractal.Fractal(self.fractal_function, frame.x_range, frame.y_range, frame.pixels, frame.pixels, self.x_offset, self.y_offset)

        values = factory.make_fractal()

        return values

    def make_animation(self) -> None:
        pygame.init()
        width_height = self.start_frame.pixels

        screen = pygame.display.set_mode((width_height * PIXEL_SIZE, width_height * PIXEL_SIZE))
        screen.fill(WHITE)

        values = self.make_frame()

        for i, row in enumerate(values):
            for j, value in enumerate(row):
                color = WHITE if value else BLACK
                pygame.draw.rect(screen, color, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.quit()

    def show_frames(self) -> None:
        pass

