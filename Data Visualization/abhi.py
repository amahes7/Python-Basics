from bokeh.plotting import figure
from bokeh.io import output_file, show

x=[10,12,14,25,17]
y=[40,56,76,54,43]


output_file("graph.html")

f=figure()

f.line(x,y)

show(f)
