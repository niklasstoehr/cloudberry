import dataSelector
import grid
import visualizer
import time
import queryDB

#_________________________________________________________________________________________________________________

class Heatmap:

    # samples from data
    #dataSamples = 25585
    #print "dataSamples: ", dataSamples
    # grid squareFrame
    squareFrame = 1000
    print "grid: ", squareFrame, " x ", squareFrame, "\n"

    #query data from AsterixDB
    queryDB.groupBy(squareFrame)



    #get data from json
    startGetData = time.clock()
    # total data 25585
    data = dataSelector.preprocessData('zika.json')
    endGetData = time.clock()
    print "geo data read from json: ", endGetData - startGetData, " seconds"

    # number of samples from selected data
    startSampleData = time.clock()
    sample = dataSelector.getSample(data, dataSamples)
    endSampleData = time.clock()
    print "geo data sampled: ", endSampleData - startSampleData, " seconds"

    #grid
    startNormalizeGrid = time.clock()
    normalizedGrid = grid.normalize(sample, len(sample))
    endNormalizeGrid = time.clock()
    print "grid normalized: ", endNormalizeGrid - startNormalizeGrid, " seconds"

    # includes weightMatrix
    geoMatrix = grid.weightMatrix(normalizedGrid, squareFrame)

    #call smoother after weighting
    #smoothedMatrix = grid.smooth(geoMatrix, squareFrame)

    #visualizer
    visualizer.visualizeHeatmap(geoMatrix, squareFrame)
