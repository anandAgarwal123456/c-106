import plotly.express as px
import csv 
import numpy

with open('tv.csv') as tv:
    df = csv.DictReader(tv)
    sc = px.scatter(df, x ="SizeTV", y="time")
    sc.show() 
