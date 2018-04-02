import json
from PIL import Image, ImageDraw


def json_parse(json_path):
    with open(json_path) as f:
        data = json.load(f)
    markup = []
    for cls in data:
        for bbox in cls['data']:
            markup.append(bbox['boundingBox'])
    return markup


path = '/home/alexanderonbysh/SynteticSet20180323/data/GEN_0323002628953_000000'

im = Image.open("{}.jpg".format(path))
draw = ImageDraw.Draw(im)
markup1 = json_parse('{}.json'.format(path))
markup2 = json_parse('{}_cutDeeper.json'.format(path))
markup3 = json_parse('{}_factor.json'.format(path))
for bbox1, bbox2, bbox3 in zip(markup1, markup2, markup3):
    draw.rectangle([bbox1['X'], bbox1['Y'], bbox1['X'] + bbox1['Width'], bbox1['Y'] + bbox1['Height']], outline='red')
    draw.rectangle([bbox2['X'], bbox2['Y'], bbox2['X'] + bbox2['Width'], bbox2['Y'] + bbox2['Height']], outline='blue')
    draw.rectangle([bbox3['X'], bbox3['Y'], bbox3['X'] + bbox3['Width'], bbox3['Y'] + bbox3['Height']], outline='yellow')

# save image
im.save('/home/alexanderonbysh/test.jpg')