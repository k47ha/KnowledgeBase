import csv
import json
from geojson import Feature, FeatureCollection, Point

features = []

with open('CDD_cleaned.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    for latitude, longitude, weather, temp in reader:
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry=Point((longitude, latitude)),
                properties={
                    'weather': weather,
                    'temp': temp
                }
            )
        )

collection = FeatureCollection(features)
with open("GeoObsCDD.json", "w") as f:
    f.write('%s' % collection)
