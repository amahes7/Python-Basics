from pandas_datareader import data
import datetime 
from bokeh.plotting import show, figure, output_file

start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)
df= data.DataReader(name="AAPL", data_source="yahoo",start=start,end=end)

output_file("A.html")
f=figure(x_axis_type="datetime",height=250,width=1000,title="candleStick Graph")
a=12*60*60*1000
f.rect(df.index[df.Close > df.Open],(df.Open+df.Close)/2,a,abs(df.Open-df.Close),fill_color="green",line_color="blue")
#f.rect(df.index[df.Close < df.Open],(df.Open+df.Close)/2,a,abs(df.Open-df.Close),fill_color="blue",line_color="green")



show(f)
print(df[df.Close > df.Open])
