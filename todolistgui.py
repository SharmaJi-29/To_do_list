import tkinter as tk
from tkinter import simpledialog, messagebox
import json

TASKS_FILE = 'tasks.json'

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Edit Task", command=self.edit_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Mark as Complete", command=self.mark_complete).pack(side=tk.LEFT, padx=5)

        self.update_listbox()

    def load_tasks(self):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = '✓' if task['completed'] else '✗'
            self.listbox.insert(tk.END, f"{idx + 1}. {task['title']} [{status}]")

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter the task title:")
        if title:
            self.tasks.append({"title": title, "completed": False})
            self.save_tasks()
            self.update_listbox()

    def edit_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            new_title = simpledialog.askstring("Edit Task", "Enter the new title:", initialvalue=self.tasks[idx]['title'])
            if new_title:
                self.tasks[idx]['title'] = new_title
                self.save_tasks()
                self.update_listbox()
        else:
            messagebox.showwarning("Edit Task", "Select a task to edit.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            del self.tasks[idx]
            self.save_tasks()
            self.update_listbox()
        else:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

    def mark_complete(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]['completed'] = True
            self.save_tasks()
            self.update_listbox()
        else:
            messagebox.showwarning("Mark Complete", "Select a task to mark as complete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
