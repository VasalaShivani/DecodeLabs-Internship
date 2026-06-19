"""
main.py - The Controller (App Orchestrator)

This file ties the Model and View layers together, implementing the 
Input-Process-Output (IPO) cycle. It coordinates application startup,
runs the menu loop, receives inputs from the View, processes them 
using the Model, and returns results back to the View.

Concepts explained for Interns:
1. Gatekeeper Entry Point: Page 19 of the training kit highlights using 
   `if __name__ == "__main__": main()`. This block ensures that the main() 
   function runs only when this script is executed directly (not when imported 
   by other modules).
2. Input Validation: Inputs must be validated (checking for numbers, non-empty 
   values, etc.) to prevent runtime crashes.
"""

# Import our decoupled Model and View layers
from model import TaskManager
import view

def run_view_tasks(manager):
    """
    Retrieves the list of tasks from the Model and displays them using the View.
    """
    tasks = manager.get_tasks()
    view.display_tasks(tasks)

def run_add_task(manager):
    """
    Prompts the user for a task description, validates it, and adds it.
    """
    task_text = view.prompt_input("Enter the task description: ")
    
    # Input Validation: prevent blank tasks
    if not task_text:
        view.display_message("Task description cannot be empty!", is_error=True)
        return
        
    new_task = manager.add_task(task_text)
    view.display_message(f"Task '{new_task['task']}' added successfully with DB ID: {new_task['id']}!")

def run_toggle_task(manager):
    """
    Prompts the user for a task's database ID and toggles its completion status.
    """
    # Show the tasks first so the user can see current IDs
    run_view_tasks(manager)
    
    id_input = view.prompt_input("Enter the DB ID of the task to toggle: ")
    
    # Validation: Ensure the user typed a valid integer
    try:
        task_id = int(id_input)
    except ValueError:
        view.display_message("Please enter a valid numeric ID.", is_error=True)
        return

    # Process: Call the model to toggle completion
    success = manager.toggle_task_completion(task_id)
    
    # Output: Show success or error
    if success:
        view.display_message(f"Task with DB ID {task_id} status toggled successfully!")
    else:
        view.display_message(f"No task found with DB ID {task_id}.", is_error=True)

def run_delete_task(manager):
    """
    Prompts the user for a task's database ID and deletes it.
    """
    # Show the tasks first so the user can see current IDs
    run_view_tasks(manager)
    
    id_input = view.prompt_input("Enter the DB ID of the task to delete: ")
    
    # Validation: Ensure the user typed a valid integer
    try:
        task_id = int(id_input)
    except ValueError:
        view.display_message("Please enter a valid numeric ID.", is_error=True)
        return

    # Process: Call the model to delete
    success = manager.delete_task(task_id)
    
    # Output: Show success or error
    if success:
        view.display_message(f"Task with DB ID {task_id} deleted successfully!")
    else:
        view.display_message(f"No task found with DB ID {task_id}.", is_error=True)

def main():
    """
    The main application flow and orchestrator loop.
    """
    # Initialize our Model (which automatically loads tasks from tasks.json)
    # The Model represents the storage layer.
    manager = TaskManager(filepath="tasks.json")

    # Clear terminal and display welcome header
    view.clear_screen()
    view.display_welcome()

    # The loop keeps the CLI application running until the user chooses to exit (Option 5)
    while True:
        view.display_menu()
        choice = view.prompt_input("Enter choice (1-5): ")

        if choice == "1":
            run_view_tasks(manager)
        elif choice == "2":
            run_add_task(manager)
        elif choice == "3":
            run_toggle_task(manager)
        elif choice == "4":
            run_delete_task(manager)
        elif choice == "5":
            view.display_message("Thank you for using the DecodeLabs To-Do List app! Goodbye.")
            break
        else:
            view.display_message("Invalid option. Please enter a number between 1 and 5.", is_error=True)

# PAGE 19 CONCEPT: The Gatekeeper
# This standard block checks if the file is run directly or imported.
# It ensures main() starts only when we run 'python main.py' directly.
if __name__ == "__main__":
    main()
