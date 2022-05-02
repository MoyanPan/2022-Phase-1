import csv
from pprint import pprint
transmissions = []
with open("transmissions.csv","r") as file:
    for row in file:
        row = row.strip()
        transmissions.append(row.split(","))
transmissions.pop(0)
ids = [x[0] for x in transmissions]
transdetail = [x[1] for x in transmissions]
sums = []
for x in transmissions:
    str = x[1]
    num = 0
    for i in str:
        try:
            num += int(i)
        except:
            pass
    sums.append(num)
pprint(sums)




