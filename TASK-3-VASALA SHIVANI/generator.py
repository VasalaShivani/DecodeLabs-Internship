import math
import secrets
import string

def calculate_entropy(length: int, pool_size: int) -> float:
    """
    Computes Shannon Information Entropy of a password.
    Formula: E = L * log2(R)
    """
    if pool_size <= 0 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)

def get_security_strength(entropy: float) -> str:
    """
    Categorizes the password strength based on its entropy in bits.
    Standard NIST / industry classifications:
      - < 40 bits: Very Weak (susceptible to immediate offline brute-force)
      - 40 - 59 bits: Weak (low security, easily crackable)
      - 60 - 79 bits: Moderate (reasonable for low-risk online accounts)
      - 80 - 127 bits: Strong (recommended for standard enterprise accounts)
      - >= 128 bits: Very Strong / Passphrase-level (virtually uncrackable)
    """
    if entropy < 40:
        return "Very Weak (Instantly crackable)"
    elif entropy < 60:
        return "Weak (Crackable in days/weeks)"
    elif entropy < 80:
        return "Moderate (Secure against basic online attacks)"
    elif entropy < 128:
        return "Strong (Recommended for enterprise credentials)"
    else:
        return "Very Strong (Resistant to state-level brute forcing / Passphrase equivalent)"

def generate_secure_password(
    length: int,
    use_letters: bool = True,
    use_digits: bool = True,
    use_punctuation: bool = True
) -> tuple[str, int]:
    """
    Generates a cryptographically secure random password of specified length.
    Ensures that at least one character from each selected pool is present.
    Usessecrets.choice for selection and secrets.SystemRandom for shuffling.
    
    Returns:
      tuple: (password_string, character_pool_size)
    """
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    pools = []
    if use_letters:
        pools.append(string.ascii_letters)
    if use_digits:
        pools.append(string.digits)
    if use_punctuation:
        pools.append(string.punctuation)
        
    if not pools:
        raise ValueError("At least one character type (letters, digits, or punctuation) must be selected.")
    
    # Combined character pool for filling the rest of the password
    combined_pool = "".join(pools)
    pool_size = len(combined_pool)
    
    # In enterprise systems, we must ensure we don't request a length shorter than the mandatory
    # minimum required to contain at least one character of each checked pool type.
    if length < len(pools):
        raise ValueError(
            f"Requested length ({length}) is too short to guarantee inclusion of all "
            f"selected character types ({len(pools)} selected)."
        )
    
    # Step 1: Guarantee inclusion of at least one character from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]
    
    # Step 2: Fill the remaining slots using the combined character pool
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(combined_pool))
        
    # Step 3: Shuffle the characters to eliminate positional predictability
    # secrets.SystemRandom() provides an OS-level cryptographically secure random source for shuffling.
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_chars)
    
    # Step 4: Perform O(N) memory allocation string conversion instead of concatenation loop
    return "".join(password_chars), pool_size
