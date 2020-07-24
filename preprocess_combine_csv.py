import pandas as pd
from os import listdir
from os.path import isfile, join

mypath = ""

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


li = []

for filename in onlyfiles:
    df = pd.read_csv(mypath+filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)


frame.to_csv(mypath+"combined.csv", sep=',')
