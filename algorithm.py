import pygame

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

    def sort_list(self):
        self.lst.sort()
        for element in self.lst:
            self.filled_sorted(element, "ORANGE")

    def is_sorted(self):
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
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    self.app.draw_app(self.lst, True, color={j:"GREEN", j+1:"RED"}, sorted_elements=self.sorted_elements)
                    yield
            self.filled_sorted(self.lst[self.len_lst - 1 - i], "ORANGE")
        #Fill the first block
        self.filled_sorted(self.lst[0], "ORANGE")
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
        for i in self.lst:
            self.filled_sorted(i, "ORANGE")
            self.app.draw_app(self.lst, True,
                              sorted_elements=self.sorted_elements)
            yield

    def merge_sort(self):
        def merge(temp, l, mid, r):
            a = l
            b = l
            c = mid + 1

            while b <= mid and c <= r:
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
                temp[a] = self.lst[b]
                a = a + 1
                b = b + 1

            # copy back
            for b in range(l, r + 1):
                self.app.draw_app(self.lst, True, color={b: "ORANGE"},
                                  sorted_elements=self.sorted_elements)
                yield
                self.filled_sorted(self.lst[b], "ORANGE")
                self.lst[b] = temp[b]

        low = 0
        high = self.len_lst - 1
        temp = self.lst.copy()
        d = 1
        while d <= high - low:
            for b in range(low, high, 2 * d):
                l = b
                mid = b + d - 1
                r = min(b + 2 * d - 1, high)
                self.sorted_elements = {}
                yield from merge(temp, l, mid, r)

            d = 2 * d

    def choose_sort(self, algo_name):
        if algo_name == "bubble_sort":
            sorting_algo = self.bubble_sort()

        if algo_name == "insertion_sort":
            sorting_algo = self.insertion_sort()

        if algo_name == "selection_sort":
            sorting_algo = self.selection_sort()

        if algo_name == "merge_sort":
            sorting_algo = self.merge_sort()
        return sorting_algo

    def reset_list(self, new_list, algo_name):
        """
        Resetting list
        :return: ->func: returning sorting algo for to set current algo
        """
        self.sorted_elements = {}
        self.lst = new_list
        return self.choose_sort(algo_name=algo_name)