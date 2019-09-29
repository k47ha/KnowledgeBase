from bs4 import BeautifulSoup
import csv


def process_coordinate_string(str):
    """
    Take the coordinate string from the KML file, and break it up into [Lat,Lon,Lat,Lon...] for a CSV row
    """
    space_splits = str.split(" ")
    ret = []
    # There was a space in between <coordinates>" "-80.123...... hence the [1:]
    for split in space_splits[1:]:
        comma_split = split.split(',')
        ret.append(comma_split[1])    # lat
        ret.append(comma_split[0])    # lng
    return ret


with open('CDD.kml', 'r') as f:
    data = BeautifulSoup(f, 'lxml')

    print(data)

    """
    with open('out.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for coords in s.find_all('coordinates'):
            writer.writerow(process_coordinate_string(coords.string))
    """
