import random
import string


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def swap(given_element, first_index, second_index):
    given_element[first_index], given_element[second_index] = given_element[second_index], given_element[first_index]


def print_measuring_results(sort_name, comparsion_counter, swap_counter):
    return f'{str.upper(sort_name)} \nComparsions amount: {comparsion_counter}, Swaps amount: {swap_counter}'


def print_elapsed_time(start_time, end_time, sort_name):
    return f'Elapsed {end_time - start_time} seconds to sort with {sort_name} \n\n'
