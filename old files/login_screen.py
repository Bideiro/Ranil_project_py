from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class Window(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title('Login Screen')
        self.geometry('800x500')
        self.minsize(800,500)


        self.menu = Login(self)
        self.mainloop()



class Login(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)


        

        self.bg()
        self.widgets()


        def resizer(e):
            global tbg,resized_bg,ttbg
            tbg =Image.open('assets/test.jpg')
            resized_bg = tbg.resize((e.width,e.height), Image.Resampling.LANCZOS)
            ttbg = ImageTk.PhotoImage(resized_bg)
            bgpc.create_image(0,0,image= ttbg, anchor='nw')
        self.bind('<Configure>', resizer)
        self.pack(expand=True, fill='both')

    def bg(self):
        global bgpc
        photo = ImageTk.PhotoImage(file='assets/test.jpg')
        bgpc = Canvas(self, width =800, height= 500)
        bgpc.pack( fill='both',expand=True)
        bgpc.create_image(0,0, image = photo , anchor='nw')
        

    def widgets(self):
        ttk.Label(self, text='Login').pack()



    # def layout(self):





Window()