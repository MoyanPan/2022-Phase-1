import csv
from email import message
from pprint import pprint
from pyexpat.errors import messages
transmissions = []
with open("transmissions.csv","r") as file:
    for row in file:
        row = row.strip()
        transmissions.append(row.split(","))
transmissions.pop(0)
ids = [int(x[0]) for x in transmissions]
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
ASCII = [[ids[i],sums[i]] for i in range(len(sums))]
ASCII = sorted(ASCII, key = lambda x:x[0])
messages = ""
for x in ASCII:
    messages += chr(x[1])
print(messages)


