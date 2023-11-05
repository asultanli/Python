'''

This Python code is a simple graphical user interface (GUI) application using the tkinter library. It creates a to-do list application where you can add tasks, 
delete tasks, clear the entire list, sort the tasks, and exit the application.

'''
from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bg='Black')
window.geometry('400x320')
def add():
    st_lb.insert(END,entry.get())
def delete():
    answer = messagebox.askyesno('Question', 'Are you sure?')
    if answer:
        st_lb.delete(st_lb.curselection()[0])

def clear():
    answer = messagebox.askyesno('Question', 'Are you sure?')
    if answer:
        st_lb.delete(0,END)

def sort():
    list_lb = sorted(list(st_lb.get(0,END)))
    st_lb.delete(0, END)
    for i in list_lb:
        st_lb.insert(END,i)
def exit():
    window.quit()

label =Label(font='Arial 20',text='TASK LIST',bg='black',fg='Gold')
label.grid(row=0,column=0,pady=5)

entry=Entry(font='Arial 15')
entry.grid(column=3,row =0,padx=5)


button = Button(font='Arial 16',text= 'Add',padx='25',bg='grey',command=add)
button.grid(row = 1,column=0)

button1 = Button(font='Arial 16',text= 'Delete',padx='12',bg='grey',command=delete)
button1.grid(row = 2,column=0,pady=10)

button2 = Button(font='Arial 16',text= 'Clear',padx='16',bg='grey',command=clear)
button2.grid(row = 3,column=0)

button3 = Button(font='Arial 16',text= 'Sort',padx='22',bg='grey',command=sort)
button3.grid(row = 4,column=0,pady=10)

button4 = Button(font='Arial 16',text= 'Exit',padx='25',bg='grey',command=exit)
button4.grid(row = 5,column=0)

st_lb = Listbox(font='Arial 15')
st_lb.grid(row=1,column=1,columnspan=5,rowspan=5,pady=10,padx=10)



window.mainloop()