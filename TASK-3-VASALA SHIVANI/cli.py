import sys
from generator import generate_secure_password, calculate_entropy, get_security_strength

def get_boolean_input(prompt: str, default: bool = True) -> bool:
    """Prompts user for a yes/no question, returning a boolean value."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        val = input(prompt + suffix).strip().lower()
        if not val:
            return default
        if val in ('y', 'yes'):
            return True
        if val in ('n', 'no'):
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def run_cli():
    print("=" * 60)
    print("         DECODELABS ENTERPRISE PASSWORD GENERATOR         ")
    print("           (NIST SP 800-63-4 Compliant Engine)           ")
    print("=" * 60)
    print("This utility generates cryptographically secure, high-entropy")
    print("credentials following the Input-Process-Output design scaffold.")
    print("-" * 60)
    
    while True:
        # 1. INPUT PHASE (with rigorous data validation)
        try:
            length_input = input("Enter target password length [Default: 16]: ").strip()
            if not length_input:
                length = 16
            else:
                length = int(length_input)
                
            if length <= 0:
                print("[-] Error: Password length must be a positive integer.")
                print("-" * 60)
                continue
        except ValueError:
            print("[-] Error: Please enter a valid integer (e.g., 16).")
            print("-" * 60)
            continue
        
        # NIST Guidelines Warning check
        if length < 15:
            print("\n[!] SECURITY WARNING: NIST SP 800-63-4 guidelines recommend")
            print("    a minimum of 15 characters for secure credentials.")
            proceed = get_boolean_input("    Do you want to override and proceed anyway?", default=False)
            if not proceed:
                print("[-] Generation aborted. Please specify a larger length.")
                print("-" * 60)
                continue
        elif length > 64:
            print("\n[!] NOTE: While supported, lengths above 64 characters may")
            print("    exceed maximum buffer sizes on some legacy backend systems.")
            proceed = get_boolean_input("    Do you want to proceed with this length?", default=True)
            if not proceed:
                print("[-] Generation aborted.")
                print("-" * 60)
                continue

        # Character options prompt
        use_letters = get_boolean_input("Include letters (A-Z, a-z)?", default=True)
        use_digits = get_boolean_input("Include numeric digits (0-9)?", default=True)
        use_symbols = get_boolean_input("Include special symbols/punctuation?", default=True)
        
        if not (use_letters or use_digits or use_symbols):
            print("\n[-] Error: You must select at least one character type.")
            print("-" * 60)
            continue
        
        # 2. PROCESS PHASE (invoking our core transformation engine)
        try:
            password, pool_size = generate_secure_password(
                length=length,
                use_letters=use_letters,
                use_digits=use_digits,
                use_punctuation=use_symbols
            )
        except ValueError as ve:
            print(f"\n[-] Error: {ve}")
            print("-" * 60)
            continue
        
        # Compute Shannon Entropy
        entropy = calculate_entropy(length, pool_size)
        strength = get_security_strength(entropy)
        
        # 3. OUTPUT PHASE (delivering high-integrity credential report)
        print("\n" + "=" * 60)
        print("                 GENERATED CREDENTIAL REPORT                 ")
        print("=" * 60)
        print(f"Generated Password :  {password}")
        print("-" * 60)
        print(f"Password Length (L) :  {length} characters")
        print(f"Character Pool (R)  :  {pool_size} unique symbols")
        print(f"Shannon Entropy (E) :  {entropy:.2f} bits")
        print(f"Strength Rating     :  {strength}")
        print("-" * 60)
        
        # Contextual brute-force metrics
        print("Approximate Brute-Force Feasibility (GPU cluster at 10^10 hashes/sec):")
        if entropy < 40:
            print("  [!] Immediate danger: Can be cracked in milliseconds.")
        elif entropy < 60:
            print("  [!] Low security: Can be cracked within a few hours to days.")
        elif entropy < 80:
            print("  [*] Moderate security: Safe for online web portal logins.")
        elif entropy < 100:
            print("  [+] High security: Secure against standard offline GPU brute-forcing.")
        else:
            print("  [++] Enterprise-grade: Secure for millions of years.")
        print("=" * 60 + "\n")
        
        if not get_boolean_input("Would you like to generate another password?", default=False):
            print("\nThank you for using the DecodeLabs Security Suite. Stay secure!")
            break
        print("-" * 60)

if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n\n[-] Session interrupted. Exiting Security Suite.")
        sys.exit(0)
