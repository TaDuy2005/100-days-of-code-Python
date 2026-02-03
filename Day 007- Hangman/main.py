import random

from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for _ in range(len(chosen_word)):
    placeholder += '_'
print(f"Word to guess: {placeholder}")

game_over = False
correct_letter = []


while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You already guessed {guess}")

    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)

        elif letter in correct_letter:
            display += letter
        else:
            display += '_'

    print(f"Word to guess: {display}")

    if guess not in correct_letter:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
