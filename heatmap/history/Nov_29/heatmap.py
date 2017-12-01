import dataSelector
import grid
import visualizer
import time

#_________________________________________________________________________________________________________________

class Heatmap:

    # samples from data
    dataSamples = 2000
    print "dataSamples: ", dataSamples
    # grid squareFrame
    squareFrame = 100
    print "grid: ", squareFrame, " x ", squareFrame, "\n"

    #dataSelector

    #get data from json
    startGetData = time.clock()
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

    # includes weightMatrix calls smoother
    geoMatrix = grid.weightMatrix(normalizedGrid, squareFrame)

    #visualizer
    visualizer.visualizeHeatmap(geoMatrix, squareFrame)
