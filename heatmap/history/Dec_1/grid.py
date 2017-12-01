import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas
import math
import time


def normalize(dataSample, entryNumber):

    c = 2
    r = entryNumber
    normalizedData = [[0 for x in range(c)] for y in range(r)]

    #print smallData

    # normalize
    maxNumberSmallDataX = dataSample[0][0]
    minNumberSmallDataX = dataSample[0][0]

    maxNumberSmallDataY = dataSample[0][1]
    minNumberSmallDataY = dataSample[0][1]

    #_________________________________________________________________________________________________________________

    for i in range (0, len(dataSample)):

       if (dataSample[i][0] < minNumberSmallDataX):
           minNumberSmallDataX = dataSample[i][0]

       if (dataSample[i][0] > maxNumberSmallDataX):
           maxNumberSmallDataX = dataSample[i][0]

       if (dataSample[i][1] < minNumberSmallDataY):
           minNumberSmallDataY = dataSample[i][1]

       if (dataSample[i][1] > maxNumberSmallDataY):
           maxNumberSmallDataY = dataSample[i][1]

    #_________________________________________________________________________________________________________________

    maxNumberSmallDataX += 1
    minNumberSmallDataX -= 1

    maxNumberSmallDataY += 1
    minNumberSmallDataY -= 1


    # scaling data to range (-1, 1)
    for x in range(0, len(dataSample)):

    # X Axes
        if (dataSample[x][0] < 0):
            normalizeX = (-(1 - ((dataSample[x][0]) - (minNumberSmallDataX)) / (maxNumberSmallDataX - (minNumberSmallDataX))))
            normalizedData[x][0] = normalizeX

        elif (dataSample[x][0] >= 0):

            normalizeX = ((dataSample[x][0]) - (minNumberSmallDataX)) / (maxNumberSmallDataX - (minNumberSmallDataX))
            normalizedData[x][0] = normalizeX

    # Y Axes
        if (dataSample[x][1] < 0):
            normalizeY = ((dataSample[x][0]) - (minNumberSmallDataY)) / (maxNumberSmallDataY - (minNumberSmallDataY))
            normalizedData[x][1] = normalizeY

        elif (dataSample[x][1] >= 0):

            normalizeY = ((dataSample[x][1]) - (minNumberSmallDataY)) / (maxNumberSmallDataY - (minNumberSmallDataY))
            normalizedData[x][1] = normalizeY

    return normalizedData



def weightMatrix(normalizedData, squareFrame):

    #time measure
    buildGridTime = 0
    smoothingTime = 0
    weightingTime = 0

    startBuildGrid = time.clock()

    # Add weight to bin of geographical data
    weightToBin = 10

    # Creates a list containing 5 lists, each of 8 items, all set to 0
    # parameter to be changed
    geoMatrix = np.empty([squareFrame, squareFrame])
    geoMatrix.fill(0)

    for x in range(0, len(normalizedData)):

        # Function y = ( (x + negativeValue ) / MaxValue ) * MaxScale
        xCoordinate = (int)(math.floor((((normalizedData[x][0]) + 1) / 2) * squareFrame))
        #print xCoordinate
        yCoordinate = (int)(math.floor((((normalizedData[x][1]) + 1) / 2) * squareFrame))
        #print yCoordinate

        geoMatrix[xCoordinate][yCoordinate] += weightToBin


        #smoothingFunction
        startSmoothingTime = time.clock()
        smooth(geoMatrix, len(normalizedData), weightToBin, squareFrame, xCoordinate, yCoordinate)
        stopSmoothingTime = time.clock()
        smoothingTime = smoothingTime + (stopSmoothingTime - startSmoothingTime)


    endBuildGrid = time.clock()

    weightingTime = (endBuildGrid-startBuildGrid) - smoothingTime
    print "weighting time: ", weightingTime, " seconds"
    print "smoothing time: ", smoothingTime, " seconds"
    return geoMatrix


def smooth(geoMatrix, points, weightToBin, squareFrame, xCoordinate, yCoordinate):

    smoothingRings = 3

    if (xCoordinate-smoothingRings >= 0 & yCoordinate-smoothingRings >= 0 & xCoordinate+smoothingRings < squareFrame & yCoordinate+smoothingRings < squareFrame):

        # ring 1
        # color gradient
        ring1 = 1
        loweredWeightToBin = (weightToBin / 4) + (weightToBin / 2)
        geoMatrix[xCoordinate+ring1][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate-ring1][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate][yCoordinate-ring1] += loweredWeightToBin
        geoMatrix[xCoordinate+ring1][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate-ring1][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate+ring1][yCoordinate-ring1] += loweredWeightToBin
        geoMatrix[xCoordinate-ring1][yCoordinate-ring1] += loweredWeightToBin

        # ring 2
        # color gradient
        ring2 = 2
        loweredWeightToBin = (weightToBin / 2)
        geoMatrix[xCoordinate+ring2][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate + ring2][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate + ring2][yCoordinate - ring1] += loweredWeightToBin

        geoMatrix[xCoordinate][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate + ring1][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate - ring1][yCoordinate + ring2] += loweredWeightToBin

        geoMatrix[xCoordinate-ring2][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate - ring2][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate - ring2][yCoordinate- ring1] += loweredWeightToBin

        geoMatrix[xCoordinate][yCoordinate-ring2] += loweredWeightToBin
        geoMatrix[xCoordinate + ring1][yCoordinate-ring2] += loweredWeightToBin
        geoMatrix[xCoordinate -ring1][yCoordinate - ring2] += loweredWeightToBin

        geoMatrix[xCoordinate+ring2][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate-ring2][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate+ring2][yCoordinate-ring2] += loweredWeightToBin
        geoMatrix[xCoordinate-ring2][yCoordinate-ring2] += loweredWeightToBin


        # ring 3
        # color gradient
        ring3 = 3
        loweredWeightToBin = (weightToBin / 4)

        geoMatrix[xCoordinate][yCoordinate+ring3] += loweredWeightToBin
        geoMatrix[xCoordinate + ring2][yCoordinate+ring3] += loweredWeightToBin
        geoMatrix[xCoordinate - ring2][yCoordinate + ring3] += loweredWeightToBin
        geoMatrix[xCoordinate + ring1][yCoordinate+ring3] += loweredWeightToBin
        geoMatrix[xCoordinate - ring1][yCoordinate + ring3] += loweredWeightToBin

        geoMatrix[xCoordinate-ring3][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate - ring3][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate - ring3][yCoordinate- ring2] += loweredWeightToBin
        geoMatrix[xCoordinate - ring3][yCoordinate + ring1] += loweredWeightToBin
        geoMatrix[xCoordinate - ring3][yCoordinate - ring1] += loweredWeightToBin

        geoMatrix[xCoordinate][yCoordinate-ring3] += loweredWeightToBin
        geoMatrix[xCoordinate + ring2][yCoordinate-ring3] += loweredWeightToBin
        geoMatrix[xCoordinate -ring2][yCoordinate - ring3] += loweredWeightToBin
        geoMatrix[xCoordinate + ring1][yCoordinate-ring3] += loweredWeightToBin
        geoMatrix[xCoordinate -ring1][yCoordinate - ring3] += loweredWeightToBin

        geoMatrix[xCoordinate+ring3][yCoordinate] += loweredWeightToBin
        geoMatrix[xCoordinate + ring3][yCoordinate+ring1] += loweredWeightToBin
        geoMatrix[xCoordinate + ring3][yCoordinate - ring1] += loweredWeightToBin
        geoMatrix[xCoordinate + ring3][yCoordinate+ring2] += loweredWeightToBin
        geoMatrix[xCoordinate + ring3][yCoordinate - ring2] += loweredWeightToBin

        geoMatrix[xCoordinate+ring3][yCoordinate+ring3] += loweredWeightToBin
        geoMatrix[xCoordinate-ring3][yCoordinate+ring3] += loweredWeightToBin
        geoMatrix[xCoordinate+ring3][yCoordinate-ring3] += loweredWeightToBin
        geoMatrix[xCoordinate-ring3][yCoordinate-ring3] += loweredWeightToBin