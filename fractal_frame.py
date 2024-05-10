import fractal_colorful as fc
import pygame

PIXEL_SIZE = 1
BLACK = (0, 0, 0)

class Fractal_Frame:
    def __init__(self, fractal_factory: fc.Fractal_Colorful) -> None:
        self.fractal_factory = fractal_factory
        self.fractal_frame = self.fractal_factory.make_fractal()

class Frame_Drawer:
    def __init__(self, fractal_factory: fc.Fractal_Colorful) -> None:
        self.fractal_factory = fractal_factory
        self.frame = Fractal_Frame(fractal_factory)
    

    def draw_frame(self) -> None:
        pygame.init()
        height = self.fractal_factory.x_steps
        width = self.fractal_factory.y_steps


        screen = pygame.display.set_mode((width * PIXEL_SIZE, height * PIXEL_SIZE))
        screen.fill(BLACK)

        colors = self.frame.fractal_frame

        for i, row in enumerate(colors):
            for j, color in enumerate(row):
                pygame.draw.rect(screen, color, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()