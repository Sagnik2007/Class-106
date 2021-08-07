import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            time_spent.append(float(row["Time Spent Watching The Television in the week(hours)"]))

    return{"x" : size_of_tv, "y" : time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(("Correlation between size of TV and time spent watching the TV in a week:- \n--->",correlation[0,1"))

def setup():
    data_path = "size_vs_time.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()