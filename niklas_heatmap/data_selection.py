import csv
import matplotlib.pyplot as plt
import pandas
#convert json into csv by 'json2csv zika.json data.csv'

datasetTrain = pandas.read_csv('data.csv', engine='python')

column1 = pandas.DataFrame(datasetTrain, columns=['id'])
column2 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_0_0'])
column3 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_1_0'])
column4 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_0_1'])
column5 = pandas.DataFrame(datasetTrain, columns=['place_bounding_box_1_1'])
column6 = pandas.DataFrame(datasetTrain, columns=['coordinate_0'])
column7 = pandas.DataFrame(datasetTrain, columns=['coordinate_1'])

selectedColumns = pandas.concat([column1, column2, column3, column4, column5, column6, column7], axis=1)
selectedColumns.to_csv('dataSelected.csv', header=True, index=False)


