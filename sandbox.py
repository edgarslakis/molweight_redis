import csv

table = []
with open("dataset.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        
        for line in reader:
            table.append(line[0])

with open("dataset.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        interesting_rows = [row[0] for idx, row in enumerate(reader) if (idx > 10) & (idx < 30)]

#print(table[1:6])
print(interesting_rows)