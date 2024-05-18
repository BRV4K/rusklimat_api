import csv
import os

names_images = {}


def claim_right_images():
    names_images = {}
    directory = 'right_files'
    for brandname in os.scandir(directory):
        if brandname.is_dir():
            for filename in os.scandir(brandname):
                fields = []
                if filename.is_file():
                    with open(filename, newline='', encoding='utf-8') as csvfile:
                        reader = csv.reader(csvfile)
                        counter = 0
                        for row in reader:
                            if counter == 0:
                                fields = row
                                counter += 1
                                continue
                            if row[0][0] == '!':
                                continue
                            image_index = fields.index('Изображения')
                            images = row[image_index:]
                            name = row[0]
                            names_images[name] = images
    return names_images

