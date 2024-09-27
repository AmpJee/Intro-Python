import os
from typing import Tuple, Optional, List, Dict

# Task structure
Task = Dict[str, str]

# Function to clear the console
def clear_console() -> None:
    """
    Clears the terminal/console window based on the operating system.
    
    Args:
        None
    
    Returns:
        None
    """
    os.system('clear' if os.name == 'posix' else 'cls')

# Function to display the To-do list view with task numbers
def display_todo_list() -> None:
    """
    Displays the To-Do List with task numbers across all categories 
    (Not Started, In Progress, Done).
    
    Args:
        None
    
    Returns:
        None
    """
    clear_console()
    print("** TO-DO LIST **\n" + "=" * 100)
    
    task_count = 1
    for category, task_list in tasks.items():
        category_full = ("Not Started" if category == "n" 
                         else "In Progress" if category == "p" 
                         else "Done")
        print(f"\n{category_full} ({len(task_list)} tasks):")
        print("-" * 100)
        
        for task in task_list:
            print(f"{task_count}. {task['name']}")
            task_count += 1

    print("\n" + "=" * 100)


# Function to find task by number across all categories
def get_task_by_number(
    task_number: int
    ) -> Tuple[Optional[Task], Optional[str], Optional[List[Task]], \
        Optional[int]]:
    """
    Retrieves a task based on its number across all categories 
    (Not Started, In Progress, Done).

    Args:
        task_number (int): The unique task number displayed in the To-Do List.

    Returns:
        tuple: A tuple (task, category, task_list, task_index). Returns the 
        task, category, the list of tasks for that category, and the index 
        of the task in the list.
    """
    count = 1
    for category, task_list in tasks.items():
        for task in task_list:
            if count == task_number:
                return task, category, task_list, task_list.index(task)
            count += 1
    return None, None, None, None


# Function to view a specific task's description by its number
def view_task_description() -> None:
    """
    Prompts the user to enter a task number to view the task's detailed 
    description.

    Args:
        None
    
    Returns:
        None
    """
    display_todo_list()

    try:
        task_number = int(input("Enter the task number to view description: "))
        task, _, _, _ = get_task_by_number(task_number)
        
        if task:
            print("\n** TASK DETAILS **")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to display the Board view (Kanban-style)
def display_board_view() -> None:
    """
    Displays the tasks in a Kanban-style board format with three categories 
    (Not Started, In Progress, Done).

    Args:
        None
    
    Returns:
        None
    """
    clear_console()
    print("** TASK BOARD **\n" + "=" * 120)

    header = f"{'Not Started':<40}{'In Progress':<40}{'Done':<40}"
    print(header)
    print("-" * 120)

    max_len = max(len(tasks["n"]), len(tasks["p"]), len(tasks["d"]))

    for i in range(max_len):
        not_started_task = (tasks["n"][i]["name"] if i < len(tasks["n"]) 
                            else "")
        in_progress_task = (tasks["p"][i]["name"] if i < len(tasks["p"]) 
                            else "")
        done_task = tasks["d"][i]["name"] if i < len(tasks["d"]) else ""
        print(f"{not_started_task:<40}{in_progress_task:<40}{done_task:<40}")

    print("\n" + "=" * 120)


# Function to add a new task
def add_task() -> None:
    """
    Prompts the user to add a new task to a selected category.

    Args:
        None
    
    Returns:
        None
    """
    category = input("Add task to category (n: Not Started, p: In Progress, "
                     "d: Done): ").strip().lower()
    if category not in tasks:
        print("Invalid category.")
        return

    task_name = input("Enter task name: ").strip()
    task_description = input("Enter task description (optional): ").strip()

    tasks[category].append({"name": task_name, "description": task_description})
    print(f"Task '{task_name}' added to '{category.upper()}'.")


# Function to move a task between categories
def move_task() -> None:
    """
    Prompts the user to move a task from one category to another based on 
    the task number.

    Args:
        None
    
    Returns:
        None
    """
    display_todo_list()
    
    try:
        task_number = int(input("Enter task number to move (e.g., 1 for the "
                                "first task in the list): "))
        task, _, task_list_from, task_index = get_task_by_number(task_number)
        
        if not task:
            print("Invalid task number.")
            return

        category_to = input("Move to category (n: Not Started, p: In Progress,"
            " d: Done): ").strip().lower()
        if category_to not in tasks:
            print("Invalid target category.")
            return

        task_list_from.pop(task_index)
        tasks[category_to].append(task)
        print(f"Task '{task['name']}' moved to '{category_to.upper()}'.")

    except ValueError:
        print("Please enter a valid number.")


# Function to remove a task
def remove_task() -> None:
    """
    Prompts the user to remove a task based on the task number.

    Args:
        None
    
    Returns:
        None
    """
    display_todo_list()

    try:
        task_number = int(input("Enter the task number to remove: "))
        task, _, task_list, task_index = get_task_by_number(task_number)
        if task:
            task_list.pop(task_index)
            print(f"Task '{task['name']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu function
def menu() -> None:
    """
    Displays the main menu and handles user input for different operations 
    (View To-Do List, Add Task, Move Task, etc.).

    Args:
        None
    
    Returns:
        None
    """
    while True:
        print("\n** MENU **")
        print("1. View To-do List")
        print("2. View Board")
        print("3. View Task Description")
        print("4. Add Task")
        print("5. Move Task")
        print("6. Remove Task")
        print("7. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            display_board_view()
        elif choice == '3':
            view_task_description()
        elif choice == '4':
            add_task()
        elif choice == '5':
            move_task()
        elif choice == '6':
            remove_task()
        elif choice == '7':
            print("Goodbye! You're gonna miss me! xoxo")
            break
        else:
            print("Invalid choice, please try again.")

# Task dictionary to store tasks by category
tasks: Dict[str, List[Task]] = {
    "n": [  # Not Started
        {"name": "Python Class Work", "description": "Learn Python basics"},
        {"name": "Facial Recognition: HS Tech Team", "description": 
         "Implement facial recognition project"}
    ],
    "p": [  # In Progress
        {"name": "LoC AI Camp 2024", "description": "Prepare for AI camp"},
        {"name": "Design Thinking: Internship", "description": 
         "Work on internship tasks"},
        {"name": "ITMX Hackathon", "description": "Participate in hackathon"}
    ],
    "d": [  # Done
        {"name": "Co-Creator Register", "description": 
         "Complete co-creator registration"}
    ]
}

# Run the application
if __name__ == "__main__":
    menu()
