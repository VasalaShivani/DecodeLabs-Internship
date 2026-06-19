"""
model.py - The Data Model (Data Logic Layer)

This file is responsible for managing the application's data. 
In backend engineering, we decouple (separate) how data is stored and manipulated 
from how it is displayed to the user.

Concepts explained for Interns:
1. In-Memory Database: We represent our database table as a Python List.
   Each element in the list is a Dictionary, which represents a row in a table:
   Table Structure (list of dicts):
   [
       {"id": 1, "task": "Buy milk", "completed": False},
       {"id": 2, "task": "Learn Python", "completed": True}
   ]
2. Primary Keys: The "id" field acts as a primary key to uniquely identify each row.
3. Persistence: RAM is volatile (erased when the script stops). We serialize our 
   in-memory list to a JSON file on disk so the data persists.
"""

import json
import os

class TaskManager:
    """
    Manages the tasks list: adding, toggling status, deleting, and 
    handling JSON save/load persistence.
    """
    
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = []  # Our in-memory list of dictionaries
        self.load_tasks()  # Automatically load saved tasks on startup

    def load_tasks(self):
        """
        Loads tasks from a JSON file.
        If the file doesn't exist, it starts with an empty list.
        """
        # If the file does not exist, we just start with an empty list of tasks
        if not os.path.exists(self.filepath):
            self.tasks = []
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                # json.load reads the JSON string from disk and parses it back into a Python list of dicts
                self.tasks = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            # Handle corrupted files or reading errors gracefully
            print(f"[Warning] Failed to load data from {self.filepath}: {e}")
            print("Starting with an empty task list.")
            self.tasks = []

    def save_tasks(self):
        """
        Saves (serializes) the in-memory tasks list to the JSON file on disk.
        """
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                # json.dump converts the Python list of dicts to a JSON string and writes it to disk
                # indent=4 makes the JSON file human-readable
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"[Error] Failed to save tasks to disk: {e}")

    def add_task(self, task_text):
        """
        Creates a new task dictionary and appends it to the tasks list.
        Auto-generates a unique sequential ID.
        
        :param task_text: The description of the task (string)
        :return: The newly created task dictionary
        """
        # Check if we have any tasks to determine the next ID
        if len(self.tasks) > 0:
            # Find the maximum ID currently used and add 1
            next_id = max(task["id"] for task in self.tasks) + 1
        else:
            next_id = 1

        # Represent the task as a Python dictionary (like a database row)
        new_task = {
            "id": next_id,
            "task": task_text,
            "completed": False
        }

        # Appending to a Python list is O(1) in time complexity because it uses dynamic arrays
        self.tasks.append(new_task)
        
        # Persist the changes immediately to disk
        self.save_tasks()
        
        return new_task

    def get_tasks(self):
        """
        Returns the current in-memory list of tasks.
        """
        return self.tasks

    def delete_task(self, task_id):
        """
        Removes a task from the list using its ID.
        
        :param task_id: The ID of the task to delete (int)
        :return: True if the task was found and deleted, False otherwise
        """
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                # Remove the task at the found index
                self.tasks.pop(index)
                self.save_tasks()  # Persist changes to disk
                return True
        return False

    def toggle_task_completion(self, task_id):
        """
        Toggles the completion status of a task between True and False.
        
        :param task_id: The ID of the task to toggle (int)
        :return: True if the task was found and toggled, False otherwise
        """
        for task in self.tasks:
            if task["id"] == task_id:
                # Toggle the boolean state
                task["completed"] = not task["completed"]
                self.save_tasks()  # Persist changes to disk
                return True
        return False
