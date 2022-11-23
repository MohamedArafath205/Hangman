from word_list import word_list
import random

word = random.choice(word_list)



# hello 

def Structure(life):
    stages =[
                # platfrom, pole, horizontal bar, rope, head, torso, both arms and both legs
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar, rope, head, torso, both arms and one leg
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar, rope, head, torso, and both arms
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar, rope, head, torso, and one arm
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar, rope, head and torso
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar, rope and head
    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole, horizontal bar and rope
    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom, pole and horizontal bar
                """
                   ________
                   |
                   |
                   |
                   |
                   |
            |----------------|
            |                |
            |----------------|
                """,
                # platfrom and pole
                """
                   |
                   |
                   |
                   |
                   |
            |----------------|
            |                |
            |----------------|
                """,
                # intial stage only with platform
                """
            |----------------|
            |                |
            |----------------|
                """
                # before the setup
                """
                
                """]
    return stages[life]

def game():
    life = 0
    difficulty = int(input("1. Easy (10 lives)\n2. Medium (6 lives)\n3. Hard (4 lives)\n Enter difficulty: "))
    if difficulty == 1:
        life = 10
    elif difficulty == 2:
        life = 6
    elif difficulty == 3:
        life = 4
    else :
        print("Enter correct choice")
    letters_guessed = ""
    while life > 0:
        guess = input("\nEnter a letter : ")
        
        if guess in word:
            print("You guessed the correct letter", Structure(life) )
        else :
            life -= 1
            print("Wrong! guess!", Structure(life) )
        
        letters_guessed += guess
        wrong_letter = 0
        
        for letter in word:
            if letter in letters_guessed:
                print(letter, end="")
            else:
                print("_", end="")
                wrong_letter += 1
        
        if wrong_letter == 0:
            print("\nCongratulations! You have won the game, The letter was ", word)
            break
        
    else:
        print("\nSorry!, You lost all of your life\nThe word was", word)
        
print("\n\n\n\n")
line = "-------------------------"
text = "HANGMAN"
x = text.center(200)
y = line.center(200)
print(y)
print(x)
print(y)

while (True):
    play_game = input("Do you want the play the game (y/n) : ").upper()
    if (play_game == "Y"):
        game()
    else:
        print("Thanks!, For playing the game.")
        break