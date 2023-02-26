import pygame
from app import App
import random
from algorithm import Algo
pygame.init()
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
        #Draw buttons
        x, y = pygame.mouse.get_pos()
        app.draw_btn((x, y))
        #checking pressed value and change algorithm
        if not sorting:
            #Can only change algorithm when the list is not being sorted
            for button, name in app.buttons.items():
                if button.clicked((x,y)):
                    algo_name = name
            sorting_algo = algo.choose_sort(algo_name=algo_name)

        #Display the current sorting algo
        app.display_sort(algo_name)

        if app.reset_button.clicked((x, y)):
            #Reset the sorted list(the orange blocks), generate new list
            sorting = False
            sorting_algo = algo.reset_list(new_list=generate_list(LIST_LENGTH),algo_name=algo_name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(algo.is_sorted())
                if app.play_button.clicked((x, y)):
                    if sorting:
                        sorting_algo = algo.choose_sort(algo_name="reset")
                    else:
                        if algo.is_sorted():
                            sorting_algo = algo.reset_list(new_list=generate_list(LIST_LENGTH),algo_name=algo_name)
                        else:
                            sorting = True

        pygame.display.update()

if __name__ == "__main__":
    main()