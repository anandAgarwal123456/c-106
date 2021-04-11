import csv 
import numpy


size = []
time=[]

with open('tv.csv') as tv:
    df = csv.DictReader(tv)
    for info in df:
        size.append(float(info["SizeTV"]))
        time.append(float(info["time"]))

data = {"x" : size, "y" : time}
calculation = numpy.corrcoef(data["x"],data["y"])
print(calculation[0,1])