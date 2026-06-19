# DecodeLabs Task 3: Random Password Generator

A command-line enterprise password generator utility built using Python. It demonstrates intermediate backend concepts including Input-Process-Output (IPO) scaffolding, cryptographically secure randomness, performance-optimized string manipulation, and mathematical proof of security using Shannon Information Entropy.

## How It Works
1. **Input Phase:** The program requests a target password length and validates it against NIST SP 800-63-4 standards (recommending a minimum of 15 characters).
2. **Process Phase:** Character arrays are built using locale-independent constants (`string` module) and combined. A password is generated using `secrets.choice()` for secure randomness, and joined in $O(N)$ linear time complexity.
3. **Entropy Validation:** The utility calculates the Shannon Information Entropy in bits: $E = L \times \log_2(R)$.
4. **Output Phase:** A detailed security credential report is delivered to the console, showing the password, entropy metrics, and brute-force cracking resistance.

## Running the Application
Make sure you have Python 3 installed. Run the script in your terminal using:
```bash
python cli.py
```
