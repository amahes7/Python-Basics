from pandas_datareader import data
import datetime 
from bokeh.plotting import show, figure, output_file
from bokeh.embed import components
from bokeh.resources import CDN
start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)
df= data.DataReader(name="AAPL", data_source="yahoo",start=start,end=end)
def status(c,o):
    if c > o :
        value="inc"
    elif c < o:
        value="desc"
    else:
        value="equal"
    return value

df["status"]=[status(c,o) for c,o in zip(df.Close,df.Open)]
df["middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

output_file("B.html")
f=figure(x_axis_type="datetime",height=250,width=1000,title="candleStick Graph")
width=12*60*60*1000
f.segment(df.index,df.High,df.index,df.Low)
f.rect(df.index[df.status=="inc"],df.middle[df.status=="inc"],width,df.Height[df.status=="inc"],fill_color="green",line_color="blue")
f.rect(df.index[df.status=="desc"],df.middle[df.status=="desc"],width,df.Height[df.status=="desc"],fill_color="blue",line_color="green")
script1, div1 = components(f)

cdn_js=CDN.js_files
cdn_css=CDN.css_files

print(cdn_js)

#how(f)
#print(df)
