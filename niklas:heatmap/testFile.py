import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas
import math

#_________________________________________________________________________________________________________________


datasetTrain = pandas.read_csv('dataSelected.csv', engine='python')

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
EntryNumber = 10
smallData = data[0:EntryNumber]
print smallData

c = 2
r = EntryNumber
normalizedData = [[0 for x in range(c)] for y in range(r)]

#print smallData

# normalize
maxNumberSmallDataX
minNumberSmallDataX

maxNumberSmallDataY
minNumberSmallDataY

#_________________________________________________________________________________________________________________

for i in range (len(smallData)):

    smallData[i][0]