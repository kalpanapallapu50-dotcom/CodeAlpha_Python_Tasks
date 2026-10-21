import random

print("=== CodeAlpha - Hangman Game ===")
print("By: Kalpana Sravanthi | Viswam College")

words = ['python', 'college', 'internship', 'viswam', 'kalpana', 'codealpha']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
used = []

print("Word: " + " ".join(guessed))

while attempts > 0 and '_' in guessed:
    letter = input("Enter a letter: ").lower()
    
    if letter in used:
        print("Already used!")
        continue
    used.append(letter)
    
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct! " + " ".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left")
        print(" ".join(guessed))

if '_' not in guessed:
    print(f"You Won! Word is {word}")
else:
    print(f"You Lost! Word was {word}")
