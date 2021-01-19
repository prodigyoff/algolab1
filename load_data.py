import csv
import random
from managers import utilities

if __name__ == '__main__':
    with open('items.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['color', 'max_amount_of_squeezed_juice_in_litres_per_hour',
                             'consumed_power_in_kilowats', 'producer'])
        for i in range(1000):
            csv_writer.writerow(
                [utilities.random_string(10), random.randint(0, 1000), random.randint(0, 1000), utilities.random_string(10)])
