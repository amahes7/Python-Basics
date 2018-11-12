from tkinter import *


def kg_Conversion():
    kg_float_value=float(kg_value.get())
    gram_value.delete(1.0,END)
    pounds_value.delete(1.0,END)
    ounce_value.delete(1.0,END)
    gram_value.insert(END,kg_float_value*1000)
    pounds_value.insert(END,kg_float_value*2.20462)
    ounce_value.insert(END,kg_float_value*35.274)

window=Tk()
kgLabel= Label(window,text="Please Enter KG:")
kgLabel.grid(row=0,column= 0)

kg_value=StringVar()
kg_input=Entry(window,textvariable=kg_value)
kg_input.grid(row=0,column=1)

convert_button= Button(window,text="Convert", command=kg_Conversion)
convert_button.grid(row=0,column=2)

gram_value=Text(window,height=1,width=35)
gram_value.insert(END,"Gram Value: ")
gram_value.grid(row=1,column=0)

pounds_value=Text(window,height=1,width=35)
pounds_value.insert(END,"Pounds Value: ")
pounds_value.grid(row=1,column=1)

ounce_value=Text(window,height=1,width=35)
ounce_value.insert(END,"Ounce Value: ")
ounce_value.grid(row=1,column=2)

window.mainloop()