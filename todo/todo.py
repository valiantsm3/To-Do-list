import tkinter as tk
from tkinter import messagebox
import os

task_file = "tasks.txt"

def load_tasks():
    """Load tasks from a file into the listbox."""
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

def save_tasks():
    """Save all tasks to a file."""
    with open(task_file, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a new task to the listbox."""
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    """Delete the selected task from the listbox."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    """Clear all tasks from the listbox."""
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)
        save_tasks()

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#2E2E2E")

# Styling
btn_style = {"bg": "#444", "fg": "white", "font": ("Arial", 12), "bd": 0, "padx": 10, "pady": 5, "activebackground": "#666"}
entry_style = {"bg": "#555", "fg": "white", "font": ("Arial", 12), "insertbackground": "white"}
listbox_style = {"bg": "#333", "fg": "white", "font": ("Arial", 12), "selectbackground": "#555"}

# Entry widget for adding tasks
task_entry = tk.Entry(root, width=40, **entry_style)
task_entry.pack(pady=10)

# Buttons for task management
add_button = tk.Button(root, text="Add Task", command=add_task, **btn_style)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, **btn_style)
clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks, **btn_style)

add_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=15, **listbox_style)
task_listbox.pack(pady=10)

# Load tasks from file
load_tasks()

# Run the application
root.mainloop()
