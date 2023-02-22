import pygame
from app import App
import random

pygame.init()

class Algo:
    """
    This class will contain all the algorithm and fill out colors
    """
    def __init__(self, lst, app):
        self.lst = lst
        self.len_lst = len(self.lst)
        self.app = app
        self.sorted_elements = {}
    def bubble_sort(self):
        """
        Fill and color blocks according to bubble sort
        :return: void
        """
        #If sorted elements is filled then reset
        self.sorted_elements = {}

        for i in range(self.len_lst - 1):
            for j in range(0, self.len_lst - i - 1):
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    self.app.draw_app(self.lst, True, color={j:"GREEN", j+1:"RED"}, sorted_elements=self.sorted_elements)
                    yield
            self.sorted_elements[self.lst[self.len_lst - 1 - i]] = "ORANGE"
        self.sorted_elements[self.lst[0]] = "ORANGE"
    def selection_sort(self):
        """
        Fill and color blocks according to bubble sort insertion sort
        :return: void
        """
        self.sorted_elements = {}
        for i in range(self.len_lst - 1):
            key = i
            j = i + 1
            while j < self.len_lst:
                if self.lst[key] > self.lst[j]:
                    key = j
                j += 1
                self.app.draw_app(self.lst, True, color={i:"GREEN",key: "YELLOW", j: "RED"}, sorted_elements=self.sorted_elements)
                yield
            self.lst[i], self.lst[key] = self.lst[key], self.lst[i]
            self.sorted_elements[self.lst[i]] = "ORANGE"

        #Fill the last block with orange
        self.sorted_elements[self.lst[self.len_lst - 1]] = "ORANGE"

    def insertion_sort(self):
        for i in range(1, len(self.lst)):
            key = self.lst[i]

            j = i - 1
            while j >= 0 and key < self.lst[j]:
                self.app.draw_app(self.lst, True, color={i: "GREEN", j-1: "RED"},
                                  sorted_elements=self.sorted_elements)
                yield

                self.lst[j + 1] = self.lst[j]
                j -= 1
            self.lst[j + 1] = key


def generate_list(n):
    """
    :param n -> int: list length
    :return: list: a random list of numbers from 1 -> n
    """
    return random.sample(range(1, n + 1) , n)

def main():
    app = App(800, 800, "Algorithm Visualizer")
    LIST_LENGTH = 50
    fps = 30

    lst = generate_list(LIST_LENGTH)
    algo = Algo(lst, app)

    exit = False
    sorting = False
    sorting_algo = algo.bubble_sort()
    algo_name = "bubble_sort"

    clock = pygame.time.Clock()
    while not exit:
        clock.tick(fps)
        if not sorting:
            app.draw_app(algo.lst, sorting, sorted_elements=algo.sorted_elements)
        else:
            try:
                next(sorting_algo)
            except StopIteration:
                sorting = False

        x, y = pygame.mouse.get_pos()
        #Pressing animation
        for button in app.buttons:
            button.check_pressed((x,y))
        app.reset_button.check_pressed((x,y))

        #checking pressed value and change algorithm
        if not sorting:
            for button, name in app.buttons.items():
                if button.clicked((x,y)):
                    algo_name = name
            if algo_name == "bubble_sort":
                sorting_algo = algo.bubble_sort()
                algo_name = "bubble_sort"
            if algo_name == "insertion_sort":
                sorting_algo = algo.insertion_sort()
                algo_name = "insertion_sort"
            if algo_name == "selection_sort":
                sorting_algo = algo.selection_sort()
                algo_name = "selection_sort"

        app.display_sort(algo_name)
        if app.reset_button.clicked((x, y)):
            sorting = False
            algo.sorted_elements = {}
            algo.lst = generate_list(LIST_LENGTH)
            if algo_name == "bubble_sort":
                sorting_algo = algo.bubble_sort()
            elif algo_name == "selection_sort":
                sorting_algo = algo.selection_sort()
            elif algo_name == "insertion_sort":
                sorting_algo = algo.insertion_sort()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if app.play_button.clicked((x, y)):
                    sorting = not sorting

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    sorting = False
                    algo.sorted_elements = {}
                    algo.lst = generate_list(LIST_LENGTH)

                    if algo_name == "bubble_sort":
                        sorting_algo = algo.bubble_sort()
                    if algo_name == "selection_sort":
                        sorting_algo = algo.selection_sort()
                    if algo_name == "insertion_sort":
                        sorting_algo = algo.insertion_sort()

        pygame.display.update()

if __name__ == "__main__":
    main()