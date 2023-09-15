import csv
import pyfpgrowth

csv_reader = csv.reader(open('www.csv',mode='r'))
data_array = []
for row in csv_reader:
    data_array.append(row)

min_support1 = 0.001 #equivalent to 100
min_support2 = 0.003
min_support3 = 0.007
min_support4 = 0.01

count = 0
item_counts = {}

patterns1 = pyfpgrowth.find_frequent_patterns(data_array, min_support1)
patterns2 = pyfpgrowth.find_frequent_patterns(data_array, min_support2)
patterns3 = pyfpgrowth.find_frequent_patterns(data_array, min_support3)
patterns4 = pyfpgrowth.find_frequent_patterns(data_array, min_support4)

num_frequent_itemsets1 = 0
num_frequent_itemsets2 = 0
num_frequent_itemsets3 = 0
num_frequent_itemsets4 = 0

num_frequent_itemsets1 = len(patterns1)
num_frequent_itemsets2 = len(patterns2)
num_frequent_itemsets3 = len(patterns3)
num_frequent_itemsets4 = len(patterns4)

print(f"Number of frequent itemsets for min_support1: {num_frequent_itemsets1}")
print(f"Number of frequent itemsets for min_support2: {num_frequent_itemsets2}")
print(f"Number of frequent itemsets for min_support3: {num_frequent_itemsets3}")
print(f"Number of frequent itemsets for min_support4: {num_frequent_itemsets4}")