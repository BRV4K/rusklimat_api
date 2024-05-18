import os
import pandas as pd


def clean_files():
    directory = 'files'
    for brandname in os.scandir(directory):
        if brandname.is_dir():
            for filename in os.scandir(brandname):
                if filename.is_file():
                    with open(filename, newline='', encoding='utf-8') as csvfile:
                        reader = pd.read_csv(csvfile)
                        rows_count = len(reader.index)
                        head = reader.columns

                        for col in range(len(head)):
                            if 'Изображения' in head[col]:
                                first_time_image_index = col
                        columns = {}
                        for col in head[first_time_image_index:]:
                            columns[col] = 'Изображения'
                        reader.dropna(how='all', axis=1, inplace=True)
                        empty_vals = ['']*rows_count
                        reader.insert(loc=1, column='Артикул', value=empty_vals)
                        reader.insert(loc=6, column='Краткая информация', value=empty_vals)
                        reader.insert(loc=8, column='Наклейка', value=empty_vals)
                        reader.insert(loc=10, column='Теги', value=empty_vals)
                        reader.to_csv(filename, index=False)

