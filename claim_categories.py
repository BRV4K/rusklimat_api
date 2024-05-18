import csv
import os


def claim_right_cats():
    names_categories = {}
    directory = 'right_files'
    for brandname in os.scandir(directory):
        if brandname.is_dir():
            for filename in os.scandir(brandname):
                fields = []
                file_name = str(filename)[11:-6]
                if filename.is_file():
                    with open(filename, newline='', encoding='utf-8') as csvfile:
                        reader = csv.reader(csvfile)
                        counter = 0
                        cat_name = []
                        for row in reader:
                            if counter == 0:
                                fields = row
                                counter += 1
                                continue
                            if row[3] == '':
                                cat_name.append(row[0])
                            else:
                                break
                        names_categories[file_name] = cat_name
    return names_categories
