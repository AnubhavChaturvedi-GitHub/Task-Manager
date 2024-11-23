import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import keyboard

# Task board class
class TaskBoard:
    def __init__(self):
        self.tasks = []

    def show_task_board(self):
        root = tk.Tk()
        root.title("Advanced Task Board")
        root.geometry("500x400")
        root.configure(bg="#f2f2f2")
        
        # Title
        title_label = tk.Label(
            root,
            text="Your Task Board",
            font=("Arial", 18, "bold"),
            fg="#333",
            bg="#f2f2f2",
            pady=10
        )
        title_label.pack()

        # Frame for tasks and buttons
        main_frame = tk.Frame(root, bg="#f2f2f2")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollable task list
        task_list_frame = tk.Frame(main_frame, bg="#f2f2f2")
        task_list_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        task_scroll = tk.Scrollbar(task_list_frame, orient=tk.VERTICAL)
        task_list = tk.Listbox(
            task_list_frame,
            font=("Arial", 12),
            height=15,
            width=50,
            yscrollcommand=task_scroll.set,
            selectbackground="#87ceeb",
            selectforeground="#fff"
        )
        task_scroll.config(command=task_list.yview)
        task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        task_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Populate the listbox
        for task in self.tasks:
            task_list.insert(tk.END, task)

        # Buttons frame
        button_frame = tk.Frame(main_frame, bg="#f2f2f2")
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Add Task Button
        def add_task():
            task = simpledialog.askstring("Add Task", "Enter a new task:")
            if task:
                self.tasks.append(task)
                task_list.insert(tk.END, task)

        add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
        add_button.grid(row=0, column=0, padx=5)

        # Remove Task Button
        def remove_task():
            selected_task = task_list.curselection()
            if selected_task:
                task_index = selected_task[0]
                task_list.delete(task_index)
                self.tasks.pop(task_index)
            else:
                messagebox.showinfo("Info", "Please select a task to remove.")

        remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
        remove_button.grid(row=0, column=1, padx=5)

        # Clear All Tasks Button
        def clear_tasks():
            if messagebox.askyesno("Clear All Tasks", "Are you sure you want to clear all tasks?"):
                task_list.delete(0, tk.END)
                self.tasks.clear()

        clear_button = ttk.Button(button_frame, text="Clear All", command=clear_tasks)
        clear_button.grid(row=0, column=2, padx=5)

        # Exit Button
        exit_button = ttk.Button(button_frame, text="Close", command=root.destroy)
        exit_button.grid(row=0, column=3, padx=5)

        # Grid resizing
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Keep the window open
        root.mainloop()

# Initialize the task board
task_board = TaskBoard()

# Define the hotkey
def open_task_board():
    task_board.show_task_board()

# Set the hotkey
keyboard.add_hotkey("ctrl+shift+z", open_task_board)

print("Press Ctrl + Shift + Z to open the task board...")
keyboard.wait("esc")  # Keeps the script running; press Esc to exit
