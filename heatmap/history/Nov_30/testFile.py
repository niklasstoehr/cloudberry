import json
import pandas as pd

json_string = json.loads(open("zika.json", "r").read())

x1 = []
x2 = []
y1 = []
y2 = []

for i in range(0, len(json_string)):

    x1Coordinate = json_string[i]['place']['bounding_box'][1][0]
    x2Coordinate = json_string[i]['place']['bounding_box'][0][0]
    y1Coordinate = json_string[i]['place']['bounding_box'][0][1]
    y2Coordinate = json_string[i]['place']['bounding_box'][1][1]

    x1.append({'bounding_box_1_0': x1Coordinate})
    x2.append({'bounding_box_0_0': x2Coordinate})
    y1.append({'bounding_box_0_1': y1Coordinate})
    y2.append({'bounding_box_1_1': y2Coordinate})


x1DF = pd.DataFrame(x1)
x2DF = pd.DataFrame(x2)
y1DF = pd.DataFrame(y1)
y2DF = pd.DataFrame(y2)

xDF = pd.concat([x1DF, x2DF], axis=1)
print xDF

yDF = pd.concat([y1DF, y2DF], axis=1)
print yDF

print pd.concat([xDF[['bounding_box_1_0', 'bounding_box_0_0']].mean(axis=1), yDF[['bounding_box_0_1', 'bounding_box_1_1']].mean(axis=1)], axis=1).as_matrix()