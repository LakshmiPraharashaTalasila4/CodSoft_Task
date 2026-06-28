from tkinter import *
from tkinter import messagebox
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def remove_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to remove!")

def delete_all():
    if messagebox.askyesno("Delete All", "Do you want to delete all tasks?"):
        task_listbox.delete(0, END)

def exit_app():
    root.destroy()
root = Tk()
root.title("To-Do List")
root.geometry("600x450")
root.resizable(False, False)

title_label = Label(root, text="TO-DO LIST", font=("Arial", 18, "bold"))
title_label.pack(pady=10)
task_label = Label(root, text="Enter Task:")
task_label.pack()

task_entry = Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=10)

add_btn = Button(button_frame, text="Add", width=15, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

remove_btn = Button(button_frame, text="Remove", width=15, command=remove_task)
remove_btn.grid(row=0, column=1, padx=5)

delete_btn = Button(button_frame, text="Delete All", width=15, command=delete_all)
delete_btn.grid(row=0, column=2, padx=5)

list_frame = Frame(root)
list_frame.pack(pady=10)

scrollbar = Scrollbar(list_frame)

task_listbox = Listbox(
    list_frame,
    width=70,
    height=12,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.pack(side=LEFT)

exit_btn = Button(root, text="Exit", width=20, command=exit_app)
exit_btn.pack(pady=15)

root.mainloop()
