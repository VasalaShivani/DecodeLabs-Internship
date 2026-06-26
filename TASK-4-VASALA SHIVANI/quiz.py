import sys

def sanitize_input(user_input: str) -> str:
    """
    Applies the sanitization pipeline as specified in the DecodeLabs training manual:
    1. Whitespace Bouncer: Eliminates leading/trailing spaces, tabs, and newlines.
    2. Neutralizer: Converts all uppercase characters to lowercase for robust matching.
    """
    return user_input.strip().lower()

def evaluate_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Evaluates a user's answer against the correct reference answer.
    Ensures deterministic processing: identical inputs produce identical outputs.
    """
    return sanitize_input(user_answer) == sanitize_input(correct_answer)

def run_quiz():
    """
    Main execution sequence for the General Knowledge Quiz decision engine.
    """
    # Stylized welcome header matching DecodeLabs standard
    print("============================================================")
    print("         DECODELABS PYTHON INDUSTRIAL TRAINING KIT          ")
    print("             PROJECT 4: THE GENERAL KNOWLEDGE QUIZ          ")
    print("============================================================")
    print("   Transitioning from static to dynamic decision engines.   ")
    print("============================================================\n")
    
    print("Welcome to the team! Step into the role of a Python Developer at DecodeLabs.")
    print("This is your Optional Mastery Phase: The General Knowledge Quiz.\n")
    print("Control Flow, State Management, and Input Sanitization are our core focus.")
    print("Each question block follows the standard IPOS architecture.\n")
    print("Starting the quiz...\n" + "-" * 60)
    
    # State Management: Initialize the score vault to integer 0
    score = 0
    
    # Question pool list: {num, q, a}
    questions = [
        {
            "num": 1,
            "q": "What is the capital of France?",
            "a": "paris"
        },
        {
            "num": 2,
            "q": "Which planet is known as the Red Planet?",
            "a": "mars"
        },
        {
            "num": 3,
            "q": "What is the largest ocean on Earth?",
            "a": "pacific"
        }
    ]
    
    # Process Phase: Loop through the question blocks
    for item in questions:
        # Step 1: Ask & Capture (Input Phase)
        print(f"Question {item['num']}: {item['q']}")
        raw_input = input("Answer: ")
        
        # Step 2: Sanitize (Filter Phase)
        sanitized = sanitize_input(raw_input)
        
        # Step 3: Evaluate (Decision Phase)
        is_correct = evaluate_answer(sanitized, item['a'])
        
        # Step 4: Execute (Side-Effects / State Update Phase)
        if is_correct:
            score += 1
            print("\n[+] Correct! +1 point added to the Score Vault.")
        else:
            # Score state is intentionally maintained, not reset in failure path
            print(f"\n[-] Incorrect. The correct answer is '{item['a'].capitalize()}'. Score state maintained.")
            
        print("-" * 60)
    
    # Output Phase: Delivering results using dynamic f-string with precision formatting
    print("\n============================================================")
    print("                      QUIZ COMPLETED                        ")
    print("============================================================")
    # Using syntax like f'{score : >2}' right-aligns the score within a two-character field
    print(f"Final Score in Vault: {score : >2} /  3")
    print("============================================================\n")
    print("Thank you for completing Project 4! Keep coding, keep building!")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\n[-] Session interrupted. Quiz closed.")
        sys.exit(0)
