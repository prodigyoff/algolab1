from managers import insertion_sort, heap_sort, utilities
from models import squeezer

import csv
import time

if __name__ == '__main__':
    juice_squeezers_list = []
    with open('items.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            juice_squeezers_list.append(squeezer.JuiceSqueezer(color=row[0],
                                                               max_amount_of_squeezed_juice_in_litres_per_hour=row[1],
                                                               consumed_power_in_kilowats=row[2],
                                                               producer=row[3]))

        insertion = insertion_sort.InsertionSort()
        insertion_start_time = time.process_time()
        insertion.sort(juice_squeezers_list, key=lambda juice_squeezer: juice_squeezer.max_amount_of_squeezed_juice_in_litres_per_hour)
        insertion_end_time = time.process_time()
        print(f'INSERTION SORT \n Sorted list: \n{juice_squeezers_list} \n')

        heap = heap_sort.HeapSort()
        heap_start_time = time.process_time()
        heap.sort(juice_squeezers_list,
                  key=lambda juice_squeezer: juice_squeezer.consumed_power_in_kilowats)
        heap_end_time = time.process_time()
        print(f'HEAPSORT \n Sorted list: \n{juice_squeezers_list} \n')

        print(utilities.print_measuring_results("insertion sort", insertion.comparsion_counter, insertion.swap_counter))
        print(utilities.print_elapsed_time(insertion_start_time, insertion_end_time, "insertion"))

        print(utilities.print_measuring_results("heapsort", heap.comparsion_counter, heap.swap_counter))
        print(utilities.print_elapsed_time(heap_start_time, heap_end_time, "heapsort"))
