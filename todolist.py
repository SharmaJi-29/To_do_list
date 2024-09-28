import json
import os

TODO_FILE = 'todo_list.json'

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f'Task "{task}" added!')

def remove_task(todo_list):
    display_todo_list(todo_list)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)
            print(f'Task "{removed_task}" removed!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nMenu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
            save_todo_list(todo_list)
        elif choice == '3':
            remove_task(todo_list)
            save_todo_list(todo_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()