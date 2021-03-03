# Srijana Shrestha
# 1918305
import csv
csv_file = input()
my_dict = {}

with open(csv_file) as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        for j in i:
            if j in my_dict:
                my_dict[j] = my_dict[j]+1
            else:
                my_dict[j] = 1
for k, v in my_dict.items():
    print(k,v)
