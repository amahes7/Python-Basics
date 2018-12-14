"""
This stores Title Author ISBN and year of the book
We can Add Select delete and update Entry.
"""

from tkinter import *
from DbOperations import Database

database=Database()



class  Window(object):

        def __init__(self,window):
                self.window=window
                self.window.wm_title("Abhijeet's Bookstore")
                title_label = Label(window,text="Title")
                title_label.grid(row=0, column=0)

                self.title_value=StringVar()
                self.title_input = Entry(window,textvariable=self.title_value)
                self.title_input.grid(row=0, column=1)

                author_label = Label(window,text="Author")
                author_label.grid(row=0,column=2)

                self.author_value=StringVar()
                self.author_input=Entry(window, textvariable=self.author_value)
                self.author_input.grid(row=0, column=3)

                year_label = Label(window,text="Year")
                year_label.grid(row=1, column=0)

                self.year_value=IntVar()
                self.year_input = Entry(window,textvariable=self.year_value)
                self.year_input.grid(row=1, column=1)

                isbn_label=Label(window,text="ISBN")
                isbn_label.grid(row=1,column=2)

                self.isbn_value=IntVar()
                self.isbn_input=Entry(window,textvariable=self.isbn_value)
                self.isbn_input.grid(row=1,column=3)

                pages_label = Label(window,text="Page Count")
                pages_label.grid(row=2, column=0)

                self.pages_value=IntVar()
                self.pages_input = Entry(window,textvariable=self.pages_value)
                self.pages_input.grid(row=2, column=1)

                genre_label=Label(window,text="Genre")
                genre_label.grid(row=2,column=2)

                self.genre_value=StringVar()
                self.genre_input=Entry(window,textvariable=self.genre_value)
                self.genre_input.grid(row=2,column=3)

                view_button=Button(window,text="View All",width=15,command=self.view_all)
                view_button.grid(row=3,column=3)

                search_button=Button(window,text="Search Entry",command=self.search,width=15)
                search_button.grid(row=4,column=3)

                add_button=Button(window,text="Add Entry", command=self.insert,width=15)
                add_button.grid(row=5,column=3)

                update_button=Button(window,text="Update Selected",command=self.update,width=15)
                update_button.grid(row=6,column=3)

                delete_button=Button(window,text="Delete Selected",command=self.delete,width=15)
                delete_button.grid(row=7,column=3)

                close_button=Button(window,text="Reset",command=self.reset,width=15)
                close_button.grid(row=8,column=3)

                close_button=Button(window,text="Close",command=self.window.destroy,width=15)
                close_button.grid(row=9,column=3)

                self.display_area=Listbox(window,height=9, width=50)
                self.display_area.grid(row=4,column=1,rowspan=7,columnspan=1)

                self.action_box=Listbox(window,height=1, width=50)
                self.action_box.grid(row=3,column=1)

                sb=Scrollbar(window)
                sb.grid(row=4,column=2,rowspan=7,columnspan=1)

                self.display_area.configure(yscrollcommand=sb.set)
                sb.configure(command=self.display_area.yview)

                self.display_area.bind('<<ListboxSelect>>',row_id)

        def view_all(self):
                self.display_area.delete(0,END)
                records=database.display_all()
                self.action_box.delete(0,END)
                self.action_box.insert(END,"View all records!!")
                for row in records:
                        self.display_area.insert(END,row)

        def insert(self):
                try:
                        if int(self.year_value.get()) > 0 and int(self.isbn_value.get()) >0 and int(self.pages_value.get()) > 0:
                                database.insert_record(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get(),self.pages_value.get(),self.genre_value.get())
                                self.display_area.delete(0,END)
                                self.action_box.delete(0,END)
                                self.action_box.insert(END,"Record Added!!")
                                for row in database.display_all():
                                        self.display_area.insert(END,row)
                        else:
                                self.display_area.delete(0,END)
                                self.display_area.insert(0,"Enter year, isbn and pages as integer and greater than 0")

                except TclError:
                        self.display_area.delete(0,END)
                        self.display_area.insert(0,"Enter year, isbn and page count as integer")
                        



        def search(self):
                try:
                        if int(self.year_value.get()) == 0 :
                                records=database.search_record (self.title_value.get(),self.author_value.get(),0,self.isbn_value.get(),self.pages_value.get(),self.genre_value.get())
                                self.display_area.delete(0,END)
                                self.action_box.delete(0,END)
                                self.action_box.insert(END,"Displaying Matching results if any!!")
                                for row in records:
                                        self.display_area.insert(END,row)
                        if int(self.isbn_value.get()) == 0 :
                                records=database.search_record (self.title_value.get(),self.author_value.get(),self.year_value.get(),0,self.pages_value.get(),self.genre_value.get())
                                self.display_area.delete(0,END)
                                self.action_box.delete(0,END)
                                self.action_box.insert(END,"Displaying search results if any!!")
                                for row in records:
                                        self.display_area.insert(END,row)
                        if int(self.pages_value.get()) == 0 :
                                records=database.search_record (self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get(),0,self.genre_value.get())
                                self.display_area.delete(0,END)
                                action_box.delete(0,END)
                                action_box.insert(END,"Displaying search results!!")
                                for row in records:
                                        display_area.insert(END,row)
                        if int(isbn_value.get()) == 0 and  int(year_value.get()) == 0 and int(genre_value.get() == 0) :
                                records=database.search_record (title_value.get(),author_value.get(),0,0,0,genre_value.get())
                                display_area.delete(0,END)
                                action_box.delete(0,END)
                                action_box.insert(END,"Displaying search results!!")
                                for row in records:
                                        display_area.insert(END,row)
                except TclError:
                        display_area.delete(0,END)
                        display_area.insert(0,"Enter year, isbn and Page count as integer or enter 0")
                        
                

        def row_id(self,event):
                try:
                        index=self.display_area.curselection()[0]
                        self.selected_row=self.display_area.get(index)
                        id=self.selected_row[0]
                        self.title_value.set(self.selected_row[1])
                        self.author_value.set(self.selected_row[2])
                        self.year_value.set(self.selected_row[3])
                        self.isbn_value.set(self.selected_row[4])
                        self.pages_value.set(self.selected_row[5])
                        self.genre_value.set(self.selected_row[6])

                except IndexError:
                        pass
                print(id)

        def delete(self):
                database.delete_record(id)
                self.display_area.delete(0,END)
                self.action_box.delete(0,END)
                self.action_box.insert(0,"Record Deleted!!")
                for row in database.display_all():
                        self.display_area.insert(END,row)

        def reset(self):
                self.display_area.delete(0,END)
                self.action_box.delete(0,END)
                self.action_box.insert(END,"Reset successful")
                self.title_value.set("Enter a title") 
                self.author_value.set("Enter an Author")
                self.year_value.set(0)
                self.isbn_value.set(0)
                self.pages_value.set(0)
                self.genre_value.set(0)


        def update(self):
                try:
                        if int(self.year_value.get()) > 0 and int(self.isbn_value.get()) >0 and int(self.pages_value.get() >0 ):
                                database.update_record(self.id,self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get(), self.pages_value.get(),self.genre_value.get())
                                self.display_area.delete(0,END)    
                                self.action_box.delete(0,END)    
                                self.action_box.insert(0,"Record Updated!!")
                                for row in database.display_all():
                                        self.display_area.insert(END,row)
                        else:
                                self.display_area.delete(0,END)
                                self.display_area.insert(0,"Enter year and isbn as integer and greater than 0")

                except TclError:
                        self.display_area.delete(0,END)
                        self.display_area.insert(0,"Enter year and isbn as integer")
                        
        def __init__(self,window):
                self.window=window
                self.window.wm_title("Abhijeet's Bookstore")
                title_label = Label(window,text="Title")
                title_label.grid(row=0, column=0)

                self.title_value=StringVar()
                self.title_input = Entry(window,textvariable=self.title_value)
                self.title_input.grid(row=0, column=1)

                author_label = Label(window,text="Author")
                author_label.grid(row=0,column=2)

                self.author_value=StringVar()
                self.author_input=Entry(window, textvariable=self.author_value)
                self.author_input.grid(row=0, column=3)

                year_label = Label(window,text="Year")
                year_label.grid(row=1, column=0)

                self.year_value=IntVar()
                self.year_input = Entry(window,textvariable=self.year_value)
                self.year_input.grid(row=1, column=1)

                isbn_label=Label(window,text="ISBN")
                isbn_label.grid(row=1,column=2)

                self.isbn_value=IntVar()
                self.isbn_input=Entry(window,textvariable=self.isbn_value)
                self.isbn_input.grid(row=1,column=3)

                pages_label = Label(window,text="Page Count")
                pages_label.grid(row=2, column=0)

                self.pages_value=IntVar()
                self.pages_input = Entry(window,textvariable=self.pages_value)
                self.pages_input.grid(row=2, column=1)

                genre_label=Label(window,text="Genre")
                genre_label.grid(row=2,column=2)

                self.genre_value=StringVar()
                self.genre_input=Entry(window,textvariable=self.genre_value)
                self.genre_input.grid(row=2,column=3)

                view_button=Button(window,text="View All",width=15,command=self.view_all)
                view_button.grid(row=3,column=3)

                search_button=Button(window,text="Search Entry",command=self.search,width=15)
                search_button.grid(row=4,column=3)

                add_button=Button(window,text="Add Entry", command=self.insert,width=15)
                add_button.grid(row=5,column=3)

                update_button=Button(window,text="Update Selected",command=self.update,width=15)
                update_button.grid(row=6,column=3)

                delete_button=Button(window,text="Delete Selected",command=self.delete,width=15)
                delete_button.grid(row=7,column=3)

                close_button=Button(window,text="Reset",command=self.reset,width=15)
                close_button.grid(row=8,column=3)

                close_button=Button(window,text="Close",command=self.window.destroy,width=15)
                close_button.grid(row=9,column=3)

                self.display_area=Listbox(window,height=9, width=50)
                self.display_area.grid(row=4,column=1,rowspan=7,columnspan=1)

                self.action_box=Listbox(window,height=1, width=50)
                self.action_box.grid(row=3,column=1)

                sb=Scrollbar(window)
                sb.grid(row=4,column=2,rowspan=7,columnspan=1)

                self.display_area.configure(yscrollcommand=sb.set)
                sb.configure(command=self.display_area.yview)

                self.display_area.bind('<<ListboxSelect>>',self.row_id)


window=Tk()
Window(window)
window.mainloop()