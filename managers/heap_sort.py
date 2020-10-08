from managers import utilities


class HeapSort:
    def __init__(self):
        self.comparsion_counter = 0
        self.swap_counter = 0

    def heapify(self, given_list, heap_size, root_index, key=lambda obj: obj):
        largest_element = root_index
        left_element = 2 * root_index + 1
        right_element = 2 * root_index + 2

        self.comparsion_counter += 2
        if left_element < heap_size and key(given_list[largest_element]) < key(given_list[left_element]):
            largest_element = left_element
            self.swap_counter += 1

        self.comparsion_counter += 2
        if right_element < heap_size and key(given_list[largest_element]) < key(given_list[right_element]):
            largest_element = right_element
            self.swap_counter += 1

        self.comparsion_counter += 1
        if largest_element != root_index:
            utilities.swap(given_list, root_index, largest_element)
            self.swap_counter += 1
            HeapSort.heapify(self, given_list, heap_size, largest_element, key)

    def sort(self, given_list, key=lambda obj: obj):
        heap_size = len(given_list)

        for i in range(heap_size//2, -1, -1):
            HeapSort.heapify(self, given_list, heap_size, i, key)

        for i in range(heap_size - 1, 0, -1):
            utilities.swap(given_list, i, 0)
            HeapSort.heapify(self, given_list, i, 0, key)
