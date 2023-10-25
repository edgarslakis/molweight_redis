import redis
import csv
import time

r = redis.Redis(
  host='redis-14151.c304.europe-west1-2.gce.cloud.redislabs.com',
  port=14151,
  password='kBb3FEacevRleRecWD2cdKjEZUgbVr7C',
  decode_responses=True)


# Datu bāzē ievieto vismaz 500 ierakstus no CSV faila
with open("dataset.csv", "r", encoding="utf-8") as file:
    print(file)
    reader = csv.reader(file, delimiter=";")
    for line in reader:
        r.set(line[0],line[1])

# Maina 20 ierakstus
with open("dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    interesting_rows = [row for idx, row in enumerate(reader) if idx < 21]
    for row in interesting_rows:
        r.set(row[0],row[2])

# Atlasa 20 ierakstus
with open("dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    cool_rows = [row[0] for idx, row in enumerate(reader) if (idx > 100) & (idx < 121)]
    for row in cool_rows:
        r.get(row)

print("Datubāzes izmērs pirms 20 ierakstu dzēšanas: ", r.dbsize())
# Dzēš 20 ierakstus
with open("dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    boring_rows = [row[0] for idx, row in enumerate(reader) if (idx > 200) & (idx < 221)]
    for row in boring_rows:
        r.delete(row)
print("Datubāzes izmērs pēc 20 ierakstu dzēšanas: ", r.dbsize())

print("Atslēgas, kuras satur patern 'CU...': ", r.keys("CU*"))

r.expire("CUL2", 10)

time.sleep(5)
print("CUL2 vērtība pēc 5 sekundēm: ", r.get("CUL2"))

time.sleep(7)
print("CUL2 vērtība pēc 12 sekundēm: ", r.get("CUL2"))
print("Atslēgas, kuras satur patern 'CU...': ", r.keys("CU*"))
