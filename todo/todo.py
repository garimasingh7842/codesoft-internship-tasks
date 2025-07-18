from tkinter import *
from tkinter import messagebox


# Create main window

root = Tk()
root.title("Garima's To-Do List App")
root.geometry("400x500")
root.configure(bg="#b3c0dd")

# List to store tasks
tasks = []

# Function to update the task listbox
def update_listbox():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

# Function to delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

# Function to mark task as done
def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected] = tasks[selected] + " ✔️"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done")

# Title

Label(root, text="My To-Do List", font=("Helvetica", 16), bg="black",fg="white").pack(pady=10)

# Entry box
task_entry = Entry(root, width=30, font=("Helvetica", 14),borderwidth=5,relief=GROOVE,bg="#7ed874")
task_entry.pack(pady=10)

# Buttons
button_frame = Frame(root, bg="pink",borderwidth=5,relief=GROOVE)
button_frame.pack(pady=10)

Button(button_frame, text="Add Task", width=12, command=add_task,bg="blue",fg="white").grid(row=0, column=0, padx=5)
Button(button_frame, text="Delete Task", width=12, command=delete_task,bg="orange",fg="white").grid(row=0, column=1, padx=5)
Button(button_frame, text="Mark Done", width=12, command=mark_done,bg="green",fg="white").grid(row=1, column=0, columnspan=2, pady=5)

# Listbox to display tasks
task_listbox = Listbox(root, width=35, height=15, font=("Helvetica", 12), selectbackground="#4497c1",bg="#df9d57",borderwidth=5,relief=GROOVE)
task_listbox.pack(pady=10)

root.mainloop()
