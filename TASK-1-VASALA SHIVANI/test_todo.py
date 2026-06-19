"""
test_todo.py - Unit Tests

This file is responsible for testing the logic of our TaskManager (Model) class.
Writing automated tests is a standard professional engineering practice to verify
that code modifications do not introduce regression errors.

Concepts explained for Interns:
1. Setup and Teardown: Before each test runs, setUp() initializes a clean testing 
   state. After each test runs, tearDown() deletes the temporary test file. This 
   prevents test cases from polluting or interfering with one another.
2. Assertions: We use self.assertEqual, self.assertTrue, self.assertFalse to verify 
   if the code behaves as expected.
"""

import unittest
import os
from model import TaskManager

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        """
        Runs before every individual test. Sets up a separate temporary JSON file
        so tests don't affect our production database tasks.json.
        """
        self.test_file = "test_tasks_temp.json"
        # Create a new, clean TaskManager instance pointing to the temp file
        self.manager = TaskManager(filepath=self.test_file)

    def tearDown(self):
        """
        Runs after every individual test. Cleans up and deletes the temporary file.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        """
        Tests if adding a task successfully creates a dictionary item 
        with correct default values and sequential IDs.
        """
        # Add a task
        task = self.manager.add_task("Learn Python lists")
        
        # Verify the list size increased
        self.assertEqual(len(self.manager.tasks), 1)
        
        # Verify schema
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["task"], "Learn Python lists")
        self.assertEqual(task["completed"], False)

        # Add a second task and verify auto-increment of ID
        task2 = self.manager.add_task("Understand Decoupled Architecture")
        self.assertEqual(task2["id"], 2)
        self.assertEqual(len(self.manager.tasks), 2)

    def test_toggle_task_completion(self):
        """
        Tests if toggling status switches completion correctly.
        """
        task = self.manager.add_task("Test toggling")
        self.assertFalse(task["completed"])  # Default is False
        
        # Toggle to True
        success = self.manager.toggle_task_completion(task["id"])
        self.assertTrue(success)
        self.assertTrue(self.manager.tasks[0]["completed"])

        # Toggle back to False
        success = self.manager.toggle_task_completion(task["id"])
        self.assertTrue(success)
        self.assertFalse(self.manager.tasks[0]["completed"])

    def test_delete_task(self):
        """
        Tests if a task is correctly deleted and removed from the list.
        """
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        
        # Delete task 1
        success = self.manager.delete_task(task1["id"])
        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["id"], task2["id"])  # Only task 2 remains

        # Attempt to delete a non-existent task
        success_invalid = self.manager.delete_task(999)
        self.assertFalse(success_invalid)

    def test_persistence(self):
        """
        Tests if saving and re-loading from JSON disk persistence works.
        """
        self.manager.add_task("Persistent Task 1")
        self.manager.add_task("Persistent Task 2")
        
        # Create a new, separate manager instance pointing to the same file.
        # This simulates stopping the app and starting it again.
        new_manager = TaskManager(filepath=self.test_file)
        
        # Verify tasks were loaded back from disk
        self.assertEqual(len(new_manager.tasks), 2)
        self.assertEqual(new_manager.tasks[0]["task"], "Persistent Task 1")
        self.assertEqual(new_manager.tasks[1]["task"], "Persistent Task 2")

if __name__ == "__main__":
    unittest.main()
