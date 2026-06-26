# DecodeLabs Task 4: The General Knowledge Quiz

A command-line general knowledge quiz game utility built using Python. It demonstrates foundational backend concepts including state preservation (Score Accumulator), input sanitization, deterministic evaluation, and conditional branching control flow.

## How It Works
1. **Input Phase:** The program prompts the user with 3 general knowledge questions sequentially and captures the raw keystrokes using the `input()` function.
2. **Sanitization Phase:** The raw input is processed through a two-step filter pipeline:
   - **Whitespace Bouncer:** `.strip()` eliminates leading/trailing spaces, tabs, and newlines.
   - **Neutralizer:** `.lower()` normalizes character cases to prevent encoding mismatches.
3. **Process Phase:** The sanitized input is compared against the reference answer using equality (`==`) logic gates.
4. **State Management:** An integer accumulator variable (`score`) acts as a "Score Vault." It starts at `0`.
   - If the answer is correct: The score increments by `1`.
   - If the answer is incorrect: The score is maintained (not reset) to preserve data integrity.
5. **Output Phase:** A formatted final report is rendered to the console, utilizing precision f-string right-alignment (`f'{score : >2}'`) to keep terminal output clean and flush.

## Running the Application
Make sure you have Python 3 installed. Run the script in your terminal using:
```bash
python quiz.py
```

## Testing the Code
To verify that the sanitization pipeline and logic gates work perfectly, automated unit tests are provided. Run them in your terminal using:
```bash
python test_quiz.py
```
If everything is working correctly, you will see:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
