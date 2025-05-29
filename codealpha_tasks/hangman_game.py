import random

#lists of words to choose from
word_list=["python","hangman","developer","internship","project","keyboard","laptop"]

# randomly choose a word
chosen_word=random.choice(word_list)
word_length=len(chosen_word)

# game sate variable
display=['_']*word_length
guessed_letters=[]
lives=6 #number of allowed wrong attempts

print("Welcome to Hangman!")
print("Guess the word,one at a time.")
print("you have",lives,"lives.good luck!\n")

# Main game loop
while lives>0 and '_'in display:
    print("word:"+"".join(display))
    print("guessed letters:",",".join(guessed_letters))
    guess=input("enter a letter:").lower()

    #input validation
    if not guess.isalpha()or len(guess)!=1:
        print(" please enetr a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("you already guessed that letter.try another one.")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
             print("correct guess!\n") 
    else:
        lives -=1
        print(f"wrong guess!lives remaning: {lives}\n")

# game and messages
if '_'not in display:
    print("congratulations! you guessed the word:",chosen_word)
else:
    print("Game over! The Word was:",chosen_word)             
