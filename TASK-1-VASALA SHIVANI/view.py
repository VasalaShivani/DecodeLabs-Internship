"""
view.py - The View Layer (User Interface)

This file is responsible for what the user sees in the terminal.
It contains functions to display menus, print stylized lists of tasks, 
and gather inputs from the user.

Concepts explained for Interns:
1. separation of concerns: The view doesn't decide what data to save or delete. 
   It only receives data from the controller and formats it nicely on the screen.
2. Pythonic enumeration: Page 11 of the training kit emphasizes using `enumerate()`.
   Instead of using `range(len(tasks))` which is manual and prone to index errors, 
   `enumerate(tasks)` yields BOTH the list index and the item dictionary in a single, clean loop.
"""

import sys

def clear_screen():
    """
    Clears the console screen for a clean user interface.
    Works on both Windows (cls) and Unix-like systems (clear).
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """
    Prints a beautiful, professional startup banner.
    """
    print("=" * 60)
    print("         DECODELABS PYTHON INDUSTRIAL TRAINING KIT")
    print("                 PROJECT 1: THE TO-DO LIST")
    print("=" * 60)
    print("   Build a solid backend foundation with structured logic.")
    print("=" * 60)
    print()

def display_menu():
    """
    Prints the menu choices for the user.
    """
    print("\n--- OPTIONS ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Toggle Task Completion")
    print("4. Delete Task")
    print("5. Exit Application")
    print("-" * 15)

def display_tasks(tasks):
    """
    Prints the task list in a structured, readable format.
    Uses enumerate() to provide list indexes (1-based for users)
    alongside the task details (database row ID, task text, status).
    
    :param tasks: List of task dictionaries
    """
    if not tasks:
        print("\n[!] Your task list is currently empty.")
        return

    print("\n" + "=" * 60)
    # Header showing columns: List Index, DB ID, Completion Status, Task Content
    print(f"{'No.':<4} | {'DB ID':<5} | {'Status':<8} | {'Task Description'}")
    print("-" * 60)

    # PAGE 11 CONCEPT: The Professional Way to iterate with index
    # enumerate(iterable, start=1) makes the index 1-based for friendly human reading
    for index, task in enumerate(tasks, start=1):
        # Determine status symbol: ✓ checkmark for completed, empty bracket for pending
        status_symbol = "[✓]" if task["completed"] else "[ ]"
        
        # Format columns:
        # Index: left-aligned, width 4
        # DB ID: left-aligned, width 5
        # Status: left-aligned, width 8
        # Task text: print normally
        print(f"{index:<4} | {task['id']:<5} | {status_symbol:<8} | {task['task']}")
    
    print("=" * 60)

def prompt_input(prompt_text):
    """
    Asks the user for input and strips whitespace.
    
    :param prompt_text: The prompt string to display
    :return: Sanitized string input
    """
    try:
        user_input = input(prompt_text)
        return user_input.strip()
    except (KeyboardInterrupt, EOFError):
        # Handle ctrl+c or standard input termination gracefully
        print("\nExiting program...")
        sys.exit(0)

def display_message(message, is_error=False):
    """
    Prints success or error messages to the console with highlighting.
    
    :param message: The message text to print
    :param is_error: Boolean flag to check if it's an error alert
    """
    if is_error:
        print(f"\n>>> [ERROR] {message}")
    else:
        print(f"\n>>> [SUCCESS] {message}")
