import csv
import pyfpgrowth

rows = 0
queries = []

with open('www.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")

    next(csv_reader) #dont print the column

    for line in csv_reader:
        rows+=1
        queries.append(line[1])

patterns = pyfpgrowth.find_frequent_patterns(queries, 100)