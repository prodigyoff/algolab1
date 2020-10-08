from managers import utilities


class InsertionSort:
    def __init__(self):
        self.comparsion_counter = 0
        self.swap_counter = 0

    def sort(self, given_list, key=lambda obj: obj):
        indexing_range = range(1, len(given_list))
        for i in indexing_range:
            element_to_sort = given_list[i]

            while key(given_list[i - 1]) > key(element_to_sort) and i > 0:
                self.comparsion_counter += 2
                utilities.swap(given_list, i, i - 1)
                self.swap_counter += 1
                i = i - 1

        return given_list
