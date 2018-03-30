import tkinter as tk

from tkinter import Text
	
root = tk.Tk()
frame = tk.Frame(root)

frame.pack()

def show():
	T=Text(root)
	T.pack()
	T.insert(tk.END,"This is my CV app")
	root.mainloop()


btn_about_me=tk.Button(frame,text='About Me',fg='blue')
btn_what_is_this=tk.Button(frame,text='What is this',fg='green',command=show)
btn_about_me.pack(side=tk.LEFT)
btn_what_is_this.pack(side=tk.LEFT)
root.mainloop()
