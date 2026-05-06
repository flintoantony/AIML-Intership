import random

# Word list
words = ["apple", "lion", "chair", "tree","house"]

# Random word selection
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()

# Maximum wrong attempts
attempts = 6

# Hangman stages
stages = [
"""
-----
|   |
|
|
|
|
=========
""",
"""
-----
|   |
O   |
|
|
|
=========
""",
"""
-----
|   |
O   |
|   |
|
|
=========
""",
"""
-----
|   |
O   |
/|  |
|
|
=========
""",
"""
-----
|   |
O   |
/|\ |
|
|
=========
""",
"""
-----
|   |
O   |
/|\ |
/   |
|
=========
""",
"""
-----
|   |
O   |
/|\ |
/ \ |
|
=========
"""
]

print("🎮 Welcome to Hangman!")

# Game loop
while attempts > 0:
    # Display current stage
    print(stages[6 - attempts])
    
    # Display word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(display_word))
    
    # Check win condition
    if set(display_word) == word_letters:
        print("🎉 You won! The word was:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.")
        continue

    # Repeated guess check
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Correct guess
    if guess in word_letters:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

# Game over condition
if attempts == 0:
    print(stages[6])
    print("💀 Game Over! The word was:", word)