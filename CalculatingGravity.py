import pandas as pd
import csv
import plotly.express as px

# Data
star_data = []
with open('dwarf_stars.csv','r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        star_data.append(row)


headers = star_data[0]
star_data = star_data[1:]

# Gravity Calculation

name = []
distance = []
mass = []
radius = []
gravity = []

for star_data in star_data:
    name.append(star_data[1])
    distance.append(star_data[2])
    mass.append(star_data[3])
    radius.append(star_data[4])

star_gravity = []
for (index, name) in enumerate(name):
  gravity = (float(mass[index])*5.972e+24) / (float(radius[index])*float(radius[index])*6371000*6371000) * 6.674e-11
  star_gravity.append(gravity)

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
df.to_csv('Final.csv')  