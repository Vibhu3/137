import pandas as pd
import matplotlib.pyplot as plt
import csv

df = []
with open('stars.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:
    if i != []:
      df.append(i)

headers = df[0]
headers[0] = 'Index'
data = df[1:]

stars_filtered_with_distance = []
for i in data:
  if float(i[2]) <= 100:
    stars_filtered_with_distance.append(i)
  else:
    pass

stars_filtered_with_gravity = []
for i in stars_filtered_with_distance:
  if float(i[5].split(' ')[0]) > 150 and float(i[5].split(' ')[0]) < 350:
    stars_filtered_with_gravity.append(i)
  else:
    pass

print('number of stars with distance less than 100 lightyears: ',len(stars_filtered_with_distance))
print('number of stars with gravity within 150-350 m/s2 : ',len(stars_filtered_with_gravity))

with open('filtered_stars.csv','w') as f:
  csvWriter = csv.writer(f)
  csvWriter.writerow(headers)
  csvWriter.writerows(stars_filtered_with_gravity)