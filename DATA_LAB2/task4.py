import csv
import pyfpgrowth

csv_reader = csv.reader(open('www.csv', mode='r'))
data_array = []
for row in csv_reader:
    data_array.append(row)

min_support = 0.8  # Set your desired minimum support threshold

# Find frequent itemsets using FP-Growth
patterns = pyfpgrowth.find_frequent_patterns(data_array, min_support)

# Generate association rules from frequent itemsets
rules = pyfpgrowth.generate_association_rules(patterns, min_support)

print(rules)