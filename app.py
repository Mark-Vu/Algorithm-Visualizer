import pygame
from frame import Frame
import os
import re
pygame.init()


class App:
    """
    Resposible for everything happening within the app and contains app configuration
    """
    BACKGROUND_COLOR = (211, 211, 211)

    def __init__(self, width, height, name):
        """
        :param width -> int: width of the GUI
        :param height -> int: height of the GUI
        :param name -> str: name of the app
        """
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.X_PAD = 20
        self.Y_PAD = self.HEIGHT // 5
        self.frame_width = self.WIDTH - self.X_PAD * 2
        self.frame_height = self.HEIGHT - self.Y_PAD
        self.frame = Frame(self.X_PAD, self.Y_PAD, self.frame_width, self.frame_height)

        pygame.display.set_caption(name)

        #keep tracks of all buttons
        button_count = 4
        button_width = (self.WIDTH//2) // button_count
        button_height = (self.HEIGHT - self.frame_height) // 3.5
        button_gap = 20
        button_x = self.WIDTH // 2 - button_gap * button_count
        self.buttons = {
            Button(self.screen, button_x, 0, button_width,
                   button_height, text='Bubble') : "bubble_sort",

            Button(self.screen, button_x + button_gap + button_width, 0, button_width,
                   button_height, text='Insertion') : "insertion_sort",

            Button(self.screen, button_x + (button_gap + button_width) * 2, 0, button_width,
                   button_height, text='Selection'): "selection_sort",

            Button(self.screen, button_x, button_height + 20, button_width, button_height,
                   text='Merge sort'): "merge_sort",

            Button(self.screen, button_x + button_gap + button_width, button_height + 20, button_width, button_height,
                   text='Quick sort'): "quick_sort",

            Button(self.screen, button_x + (button_gap + button_width) * 2, button_height + 20, button_width, button_height,
                   text='Heap sort'): "heap_sort",

            Button(self.screen, button_x + (button_gap + button_width) * 3, 0, button_width,
                   button_height, text="Shaker"): "shaker_sort",

            Button(self.screen, button_x + (button_gap + button_width) * 3, button_height + 20, button_width,
                   button_height, text="Tim sort"): "tim_sort"
        }
        self.reset_button = Button(self.screen, self.WIDTH-self.X_PAD - 50, self.HEIGHT // 7, 50, 40, text='Reset')

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

    def image_btn(self, sorting=True):
        if not sorting:
            self.play_button = ImageButton(self.screen, pos=(self.X_PAD, self.HEIGHT // 6), img="play_img")
        else:
            self.play_button = ImageButton(self.screen, pos=(self.X_PAD, self.HEIGHT // 6), img="pause_img")

    def draw_btn(self, pos):
        self.reset_button.check_pressed(pos)
        for button in self.buttons:
            button.check_pressed(pos)

    def display_sort(self, algo_name):
        text_color = (20, 20, 20)
        font = pygame.font.SysFont('consolas', 35)
        algo_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', algo_name).title()
        text_surface = font.render(algo_name, True, text_color)
        self.screen.blit(text_surface, (self.X_PAD, self.Y_PAD // 3))

    def draw_app(self, lst, sorting, color={}, sorted_elements={}):
        self.screen.fill(self.BACKGROUND_COLOR)
        self.image_btn(sorting)

        if sorting:
            self.define_frame(lst, color, sorted_elements)
        else:
            self.define_frame(lst, sorted_elements=sorted_elements)


class Button:
    FONT_SIZE = 15
    FONT = pygame.font.SysFont('consolas', FONT_SIZE)
    TEXT_COLOR = (255,255,255)
    def __init__(self, screen, x, y, width, height, text='Button'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.fillColors = {
            'normal': '#272727',
            'hover': '#161616',
            'pressed': (51,51,51),
        }

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_text = self.FONT.render(text, True, self.TEXT_COLOR)


    def check_pressed(self, mouse_pos):
        self.button_surface.fill(self.fillColors['normal'])
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed()[0]:
                self.button_surface.fill(self.fillColors['pressed'])

        self.button_surface.blit(self.button_text, [
            self.button_rect.width / 2 - self.button_text.get_rect().width / 2,
            self.button_rect.height / 2 - self.button_text.get_rect().height / 2
        ])
        self.screen.blit(self.button_surface, self.button_rect)

    def clicked(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]

class ImageButton():
    IMGS = {
        "play_img": "button_images/play-button.png",
        "pause_img": "button_images/pause-button.png",
        "reset_img": "button_images/reset.png"
    }

    def __init__(self, screen, pos, img):
        """
        :param screen: pygame display
        :param x -> int: x coordinate
        :param y -> int: y coordinate
        :param img -> str: define what image to use
        """
        self.x, self.y = pos
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(path, self.IMGS[img])
        self.image = pygame.image.load(file_path)
        screen.blit(self.image, (self.x, self.y))

    def clicked(self, mouse_pos):
        x, y = mouse_pos
        return self.image.get_rect(topleft=(self.x, self.y)).collidepoint(x, y)
