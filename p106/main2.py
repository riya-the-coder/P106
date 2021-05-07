import csv
import numpy as np
import plotly.express as px
import pandas as pd


def plotFigure(datapath):
  with open(datapath)as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="sleep in hours",y="Coffee in ml")
    fig.show()

def getDataSource(datapath):
  Coffee=[]
  Sleep=[]
  with open(datapath)as csvfile:
    csvreader=csv.DictReader(csvfile)
    for row in csvreader:
        Coffee.append(float(row["Coffee in ml"]))
        Sleep.append(float(row["sleep in hours"]))
    
  return {"x":Coffee, "y":Sleep}

def findCorrelation(datasource):
  correlation=np.corrcoef(datasource["x"],datasource["y"])
  print("correlation between sleep in hours and Coffee in ml ",correlation[0,1])

def setup():
  datapath="cups of coffee vs hours of sleep.csv"
  datasource=getDataSource(datapath)
  findCorrelation(datasource)
  plotFigure(datapath)

setup()