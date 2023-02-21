import pygame
from frame import Frame
import os

class App:
    """
    Resposible for everything happening within the app and contains app configuration
    """
    BACKGROUND_COLOR = (255, 255, 255)

    def __init__(self, width, height, name):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.X_PAD = 20
        self.Y_PAD = self.HEIGHT // 5
        frame_width = self.WIDTH - self.X_PAD * 2
        frame_height = self.HEIGHT - self.Y_PAD
        self.frame = Frame(self.X_PAD, self.Y_PAD, frame_width, frame_height)
        pygame.display.set_caption(name)

    def define_frame(self, lst, color={}, sorted_elements={}):
        """
        Draw the sorting frame
        :param lst -> list:
        :param color -> dict: dict contains the {index of list: color}
        :param sorted_elements -> dict: {value in the list: color}
        :return:
        """
        self.frame.draw_frame(self.screen)
        self.frame.draw_list(self.screen, lst, self.HEIGHT,
                             colors=color, sorted_elements=sorted_elements)

    def draw_buttons(self, sorting=True):
        if not sorting:
            button = ImageButton(self.screen, pos=(self.X_PAD, self.HEIGHT // 6), img="play_img")
        else:
            button = ImageButton(self.screen, pos=(self.X_PAD, self.HEIGHT// 6), img="pause_img")

    def draw_app(self, lst, sorting, color={}, sorted_elements={}):
        self.screen.fill(self.BACKGROUND_COLOR)
        self.draw_buttons(sorting)

        if sorting:
            self.define_frame(lst, color, sorted_elements)
        else:
            self.define_frame(lst, sorted_elements=sorted_elements)


class Button:
    def __init__(self, screen, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self, mouse_pos):
        """
        :param mouse_pos -> list: mouse click coordinates
        :return: bool
        """
        return False

class ImageButton():
    IMGS = {
        "play_img": "algo_visualizer/button_images/play-button.png",
        "pause_img": "algo_visualizer/button_images/pause-button.png"
    }
    def __init__(self, screen, pos, img):
        """
        :param screen: pygame display
        :param x -> int: x coordinate
        :param y -> int: y coordinate
        :param img -> str: define what image to use
        """
        self.x, self.y = pos
        # self.image = pygame.image.load(self.IMGS[img]).convert()
        # A:\projects\algo_visualizer
        self.image = pygame.image.load(os.path.join(self.IMGS[img]))
        screen.blit(self.image, (self.x,self.y))

    def clicked(self ,mouse_pos):
        x, y = mouse_pos
        return self.image.get_rect().collidepoint(x,y)