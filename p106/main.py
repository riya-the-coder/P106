import numpy as np
import csv 
import plotly.express as px
import pandas as pd

def plotFigure(datapath):
  with open(datapath)as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
    fig.show()

def getDataSource(datapath):
  Marks=[]
  Days=[]
  with open(datapath)as csvfile:
    csvreader=csv.DictReader(csvfile)
  for row in csvreader:
    Marks.append(float(row["Marks In Percentage"]))
    Days.append(float(row["Days Present"]))
    
  return {"x":Marks, "y":Days}

def findCorrelation(datasource):
  correlation=np.corrcoef(datasource["x"],datasource["y"])
  print("correlation between marks in percentage and days present ",correlation[0,1])

def setup():
  datapath="Student Marks vs Days Present.csv"
  datasource=getDataSource(datapath)
  findCorrelation(datasource)
  plotFigure(datapath)

setup()