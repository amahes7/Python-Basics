from tkinter import *

def miles_to_km():
    km=float(e1_value.get())/1.6
    t1.insert(END,km)
window= Tk()
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
t1=Text(window,height=1,width=35)
t1.insert(END,"Km Values: ")
t1.grid(row=0,column=2)
b1=Button(window,text="Calculate Km",command=miles_to_km)
b1.grid(row=0,column=0)

window.mainloop()
