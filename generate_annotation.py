import json
import csv

import os
from tqdm import tqdm

BASE = '/home/alexanderonbysh/SynteticSet20180323/data'
CLS = set()


def json_parse(base_path: str, json_path: str):
    with open(os.path.join(base_path, json_path)) as f:
        data = json.load(f)
    markup = []
    for cls in data:
        class_id = cls['id']
        if class_id == 'noise_bottle':
            continue
        CLS.add(class_id)
        for bbox in cls['data']:
            bbox = bbox['boundingBox']
            markup.append(
                [class_id, json_path[:-4] + 'jpg', bbox['Width'], bbox['Height'], bbox['X'] + bbox['Width'], bbox['X'],
                 bbox['Y'] + bbox['Height'], bbox['Y']])
    return markup


base = []
cut_deeper = []
factor = []
for file in os.listdir(BASE):
    if file.endswith('_cutDeeper.json'):
        cut_deeper.append(file)
    elif file.endswith('_factor.json'):
        factor.append(file)
    elif not file.endswith('.jpg'):
        base.append(file)

for dataset, name in zip((base, cut_deeper, factor), ('base_tf', 'cut_deeper_tf', 'factor_tf')):
    markup = []
    for file in tqdm(dataset):
        markup.extend(json_parse(BASE, file))
    with open(os.path.join('/home/alexanderonbysh/tf', name + '.csv'), 'w') as f:
        f.write(','.join(['class', 'filename', 'height', 'width', 'xmax', 'xmin', 'ymax', 'ymin']) + '\n')
        for val in markup:
            f.write(','.join([str(x) for x in val]) + '\n')

with open('/home/alexanderonbysh/classes.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for i, cls in enumerate(CLS):
        writer.writerow([cls, i])
