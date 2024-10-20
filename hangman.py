import random
from hangman_words import word_list
from hangman_art import stages



lives = 6


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************<???>{lives}LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print("you already chosen this word")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"you have guessed '{guess}',that is not correct you lose a life")

        if lives == 0:
            game_over = True;
            print(f"The correct word is ={chosen_word}")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])
