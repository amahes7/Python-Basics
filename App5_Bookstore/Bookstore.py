"""
This stores Title Author ISBN and year of the book
We can Add Select delete and update Entry.
"""

from tkinter import *
import DbOperations

def view_all():
        display_area.delete(0,END)
        records=DbOperations.display_all()
        action_box.delete(0,END)
        action_box.insert(END,"View all records!!")
        for row in records:
                display_area.insert(END,row)

def insert():
        try:
                if int(year_value.get()) > 0 and int(isbn_value.get()) >0 and int(pages_value.get()) > 0:
                        DbOperations.insert_record(title_value.get(),author_value.get(),year_value.get(),isbn_value.get(),pages_value.get(),genre_value.get())
                        display_area.delete(0,END)
                        action_box.delete(0,END)
                        action_box.insert(END,"Record Added!!")
                        for row in DbOperations.display_all():
                                display_area.insert(END,row)
                else:
                        display_area.delete(0,END)
                        display_area.insert(0,"Enter year, isbn and pages as integer and greater than 0")

        except TclError:
                display_area.delete(0,END)
                display_area.insert(0,"Enter year, isbn and page count as integer")
                



def search():
        try:
                if int(year_value.get()) == 0 :
                        records=DbOperations.search_record (title_value.get(),author_value.get(),0,isbn_value.get(),pages_value.get(),genre_value.get())
                        display_area.delete(0,END)
                        action_box.delete(0,END)
                        action_box.insert(END,"Displaying Matching results if any!!")
                        for row in records:
                                display_area.insert(END,row)
                if int(isbn_value.get()) == 0 :
                        records=DbOperations.search_record (title_value.get(),author_value.get(),year_value.get(),0,pages_value.get(),genre_value.get())
                        display_area.delete(0,END)
                        action_box.delete(0,END)
                        action_box.insert(END,"Displaying search results if any!!")
                        for row in records:
                                display_area.insert(END,row)
                if int(pages_value.get()) == 0 :
                        records=DbOperations.search_record (title_value.get(),author_value.get(),year_value.get(),isbn_value.get(),0,genre_value.get())
                        display_area.delete(0,END)
                        action_box.delete(0,END)
                        action_box.insert(END,"Displaying search results!!")
                        for row in records:
                                display_area.insert(END,row)
                if int(isbn_value.get()) == 0 and  int(year_value.get()) == 0 and int(genre_value.get() == 0) :
                        records=DbOperations.search_record (title_value.get(),author_value.get(),0,0,0,genre_value.get())
                        display_area.delete(0,END)
                        action_box.delete(0,END)
                        action_box.insert(END,"Displaying search results!!")
                        for row in records:
                                display_area.insert(END,row)
        except TclError:
                display_area.delete(0,END)
                display_area.insert(0,"Enter year, isbn and Page count as integer or enter 0")
                
        

def row_id(event):
    global selected_row
    global id
    try:
        index=display_area.curselection()[0]
        selected_row=display_area.get(index)
        id=selected_row[0]
        title_value.set(selected_row[1])
        author_value.set(selected_row[2])
        year_value.set(selected_row[3])
        isbn_value.set(selected_row[4])
        pages_value.set(selected_row[5])
        genre_value.set(selected_row[6])

    except IndexError:
        pass
    print(id)

def delete():
    DbOperations.delete_record(id)
    display_area.delete(0,END)
    action_box.delete(0,END)
    action_box.insert(0,"Record Deleted!!")
    for row in DbOperations.display_all():
        display_area.insert(END,row)

def reset():
        display_area.delete(0,END)
        action_box.delete(0,END)
        action_box.insert(END,"Reset successful")
        title_value.set("Enter a title")
        author_value.set("Enter an Author")
        year_value.set(0)
        isbn_value.set(0)
        pages_value.set(0)
        genre_value.set(0)


def update():
        try:
                if int(year_value.get()) > 0 and int(isbn_value.get()) >0 and int(pages_value.get() >0 ):
                        DbOperations.update_record(id,title_value.get(),author_value.get(),year_value.get(),isbn_value.get(), pages_value.get(),genre_value.get())
                        display_area.delete(0,END)    
                        display_area.insert(0,"Record Updated!!")
                        for row in DbOperations.display_all():
                                display_area.insert(END,row)
                else:
                        display_area.delete(0,END)
                        display_area.insert(0,"Enter year and isbn as integer and greater than 0")

        except TclError:
                display_area.delete(0,END)
                display_area.insert(0,"Enter year and isbn as integer")

window=Tk()

window.wm_title("Abhijeet's Bookstore")
title_label = Label(window,text="Title")
title_label.grid(row=0, column=0)

title_value=StringVar()
title_input = Entry(window,textvariable=title_value)
title_input.grid(row=0, column=1)

author_label = Label(window,text="Author")
author_label.grid(row=0,column=2)

author_value=StringVar()
author_input=Entry(window, textvariable=author_value)
author_input.grid(row=0, column=3)

year_label = Label(window,text="Year")
year_label.grid(row=1, column=0)

year_value=IntVar()
year_input = Entry(window,textvariable=year_value)
year_input.grid(row=1, column=1)

isbn_label=Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)

isbn_value=IntVar()
isbn_input=Entry(window,textvariable=isbn_value)
isbn_input.grid(row=1,column=3)

pages_label = Label(window,text="Page Count")
pages_label.grid(row=2, column=0)

pages_value=IntVar()
pages_input = Entry(window,textvariable=pages_value)
pages_input.grid(row=2, column=1)

genre_label=Label(window,text="Genre")
genre_label.grid(row=2,column=2)

genre_value=StringVar()
genre_input=Entry(window,textvariable=genre_value)
genre_input.grid(row=2,column=3)

view_button=Button(window,text="View All",width=15,command=view_all)
view_button.grid(row=3,column=3)

search_button=Button(window,text="Search Entry",command=search,width=15)
search_button.grid(row=4,column=3)

add_button=Button(window,text="Add Entry", command=insert,width=15)
add_button.grid(row=5,column=3)

update_button=Button(window,text="Update Selected",command=update,width=15)
update_button.grid(row=6,column=3)

delete_button=Button(window,text="Delete Selected",command=delete,width=15)
delete_button.grid(row=7,column=3)

close_button=Button(window,text="Reset",command=reset,width=15)
close_button.grid(row=8,column=3)

close_button=Button(window,text="Close",command=window.destroy,width=15)
close_button.grid(row=9,column=3)

display_area=Listbox(window,height=9, width=50)
display_area.grid(row=4,column=1,rowspan=7,columnspan=1)

action_box=Listbox(window,height=1, width=50)
action_box.grid(row=3,column=1)

sb=Scrollbar(window)
sb.grid(row=4,column=2,rowspan=7,columnspan=1)

display_area.configure(yscrollcommand=sb.set)
sb.configure(command=display_area.yview)

display_area.bind('<<ListboxSelect>>',row_id)
window.mainloop()