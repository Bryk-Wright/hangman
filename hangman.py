import random
import man
import words

display = []
LIVES = 0
prev_guesses = []

print(r"""
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/""")

chosen_word = random.choice(words.list)
for i in chosen_word:
    display.append("_")

while LIVES < 6:
    FOUND = False
    WIN = False
    guess = input("Guess a letter! ").lower()

    for index, letter in enumerate(chosen_word):
        if guess == letter and not guess in prev_guesses:
            display[index] = guess
            FOUND = True

    if not FOUND:
        LIVES += 1

    CAT = "".join(display)
    if CAT == chosen_word:
        WIN = True
    else:
        WIN = False

    if WIN is True:
        print(f"You won! The word was {chosen_word}")
        quit()

    print("Previous guesses")
    print(*prev_guesses)
    prev_guesses.append(guess)
    print(man.progress[LIVES])
    print(*display)

    if LIVES == 6:
        print("You lose!")
        print(f"The word was: {chosen_word}")
