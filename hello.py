import random

def get_random_quote():
    """Return a random motivational quote."""
    quotes = [
        "Keep going, you’re doing great!",
        "Every day is a new opportunity to grow.",
        "Believe in yourself and all that you are.",
        "Success is the sum of small efforts repeated day in and day out."
    ]
    return random.choice(quotes)

def main():
    """Print Hello, World! and a random motivational quote."""
    print("Hello, World!")
    print(get_random_quote())

if __name__ == "__main__":
    main()