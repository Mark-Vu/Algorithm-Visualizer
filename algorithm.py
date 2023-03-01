import pygame
from collections import deque
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
        self.comparison = 0
        self.swap = 0

    def sort_list(self):
        """
        sort the list and paint orrange
        """
        for i in self.lst:
            self.filled_sorted(i, "GREEN")
            self.app.draw_app(self.lst, True,color={i:"RED"},
                              sorted_elements=self.sorted_elements)
            yield

    def is_sorted(self):
        """
        :return: -> bool: check if the list is sorted
        """
        for i in range(self.len_lst):
            if self.lst[i] != i + 1:
                return False
        return True
    def filled_sorted(self, val, color):
        self.sorted_elements[val] = color
    def bubble_sort(self):
        """
        Fill and color blocks according to bubble sort
        :return: void
        """
        #If sorted elements is filled then reset
        self.sorted_elements = {}

        for i in range(self.len_lst - 1):
            for j in range(0, self.len_lst - i - 1):
                self.comparison += 1
                self.app.draw_app(self.lst, True, color={j: "GREEN", j + 1: "RED"},
                                  sorted_elements=self.sorted_elements)
                yield
                if self.lst[j] > self.lst[j + 1]:
                    self.swap += 1
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
            self.filled_sorted(self.lst[self.len_lst - 1 - i], "GREEN")
        #Fill the first block
        self.filled_sorted(self.lst[0], "GREEN")
    def selection_sort(self):
        """
        Fill and color blocks according to bubble sort insertion sort
        :return: void
        """
        self.sorted_elements = {}
        for i in range(self.len_lst - 1):
            key = i
            j = i + 1
            self.comparison += 1
            while j < self.len_lst:
                self.comparison += 1
                if self.lst[key] > self.lst[j]:
                    key = j
                j += 1
                self.app.draw_app(self.lst, True, color={i:"GREEN",key: "BLUE", j: "RED"}, sorted_elements=self.sorted_elements)
                yield
            self.lst[i], self.lst[key] = self.lst[key], self.lst[i]
            self.swap += 1
            self.sorted_elements[self.lst[i]] = "GREEN"

        #Fill the last block with GREEN
        self.sorted_elements[self.lst[self.len_lst - 1]] = "GREEN"

    def insertion_sort(self):
        for i in range(1, len(self.lst)):
            key = self.lst[i]
            self.comparison += 1
            j = i - 1
            while j >= 0 and key < self.lst[j]:
                self.comparison += 1
                self.app.draw_app(self.lst, True, color={i: "GREEN", j-1: "RED"},
                                  sorted_elements=self.sorted_elements)
                yield
                self.lst[j + 1] = self.lst[j]
                self.swap += 1
                j -= 1
            self.lst[j + 1] = key

        yield from self.sort_list()

    def merge_sort(self):
        def merge(temp, l, mid, r):
            a = l
            b = l
            c = mid + 1

            while b <= mid and c <= r:
                self.comparison += 1
                self.app.draw_app(self.lst, True, color={b: "RED", c:"GREEN"},
                sorted_elements = self.sorted_elements)
                yield
                if self.lst[b] < self.lst[c]:
                    temp[a] = self.lst[b]
                    b = b + 1
                else:
                    temp[a] = self.lst[c]
                    c = c + 1
                a = a + 1

            # remaining elements
            while b < len(self.lst) and b <= mid:
                self.comparison += 1
                temp[a] = self.lst[b]
                a = a + 1
                b = b + 1

            # copy back
            for b in range(l, r + 1):
                self.app.draw_app(self.lst, True, color={b: "GREEN"},
                                  sorted_elements=self.sorted_elements)
                yield
                self.filled_sorted(self.lst[b], "GREEN")
                self.swap += 1
                self.lst[b] = temp[b]

        low = 0
        high = self.len_lst - 1
        temp = self.lst.copy()
        d = 1
        while d <= high - low:
            self.comparison += 1
            for b in range(low, high, 2 * d):
                l = b
                mid = b + d - 1
                r = min(b + 2 * d - 1, high)
                self.sorted_elements = {}
                yield from merge(temp, l, mid, r)

            d = 2 * d

    def quick_sort(self):
        stack = deque()
        start = 0
        end = len(self.lst) - 1
        stack.append((start, end))

        while stack:
            start, end = stack.pop()

            # rearrange elements across pivot
            pivot = self.lst[end]
            pIndex = start

            for i in range(start, end):
                self.app.draw_app(self.lst, True, color={i: "RED", pivot: "GREEN", pIndex: "RED"},
                                  sorted_elements=self.sorted_elements)
                yield
                self.comparison += 1
                if self.lst[i] <= pivot:
                    self.app.draw_app(self.lst, True, color={i: "RED", pivot: "GREEN", pIndex: "RED"},
                                      sorted_elements=self.sorted_elements)
                    yield
                    self.swap += 1
                    temp = self.lst[i]
                    self.lst[i] = self.lst[pIndex]
                    self.lst[pIndex] = temp
                    pIndex = pIndex + 1

            self.app.draw_app(self.lst, True, color={end: "BLUE", pIndex: "BLUE"},
                              sorted_elements=self.sorted_elements)
            yield
            temp = self.lst[pIndex]
            self.lst[pIndex] = self.lst[end]
            self.lst[end] = temp
            self.swap += 1

            if pIndex - 1 > start:
                self.comparison += 1
                stack.append((start, pIndex - 1))

            # push sublist indices containing elements that are
            # more than the current pIndex to stack
            if pIndex + 1 < end:
                self.comparison += 1
                stack.append((pIndex + 1, end))
        yield from self.sort_list()

    def heap_sort(self):
        def heapify(n, i):
            largest = i
            self.app.draw_app(self.lst, True, color={i: "RED", largest: "GREEN"}, sorted_elements=self.sorted_elements)
            yield
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and self.lst[largest] < self.lst[l]:
                self.comparison += 1
                largest = l
            if r < n and self.lst[largest] < self.lst[r]:
                self.comparison += 1
                largest = r
            self.app.draw_app(self.lst, True, color={i: "RED", largest: "GREEN"}, sorted_elements=self.sorted_elements)
            yield
            if largest != i:
                self.comparison += 1
                self.lst[i], self.lst[largest] = self.lst[largest], self.lst[i]
                self.app.draw_app(self.lst, True, color={i: "RED", largest: "GREEN"}, sorted_elements=self.sorted_elements)
                yield
                self.swap += 1
                yield from heapify(n, largest)

        n = len(self.lst)
        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            self.app.draw_app(self.lst, True, color={0: "RED", i: "GREEN"}, sorted_elements=self.sorted_elements)
            yield
            self.lst[i], self.lst[0] = self.lst[0], self.lst[i]  # swap
            self.swap += 1
            self.sorted_elements[self.lst[i]] = "GREEN"
            yield from heapify(i, 0)

    def shaker_sort(self):
        n = self.len_lst
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                self.comparison += 1
                self.app.draw_app(self.lst, True, color={i: "RED", i + 1: "GREEN"},
                                  sorted_elements=self.sorted_elements)
                yield
                if (self.lst[i] > self.lst[i + 1]):
                    self.swap += 1
                    self.lst[i], self.lst[i+1] = self.lst[i+1], self.lst[i]
                    swapped = True
            if not swapped:
                #Then the list is sorted
                break

            swapped = False
            end -= 1
            for i in range(end-1, start-1, -1):
                self.comparison += 1
                self.app.draw_app(self.lst, True, color={i: "RED", i + 1: "GREEN"},
                                  sorted_elements=self.sorted_elements)
                yield
                if (self.lst[i] > self.lst[i + 1]):
                    self.swap += 1
                    self.lst[i], self.lst[i+1] = self.lst[i+1], self.lst[i]
                    swapped = True
            start += 1
        yield from self.sort_list()

    def shell_sort(self):
        gap = self.len_lst // 2
        while gap > 0:
            j = gap
            while j < self.len_lst:
                i = j - gap
                while i >= 0:
                    self.comparison += 1
                    self.app.draw_app(self.lst, True, color={i + gap: "RED", i: "GREEN"},
                                      sorted_elements=self.sorted_elements)
                    yield
                    if self.lst[i + gap] > self.lst[i]:
                        yield
                        break
                    else:
                        self.lst[i + gap], self.lst[i] = self.lst[i], self.lst[i + gap]
                        yield
                        self.swap += 1

                    i = i - gap
                j += 1
                yield
            gap = gap // 2
        yield from self.sort_list()

    def choose_sort(self, algo_name):
        self.algos = {
            "bubble_sort": self.bubble_sort(),
            "insertion_sort": self.insertion_sort(),
            "selection_sort": self.selection_sort(),
            "merge_sort": self.merge_sort(),
            "quick_sort": self.quick_sort(),
            "heap_sort": self.heap_sort(),
            "shaker_sort": self.shaker_sort(),
            "shell_sort": self.shell_sort()
        }
        if algo_name in self.algos:
            sorting_algo = self.algos[algo_name]

        if algo_name == "reset":
            self.swap = 0
            self.comparison = 0
            self.lst.sort()
            sorting_algo = self.sort_list()

        return sorting_algo

    def reset_list(self, new_list, algo_name):
        """
        Resetting list
        :return: ->func: returning sorting algo for to set current algo
        """
        self.sorted_elements = {}
        self.lst = new_list
        self.swap = 0
        self.comparison = 0
        return self.choose_sort(algo_name=algo_name)