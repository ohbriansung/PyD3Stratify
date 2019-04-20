"""
Createding a smaller simple for development.
"""
import csv

with open('./data/in/fire_department_calls_for_service.csv', 'r') as input,\
        open('./data/in/fire_department_calls_for_service_sample.csv', 'w') as output:
    max_count = 4200

    reader = csv.reader(input)
    headers = next(reader)

    reader = csv.DictReader(input, fieldnames=headers)
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()

    for _ in range(max_count):
        row = next(reader)
        writer.writerow(row)
