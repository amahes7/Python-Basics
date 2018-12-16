from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("adbe.csv",parse_dates=["Date"])

Date=df["Date"]
Volume=df["Volume"]

print(Date)
print(Volume)
output_file("pp2.html")

f=figure(width=500,height=500, x_axis_type="datetime",responsive=True)
f.title.text="Date vs Volume"
f.title.text_color="blue"
f.title.text_font="times"

f.xaxis.axis_label="Date"
f.yaxis.axis_label="Volume"

f.line(Date,Volume,alpha=0.5)

show(f)
