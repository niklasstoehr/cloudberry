import json
import pandas as pd



def preprocessData(jsonName):

    json_string = json.loads(open(jsonName, "r").read())

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
    #print xDF

    yDF = pd.concat([y1DF, y2DF], axis=1)
    #print yDF

    return pd.concat([xDF[['bounding_box_1_0', 'bounding_box_0_0']].mean(axis=1),
                     yDF[['bounding_box_0_1', 'bounding_box_1_1']].mean(axis=1)], axis=1).as_matrix()



def getSample(data, entryNumber):

    smallData = data[0:entryNumber]

    return smallData















"""
CSV


import pandas as pd
import numpy as np
import random
#convert json into csv by 'json2csv zika.json data.csv'

def readInitialData(csvName):

    readDataset = pd.read_csv(csvName, engine='python')

    column1 = pd.DataFrame(readDataset, columns=['id'])
    column2 = pd.DataFrame(readDataset, columns=['place_bounding_box_0_0'])
    column3 = pd.DataFrame(readDataset, columns=['place_bounding_box_1_0'])
    column4 = pd.DataFrame(readDataset, columns=['place_bounding_box_0_1'])
    column5 = pd.DataFrame(readDataset, columns=['place_bounding_box_1_1'])
    #column6 = pd.DataFrame(readDataset, columns=['coordinate_0'])
    #column7 = pd.DataFrame(readDataset, columns=['coordinate_1'])

    selectedColumns = pd.concat([column1, column2, column3, column4, column5], axis=1)
    #print selectedColumns
    selectedColumns.to_csv('selectedData.csv', header=True, index=False)


def preprocessData():

    df = pd.read_csv('selectedData.csv', engine='python')

    x1 = 'place_bounding_box_1_0'
    x2 = 'place_bounding_box_0_0'

    y1 = 'place_bounding_box_1_1'
    y2 = 'place_bounding_box_0_1'

    #print pd.concat([df[[x1, x2]].mean(axis=1), df[[y1, y2]].mean(axis=1)], axis=1).as_matrix()
    return pd.concat([df[[x1, x2]].mean(axis=1), df[[y1, y2]].mean(axis=1)], axis=1).as_matrix()


def getSample(data, entryNumber):

    smallData = data[0:entryNumber]

    return smallData

"""