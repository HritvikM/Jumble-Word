import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ImageAddress = 'C:/Users/hritv/PycharmProjects/JumbleWord/Youwon.png'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)

def get_jumble_word(word):
    l = list(word)
    random.shuffle(l)
    return ''.join(l)

with open("Jumbletxt.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))


def game():
    x = 0
    y = 0
    for i in range(5):
        a=(random.choice(words))
        print("\nThe jumble is:", get_jumble_word(a))
        guess=input("Enter your guess:")
        if guess == a:
            x=x+1
            print("That's it!  You guessed it!\n")
        else:
            y=y+1
            print("You failed...")
    print("Your score is: " + str(x))
    print("Computer score is: " + str(y))
    if(x>y):
        print("You Won")
        plt.imshow(ImageNumpyFormat)
        plt.draw()
        plt.pause(1)  # pause how many seconds
        plt.close()
    else:
        print("You Lose")
    play = input("Do you want to play again? (yes or no)")
    if (play == "yes"):
        game()

print("""RULES OF THE GAME:
1. 5 Round will be played and if you get 3 or more points , You won otherwise  Computer Wins.
2.  Use Capital Letters.
3.  In each round,  You will be given one Jumbled word and you have to answer the original unjumbled word.
4.  If you answer is correct you get  1 point.
""")
play = input("Do you want to play? (yes or no)\n")
if (play == "yes"):
    game()

print("Thanks for playing.")

input("\nPress the enter key to exit.")
