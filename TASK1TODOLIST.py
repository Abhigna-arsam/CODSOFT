#importing tkinker....

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = txt_input.get()
    if task != "":
        lb_tasks.insert(tk.END, task)
        txt_input.delete(0, tk.END)
    else:
        messagebox.showwarning(title='Warning!', message='You must enter a task.')

def delete_task():
    try:
        task_index = lb_tasks.curselection()[0]
        lb_tasks.delete(task_index)
    except:
        messagebox.showwarning(title='Warning!', message='You must select a task.')

# create window
window = tk.Tk()

# create GUI elements
window.title("TO DO LIST")
txt_input = tk.Entry(window, width=60)
btn_add_task = tk.Button(window, text='Add task', command=add_task)
btn_del_task = tk.Button(window, text='Delete task', command=delete_task)
lb_tasks = tk.Listbox(window)

# pack elements into window
txt_input.pack()
btn_add_task.pack()
btn_del_task.pack()
lb_tasks.pack()

# run the application
window.mainloop()
  




