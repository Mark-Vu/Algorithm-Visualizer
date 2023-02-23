import pygame

class Frame:
    """
    This class will be responsible for the sorting frame and blocks configuration
    """
    BLOCK_COLORS = {
        "LIGHT_GREEN": "#7fdca5",
        "BLUE" : "#77C3EC",
        "GREEN" : (0, 255, 0),
        "RED" : (255, 0, 0),
        "ORANGE": (255,165,0),
        "YELLOW": (255,255,0),
        "DARK_GREEN": (1, 50, 32)
    }
    def __init__(self, x, y, frame_width, frame_height):
        self.GAP = 5
        self.x = x
        self.y = y
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.BACKGROUND_COLOR = (24,25,29)

    def draw_frame(self, screen):
        pygame.draw.rect(screen, self.BACKGROUND_COLOR, (self.x, self.y, self.frame_width, self.frame_height))

    def draw_list(self, screen, lst, screen_height, colors={}, sorted_elements={}):
        """
        Draw and coloring the blocks
        :param screen -> pygame display
        :param lst -> list()
        :param screen_height -> int
        :param colors -> dict: for getting the colors of sorting blocks
        :param sorted_elements -> dict: for getting the orange color of sorted blocks
        :return:
        """
        self.block_width = (self.frame_width - ( (len(lst) - 1) * self.GAP) ) / len(lst)
        self.block_height = self.frame_height // (len(lst))
        for i, val in enumerate(lst):
            if i > 0:
                block_x += self.GAP + self.block_width
            else:
                block_x = self.x


            if i in colors:
                c = colors[i]
                color = self.BLOCK_COLORS[c]
            else:
                color = self.BLOCK_COLORS["BLUE"]

            if val in sorted_elements:
                c = sorted_elements[val]
                color = self.BLOCK_COLORS[c]

            block_y = screen_height - self.block_height * val
            pygame.draw.rect(screen, color,
                             (block_x, block_y, self.block_width, self.frame_height) , 0)

