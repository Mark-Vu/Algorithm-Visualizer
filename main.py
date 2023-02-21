import pygame
from app import App
import random

pygame.init()

sorted_elements = {}

def bubble_sort(lst, app):
    global sorted_elements
    #If sorted elements is filled then reset
    sorted_elements = {}

    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                app.draw_app(lst, True, color={j:"GREEN", j+1:"RED"}, sorted_elements=sorted_elements)
                yield
        sorted_elements[lst[len(lst) - 1 - i]] = "ORANGE"
    sorted_elements[lst[0]] = "ORANGE"

def insertion_sort(lst, app):
    global sorted_elements
    sorted_elements = {}

    for i in range(1, len(lst)):
        key = lst[i]

        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            app.draw_app(lst, True, color={i: "GREEN", j: "RED"}, sorted_elements=sorted_elements)
            yield
        lst[j + 1] = key
        sorted_elements[i] = "ORANGE"


def generate_list(n):
    return random.sample(range(1, n + 1) , n)

def main():
    global sorted_elements

    app = App(800, 800, "Algorithm Visualizer")
    LIST_LENGTH = 20
    lst = generate_list(LIST_LENGTH)
    print(lst)
    exit = False
    sorting = False
    sorting_algo = bubble_sort(lst, app)
    fps = 5
    clock = pygame.time.Clock()
    while not exit:
        clock.tick(fps)
        if not sorting:
            app.draw_app(lst, sorting, sorted_elements=sorted_elements)
        else:
            try:
                next(sorting_algo)
            except Exception:
                sorting = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    sorting = False
                    sorted_elements = {}
                    lst = generate_list(LIST_LENGTH)

                    sorting_algo = bubble_sort(lst, app)

                if event.key == pygame.K_SPACE:
                    sorting = not sorting

                if event.key == pygame.K_b:
                    sorting_algo = bubble_sort(lst, app)

                if event.key == pygame.K_i:
                    sorting_algo = insertion_sort(lst, app)

        pygame.display.update()

if __name__ == "__main__":
    main()