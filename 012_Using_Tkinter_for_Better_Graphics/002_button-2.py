def hello():
    print('hello there')

from tkinter import *
tk = Tk()
btn = Button(tk, text='click me', command=hello)
btn.pack()

# This allows the Tkinter window to open.
tk.mainloop()
