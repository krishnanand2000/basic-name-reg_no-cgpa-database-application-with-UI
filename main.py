import tkinter
from tkinter import *
from tkinter import messagebox
import csv

def main_window():
    info_window = tkinter.Tk(screenName='help me')
    info_window.title("Project BY Krishnanand and Shibin")
    welcome = Label (info_window,text="WELCOME TO SRM INSTITUTE OF SCIENCE AND TECHNOLOGY",justify = CENTER,borderwidth=0,bg = 'CYAN')
    welcome.pack()
    info_window_Frame = Frame(info_window,bd=3,height=500,width=500)
    info_window_Frame.pack()
    sec_line=Label(info_window_Frame,justify=CENTER,text="Enter The Details",borderwidth=0,cursor="ARROW")
    sec_line.grid(row=1,columnspan=3)
    first_name=Label(info_window_Frame,justify=LEFT,text="Enter First Name:",borderwidth=10)
    first_name.grid(row = 2, column = 1)
    global first_name_entry
    first_name_entry=Entry(info_window_Frame,bd=1,justify=LEFT,width=20)
    first_name_entry.grid(row = 2, column = 2)
    Last_name=Label(info_window_Frame,justify=LEFT,text="Enter Last Name:",borderwidth=10)
    Last_name.grid(row = 3, column = 1)
    global last_name_entry
    last_name_entry=Entry(info_window_Frame,bd=1,justify=LEFT,width=20)
    last_name_entry.grid(row =3, column = 2)
    cgpa=Label(info_window_Frame,justify=LEFT,text="Enter Your CGPA:",borderwidth=10)
    cgpa.grid(row = 4, column = 1)
    global cgpa_entry
    cgpa_entry=Entry(info_window_Frame,bd=1,justify=LEFT,width=20)
    cgpa_entry.grid(row =4, column = 2)
    registration_reg=Label(info_window_Frame,justify=LEFT,text="Registration Number:",borderwidth=10)
    registration_reg.grid(row = 5, column = 1)
    global registration_reg_entry
    registration_reg_entry=Entry(info_window_Frame,bd=1,justify=LEFT,width=20)
    registration_reg_entry.grid(row =5, column = 2)
    button=Button(info_window_Frame,text="Submit",justify=CENTER, command=get_values ,borderwidth=10,cursor="arrow",)
    button.grid(row=6,columnspan=3)

    info_window.mainloop()

def message_writing():
    tkinter.messagebox.showwarning(title="Submit",message="Yourr details has been Submitted")
    
def get_values():
        first=first_name_entry.get()
        last=last_name_entry.get()
        reg=registration_reg_entry.get()
        cgpa=cgpa_entry.get()
        write_values(first,last,reg,cgpa)
    
def write_values(first,last,reg,cgpa):
        My_list=[first,last,reg,cgpa]
        with open ('database.csv','a',newline='') as data:
            data.write(str(My_list))
            data.write("\n")
            data.close
        message_writing()

main_window()