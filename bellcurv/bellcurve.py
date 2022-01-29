from turtle import pd
import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("1.csv")
fig=ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist=False)
fig.show()




