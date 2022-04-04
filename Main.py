import random

running = True
print("Welcome to Hangman!!")
words = [
    "Hello", 
    "World", 
    "Sandwich"
]

def build_placeholder(word, correct_guesses):
    placeholder = ""
    for i in range(len(word)):
        for letter in correct_guesses.keys():
            if i in correct_guesses[letter]:
                placeholder += letter
            else:
                placeholder += "_"

    return placeholder

while running:
    print("I'm thinking of a word...")
    random_index = random.randint(0, len(words)-1)
    computer_word = words[random_index]
    guesses = set()
    correct_guesses = {}
    tries = 0
    placeholder = build_placeholder(computer_word, correct_guesses)

    guessed_correctly = placeholder == computer_word
    if not guessed_correctly:
        tries += 1
        print("Please guess a letter or solve.")
        user_input = input("-->")
        is_solving = len(user_input) > 1
        if is_solving:
            if user_input == computer_word:
                guessed_correctly = True
            else:
                print("Incorrect")