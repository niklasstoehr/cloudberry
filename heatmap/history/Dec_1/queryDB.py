import requests
import json

def groupBy (cellSize):

    # groupBy query; the farwest point: -124.7844079; the southernmost point: 24.7433195; grid size: 5 x 5
    sqlQuery = "use twitter;\nselect spatial_cell(coordinate, create_point(-124.7844079,24.7433195)," + str(cellSize) + "," + str(cellSize) + ") as cell, count(*) as cnt from ds_tweet group by cell;"
    headers = {'Content-type': 'query/service'}

    requestAnswer = requests.post('http://localhost:19002/query/service', headers=headers, data=sqlQuery)
    gridData = requestAnswer.json()

    return gridData
    # print json.dumps(gridData, indent=4, sort_keys=True)


