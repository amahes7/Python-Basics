from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("bachelors.csv")

year=df["Year"]
Engineering=df["Engineering"]


output_file("bach.html")

f=figure()
f.title.text="year vs engineering"
f.title.text_color="red"
f.xaxis.axis_label="year"
f.yaxis.axis_label="Engineering"

f.line(year,Engineering)

show(f)
