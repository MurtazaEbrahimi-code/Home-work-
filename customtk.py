from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ct
# ----------------------------------------------------------------------------------------------

window = ct.CTk()
window.geometry("680x410+30+30")
window.config(bg='black')
window.title('Home work')
window.resizable(False, False)


# function ----------------------------------------------------------------------------------------------

def HW1():

    tex = ct.CTkTextbox(frame2, font=("Bell MT", 17),width=460,height=360,fg_color='black',border_color='white'
                        ,border_width=8)
    t = open("Home1.txt", 'r').read()
    tex.insert('1.0', t)
    tex.grid(row=0, column=1)


def HW2():
    tex = ct.CTkTextbox(frame2, font=("Bell MT", 17),width=460,height=360,fg_color='black',border_color='white',border_width=8)
    t = open("Home2.txt", 'r').read()
    tex.insert('1.0', t)
    tex.grid(row=0, column=1)


def HW3():
    tex = ct.CTkTextbox(frame2, font=("Bell MT", 17),width=460,height=360,fg_color='black',border_color='white',border_width=8)
    t = open("Home3.txt", 'r').read()
    tex.insert('1.0', t)
    tex.grid(row=0, column=1)


def HW4():
    tex = ct.CTkTextbox(frame2, font=("Bell MT", 17),width=460,height=360,fg_color='black',border_color='white',border_width=8)
    t = open("Home4.txt", 'r').read()
    tex.insert('1.0', t)
    tex.grid(row=0, column=1)


# wiget----------------------------------------------------------------------------------------------

frame1 = ct.CTkFrame(window, width=140, height=360,fg_color='black',border_width=8,border_color='white')
frame1.pack_propagate(False)
frame1.pack(side='left',padx=10)

frame2 = ct.CTkFrame(window, width=140, height=800)
frame2.pack_propagate(False)
frame2.pack(side='left', padx=30)


tex = ct.CTkTextbox(frame2, font=("Bell MT", 11),width=460,height=360,fg_color='black',border_color='white',border_width=8)
labal = ct.CTkLabel(frame2, text="welcome!", font=('Areal', 70),bg_color='black')
labal.place(x=90, y=135)
tex.grid(row=0, column=1)

label = ct.CTkLabel(frame1,text='',fg_color='black',bg_color='black')
btn1 = ct.CTkButton(frame1, text='HW 1', command=HW1, width=70,fg_color='white',text_color='black',hover_color='Gainsboro')
btn2 = ct.CTkButton(frame1, text='HW 2', command=HW2, width=70,fg_color='white',text_color='black',hover_color='Gainsboro')
btn3 = ct.CTkButton(frame1, text='HW 3', command=HW3, width=70,fg_color='white',text_color='black',hover_color='Gainsboro')
btn4 = ct.CTkButton(frame1, text='HW 4', command=HW4, width=70,fg_color='white',text_color='black',hover_color='Gainsboro')

label.pack(pady=9)
btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)


window.mainloop()
