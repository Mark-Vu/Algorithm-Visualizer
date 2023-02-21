import pygame
from frame import Frame

class App:
    BACKGROUND_COLOR = (255, 255, 255)
    def __init__(self, width, height, name):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        X_PAD = 20
        Y_PAD = self.HEIGHT // 5
        frame_width = self.WIDTH - X_PAD * 2
        frame_height = self.HEIGHT - Y_PAD
        self.frame = Frame(X_PAD, Y_PAD, frame_width, frame_height)
        pygame.display.set_caption(name)

    def define_frame(self, lst, color={}, sorted_elements={}):
        self.frame.draw_frame(self.screen)
        self.frame.draw_list(self.screen, lst, self.HEIGHT, color, sorted_elements)

    def draw_app(self, lst, sort, color={}, sorted_elements={}):
        self.screen.fill(self.BACKGROUND_COLOR)
        if sort:
            self.define_frame(lst, color, sorted_elements)
        else:
            self.define_frame(lst, sorted_elements=sorted_elements)