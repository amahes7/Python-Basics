from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_excel("verlegenhuken.xlsx")

Temperature=df["Temperature"]/10
Pressure=df["Pressure"]/10


output_file("pp1.html")

f=figure()
f.title.text="Temperature vs Pressure"
f.title.text_color="blue"
f.title.text_font="times"

f.xaxis.axis_label="Temperature"
f.yaxis.axis_label="Pressure"

f.circle(Temperature,Pressure)

show(f)
