import tkinter as t
from time import strftime as st

def updatetime():
    currenttime = st('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

root = t.Tk()
root.title("Clock")
label = t.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')
updatetime()
root.mainloop()
