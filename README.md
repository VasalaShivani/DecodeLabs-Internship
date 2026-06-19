# CLI To-Do List Application

A simple, lightweight, and easy-to-use Command-Line (CLI) To-Do List application. It helps you manage your daily tasks right from your terminal. 

Your tasks are automatically saved to a file called `tasks.json` on your computer, meaning they won't be lost even if you close the program or turn off your computer!

---

## ⚙️ How it Works

The application is split into three clean Python files to make the code organized and easy to read:
* **`model.py`**: The "storage closet" where your tasks are saved, loaded, and edited.
* **`view.py`**: The "screen painter" that formats how everything looks (menus, tables, checkmarks) and asks you for keyboard input.
* **`main.py`**: The "brain" that runs the program loop and connects the screen output with the database.

---

## 🚀 How to Run the Application

You do not need to install any external packages. The project runs on standard Python.

1. Open your terminal or Command Prompt.
2. Navigate to the folder where you placed the project:
   ```bash
    
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## 💻 What the Output Looks Like

### The Welcome Banner and Options Menu
When you first start the application, you will see a stylized welcome header and a numbered menu:
```text
============================================================
         DECODELABS PYTHON INDUSTRIAL TRAINING KIT
                 PROJECT 1: THE TO-DO LIST
============================================================
   Build a solid backend foundation with structured logic.
============================================================


--- OPTIONS ---
1. View Tasks
2. Add Task
3. Toggle Task Completion
4. Delete Task
5. Exit Application
---------------
Enter choice (1-5): 
```

### Viewing Tasks
When you choose Option 1, your tasks will print in a clean table showing their order, their database ID, completion status (with a checkmark `[✓]`), and task name:
```text
============================================================
No.  | DB ID | Status   | Task Description
------------------------------------------------------------
1    | 1     | [✓]      | Buy groceries
2    | 2     | [ ]      | Practice Python loops
3    | 3     | [ ]      | Write unit tests
============================================================
```

---

## 🛠️ Options Guide

* **1. View Tasks**: Shows all your saved tasks in a table. If you don't have any tasks, it will let you know the list is empty.
* **2. Add Task**: Prompts you to type a description and creates a new task.
* **3. Toggle Task Completion**: Lets you mark a task as completed `[✓]` or switch it back to pending `[ ]` by typing its unique **DB ID**.
* **4. Delete Task**: Permanently removes a task from your database by typing its unique **DB ID**.
* **5. Exit Application**: Safely saves all changes and closes the program.

---

## 🧪 Testing the Code

If you want to verify that the core logic works perfectly, we have written automated tests. To run them, type this command in your terminal:
```bash
python test_todo.py
```
If everything is working correctly, you will see:
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.027s

OK
```
