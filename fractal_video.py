import fractal_colorful as fc
import math
import csv
import pygame

PIXEL_SIZE = 1
BLACK = (0, 0, 0)


class Frame:
    def __init__(self, x_range:float, y_range:float) -> None:
        self.x_range = x_range
        self.y_range = y_range

class Fractal_Video:
    def __init__(self, fractal_factory: fc.Fractal_Colorful, end_frame: Frame, frames_count:int, name:str = "Default") -> None:
        self.fractal_factory = fractal_factory
        self.start_frame = Frame(
            fractal_factory.x_range, 
            fractal_factory.y_range)
        self.frames_count = frames_count
        self.frame_counter = 0
        self.end_frame = end_frame
        self.name = name
        self.frames = []
        self.calculate_LA_vals()
    
    def calculate_LA_vals(self) -> None:
        self.direction_x = self.end_frame.x_range - self.start_frame.x_range
        self.direction_y = self.end_frame.y_range - self.start_frame.y_range
        self.vector_length = math.sqrt(self.direction_x**2 + self.direction_y**2)
        self.lambda_ = 1.0 / self.frames_count



    def make_video(self) -> None:
        frames = []

        current_frame = self.start_frame
        loading_counter = 0
        border = int(self.frames_count / 20)
        print("----------------------------------------")
        for i in range(self.frames_count):
            current_frame = self.next_frame()
            self.fractal_factory.x_range = current_frame.x_range
            self.fractal_factory.y_range = current_frame.y_range
            factory = fc.Fractal_Colorful(self.fractal_factory.function, current_frame.x_range, current_frame.y_range, self.fractal_factory.x_steps, self.fractal_factory.y_steps, self.fractal_factory.x_offset, self.fractal_factory.y_offset)

            values = factory.make_fractal()

            if loading_counter == border:
                print("--", end="")
                loading_counter = 0
            else:
                loading_counter += 1

            if len(values) > 0:
                frames.append(values)
            else:
                print("fail")

            print(f"Frame {i} generated")

        with open(self.name + ".csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for frame in frames:
                writer.writerow(','.join([f'{r}:{g}:{b}' for r, g, b in row]) for row in frame)


    def extract_video(self):
        frames = []
        with open(self.name + ".csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                frame = []
                for pixel in row:
                    pixel_data = pixel.split(',')
                    pixel_rgb = [(int(x.split(':')[0]), int(x.split(':')[1]), int(x.split(':')[2])) for x in pixel_data]
                    frame.append(pixel_rgb)
                frames.append(frame)

        return frames

    def show_video(self):
        pass

    def next_frame(self) -> Frame:
        next_x:float = self.start_frame.x_range + self.frame_counter * self.lambda_ * self.direction_x
        next_y:float = self.start_frame.y_range + self.frame_counter * self.lambda_ * self.direction_y

        next_frame:Frame = Frame(next_x, next_y)

        self.frame_counter += 1

        return next_frame

class Fractal_Video_Renderer:
    def __init__(self, fractal_video: Fractal_Video):
        self.fractal_video = fractal_video

    def render_video(self):
        pygame.init()

        height = self.fractal_video.fractal_factory.y_steps
        width = self.fractal_video.fractal_factory.x_steps

        screen = pygame.display.set_mode((width * PIXEL_SIZE, height * PIXEL_SIZE))
        screen.fill(BLACK)

        clock = pygame.time.Clock()

        running = True
        while running:
            for frame in self.fractal_video.frames:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break

                for i, row in enumerate(frame):
                    for j, color in enumerate(row):
                        pygame.draw.rect(screen, color, (i * PIXEL_SIZE, j * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
                
                pygame.display.flip()
                clock.tick(25)
        pygame.quit()

