def main():
    print("====================================")
    print("    DECODELABS EXPENSE TRACKER      ")
    print("====================================")
    print("Enter your expenses one by one.")
    print("Type 'quit' when you are done to see the final ledger.\n")

    # State initialized outside the loop to prevent memory reset
    total_spent = 0.0

    while True:
        user_input = input("Enter expense amount: ").strip()

        # Sentinel check for graceful shutdown
        if user_input.lower() == 'quit':
            print("\nFinalizing ledger computations...")
            break

        # Defensive coding block to reject invalid inputs without crashing
        try:
            expense = float(user_input)
            total_spent += expense
            print(f"Successfully added: ${expense:.2f} | Running Total: ${total_spent:.2f}\n")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value or type 'quit'.\n")

    # Decoupled presentation phase
    print("====================================")
    print(f"FINAL TOTAL: ${total_spent:.2f}")
    print("====================================")


if __name__ == "__main__":
    main()
