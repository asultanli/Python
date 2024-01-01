
import random

from Random_Words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo,stages
print(logo)
#Testing code
#print(f'the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guessed_letters = []
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You have already guessed that letter,try another one :)")
        if guess not in chosen_word:
            lives += 1
    guessed_letters += guess

    
    guessed_letters += guess
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("Guessed letter is not in word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.Good luck next try!")
            print("The word was:",chosen_word)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages[lives])