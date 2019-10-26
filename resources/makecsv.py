#!/usr/bin/python
import csv
import random

records=60000
print("Making %d records\n" % records)

fieldnames=['name','age','city']
writer = csv.DictWriter(open("people-ages.csv", "w"), fieldnames=fieldnames)

names=['Saray', 'Sandoval', 'Macarena', 'Zulema', 'Anastacia', 'Goya']
cities=['Madrid', 'Floripa', 'Berlin', 'Paris', 'Denver']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('name', random.choice(names)),
    ('age', str(random.randint(10,60))),
    ('city', random.choice(cities))]))