# DecodeLabs Task 2: Expense Tracker

A command-line expense accumulator application built using Python. It demonstrates foundational backend concepts including state preservation, input validation, defensive programming, and infinite control loops.

## How It Works
1. **Initialize State:** The ledger starts at `$0.00`.
2. **Interactive Loop:** The script continuously prompts you to log an expense.
3. **Data Protection:** Invalid values (e.g., text, empty inputs) are caught defensively, preventing application crashes.
4. **Sentinel Check:** Typing `quit` ends the loop and outputs the audited final total.

## Running the Application
Make sure you have Python 3 installed. Run the script in your terminal using:
```bash
python expense_tracker.py
```
