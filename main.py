import pandas as pd

melcoOutputCsvList = ['0100.csv', '0200.csv', '0300.csv']
PUXOutputCsvList = ['0100.csv', '0200.csv', '0300.csv']
#df = pd.read_csv('0100.csv')
#print(df)
#df.to_csv("0100Result.csv")

for csv in melcoOutputCsvList:
    print(csv)
    df = pd.read_csv('MELCO/' + csv)
    #print(df['GazeLeft'])
    #print(df['GazeLeft'].values.tolist())
    print(df['GazeRight'].values.tolist())

######Marker######
C = [0,0]
WL1 = [-10,0]
WR2 = [20,0]

import os
import glob

movieList=['0100', '0200', '0300']
for movie in movieList:
    print(movie)
    #print(glob.glob(os.path.join('MELCO', '*'+movie+'.csv')))
    df = pd.read_csv(glob.glob(os.path.join('MELCO', '*' + movie + '.csv'))[0])
    print(df['GazeRight'].values.tolist())

    df = pd.read_csv(glob.glob(os.path.join('tag', '*'+movie+'.csv'))[0])
    print(df['Marker'].values.tolist())

