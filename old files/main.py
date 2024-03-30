from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
def resizer(e):

    global tbg,resized_bg,ttbg

    tbg =Image.open('assets/test.jpg')
    resized_bg = tbg.resize((e.width,e.height), Image.Resampling.LANCZOS)
    ttbg = ImageTk.PhotoImage(resized_bg)
    app_Bg.create_image(0,0,image= ttbg, anchor='nw')


def auth():
    print(user_string.get())
    print(pass_string.get())

    for_testing = True

    if for_testing:
        login_frame.pack_forget()
    else:
        print('db not created')


window = ttk.Window()
window.title('Login')
window.geometry('800x500')
# window.iconbitmap()

bg = PhotoImage(file = "")
app_Bg = Canvas(window, width=800,height=500)
app_Bg.pack(fill='both',expand=True)
app_Bg.create_image(0,0,image= bg, anchor='nw')



login_frame = ttk.Frame(master = window)

title_label = ttk.Label(master = login_frame, text = 'Login',font = 'bebas 15')
title_label.pack()

user_input_frame = ttk.Frame(master = login_frame)
user_string = tk.StringVar()
user_label = tk.Label(master = user_input_frame, text = 'Username:',font = 'bebas 15')
user_input = ttk.Entry(master = user_input_frame, textvariable = user_string)
user_label.pack(side = 'left')
user_input.pack(side = 'left')
user_input_frame.pack()


pass_input_frame = ttk.Frame(master = login_frame)
pass_string = tk.StringVar()
pass_label = tk.Label(master = pass_input_frame, text = 'Passcode:',font = 'bebas 15')
pass_input = ttk.Entry(master = pass_input_frame, textvariable= pass_string)
pass_label.pack(side = 'left')
pass_input.pack(side = 'left')
pass_input_frame.pack()

button_frame = ttk.Frame(master = login_frame)
confirm_button = ttk.Button( master=button_frame , text = 'login', command= auth )
forgot_button = ttk.Button( master=button_frame , text = 'forgot password' )
confirm_button.pack(side='left')
forgot_button.pack(side='left')
button_frame.pack()

window.bind('<Configure>', resizer)

# login_frame.pack()
window.mainloop()
print("hi")