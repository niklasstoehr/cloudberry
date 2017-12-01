import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas
import math

#_________________________________________________________________________________________________________________


datasetTrain = pandas.read_csv('selectedData.csv', engine='python')

column1 = pandas.DataFrame(datasetTrain, columns=['id'])
column2 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_0_0'])
column3 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_1_0'])
column4 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_0_1'])
column5 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_1_1'])
column6 = pandas.DataFrame(datasetTrain, columns=['coordinate_0'])
column7 = pandas.DataFrame(datasetTrain, columns=['coordinate_1'])

dataPandas = pandas.concat([column2, column4], axis=1)
data = dataPandas.as_matrix()



#_________________________________________________________________________________________________________________

# How many entries from data shall be taken
EntryNumber = 200
smallData = data[0:EntryNumber]

c = 2
r = EntryNumber
normalizedData = [[0 for x in range(c)] for y in range(r)]

#print smallData

# normalize
maxNumberSmallDataX = smallData[0][0]
minNumberSmallDataX = smallData[0][0]

maxNumberSmallDataY = smallData[0][1]
minNumberSmallDataY = smallData[0][1]

#_________________________________________________________________________________________________________________

for i in range (0, len(smallData)):

   if (smallData[i][0] < minNumberSmallDataX):
       minNumberSmallDataX = smallData[i][0]

   if (smallData[i][0] > maxNumberSmallDataX):
       maxNumberSmallDataX = smallData[i][0]

   if (smallData[i][1] < minNumberSmallDataY):
       minNumberSmallDataY = smallData[i][1]

   if (smallData[i][1] > maxNumberSmallDataY):
       maxNumberSmallDataY = smallData[i][1]

#_________________________________________________________________________________________________________________

maxNumberSmallDataX += 1
minNumberSmallDataX -= 1

maxNumberSmallDataY += 1
minNumberSmallDataY -= 1


# scaling data to range (-1, 1)
for x in range(0, len(smallData)):

# X Axes
    if (smallData[x][0] < 0):
        normalizeX = (-(1 - ((smallData[x][0]) - (minNumberSmallDataX)) / (maxNumberSmallDataX - (minNumberSmallDataX))))
        normalizedData[x][0] = normalizeX

    elif (smallData[x][0] >= 0):

        normalizeX = ((smallData[x][0]) - (minNumberSmallDataX)) / (maxNumberSmallDataX - (minNumberSmallDataX))
        normalizedData[x][0] = normalizeX

# Y Axes
    if (smallData[x][1] < 0):
        normalizeY = ((smallData[x][0]) - (minNumberSmallDataY)) / (maxNumberSmallDataY - (minNumberSmallDataY))
        normalizedData[x][1] = normalizeY

    elif (smallData[x][1] >= 0):

        normalizeY = ((smallData[x][1]) - (minNumberSmallDataY)) / (maxNumberSmallDataY - (minNumberSmallDataY))
        normalizedData[x][1] = normalizeY

#print normalizedData


#_________________________________________________________________________________________________________________
# Add weight to geographical data

# Creates a list containing 5 lists, each of 8 items, all set to 0

# parameter to be changed
squareFrame = 10;
geoMatrix = np.empty([squareFrame, squareFrame])
geoMatrix.fill(0)

#print normalizedData

for x in range(0, len(normalizedData)):

    # Function y = ( (x + negativeValue ) / MaxValue ) * MaxScale
    xCoordinate = (int)(math.floor((((normalizedData[x][0]) + 1) / 2) * squareFrame))
    #print xCoordinate
    yCoordinate = (int)(math.floor((((normalizedData[x][1]) + 1) / 2) * squareFrame))
    #print yCoordinate

    geoMatrix[xCoordinate][yCoordinate] += 1

print geoMatrix



#_________________________________________________________________________________________________________________
# Display Geomatrix


# find largest value to adjust colour in matrix
largest = 0
for i in range(0,squareFrame):
    for j in range(0,squareFrame):
        if geoMatrix[i][j] > largest:
            largest = geoMatrix[i][j]

print largest



# create discrete colormap
cmap = 'hot'
norm = mpl.colors.Normalize(vmin=0, vmax=largest)

fig, ax = plt.subplots()
ax.imshow(geoMatrix, cmap= cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='none', linestyle='', color='k', linewidth=1)
ax.set_xticks(np.arange(0, squareFrame, squareFrame/4));
ax.set_yticks(np.arange(0, squareFrame, squareFrame/4));

plt.show()

#_________________________________________________________________________________________________________________

