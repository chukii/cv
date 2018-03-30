import tkinter as tk

from tkinter import Text
	
root = tk.Tk()
frame = tk.Frame(root)

frame.pack()

def show_WIT():
	T=Text(root)
	T.pack()
	T.insert(tk.END,"This is my CV app")
	#root.mainloop()

def show_AM():
	T=Text(root)
	T.pack()
	T.insert(tk.END,"I am Miguel Ramos, a Systems Engineer")
	#root.mainloop()
btn_about_me=tk.Button(frame,text='About Me',fg='blue',command = show_AM)
btn_what_is_this=tk.Button(frame,text='What is this',fg='green',command=show_WIT)
btn_about_me.pack(side=tk.LEFT)
btn_what_is_this.pack(side=tk.LEFT)
root.mainloop()
