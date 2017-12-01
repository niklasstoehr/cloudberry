import numpy as np
import math
import grid
import visualizer
import time
import json
import queryDB


# _________________________________________________________________________________________________________________

class HeatmapAsterix:


    # query data from AsterixDB
    groupBy = 5.0
    print "groupy size: ", groupBy
    startGetData = time.clock()
    jsonData = queryDB.groupBy(groupBy)
    endGetData = time.clock()
    #print json.dumps(jsonData, indent=4, sort_keys=True)

    asterixTime = jsonData['metrics']['executionTime']
    print 'asterix execution time: ', (asterixTime)
    print "get groupby data: ", endGetData - startGetData, " seconds"

    tweets = jsonData['results'][0]['cnt']
    print 'number of tweets :', tweets
    cells = len(jsonData['results'])-1
    print 'number of grid cells: ', cells
    gridSize = math.sqrt(cells)
    print 'gridSize: ',gridSize,' * ',gridSize


    #geoMatrix = grid
    grid = np.empty([int(gridSize), int(gridSize)])
    grid.fill(0)

    row = 0

    for i in range(0, cells):

        # get count from every cell
        cnt = jsonData['results'][i]['cnt']

        column = int(i%gridSize)
        grid[row][column] = cnt

        if (column == 4):
            row += row


    print grid
