from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
from motion_detector import df
from bokeh.models import HoverTool,ColumnDataSource

cds=ColumnDataSource(df)
#Start=cds["Start"]
#End=cds["End"]


output_file("plot.html")

f=figure(x_axis_type="datetime",height=250,width=1000,title="motion")
hover=HoverTool(tooltips=[("Start :","@Start"),("End :","@End")])
f.add_tools(hover)
f.quad(left="Start",right="End",bottom=0,top=1,source=cds)

show(f)
