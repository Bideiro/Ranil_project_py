import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
# import 






log_table = ttk.Treeview(window, columns=('Date','Time','Username','UserID','ActionTypeID'), show= 'headings')
log_table.heading('Date', text='Date')
log_table.heading('Time', text='Time')
log_table.heading('Username', text='Name')
log_table.heading('UserID', text='ID')
log_table.heading('ActionTypeID', text='Action')

log_table.pack(fill='both', expand=True)