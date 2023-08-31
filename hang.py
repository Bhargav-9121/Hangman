import random

class HangMan:
    def __init__(self, words):
        self.words=words        

    def play(self, w, count=0):
        dashes = ["_"] * len(w)

        status="alive"

        while True:
            for i in dashes:
                print(i, end=" ")

            if ("_" not in dashes):
                print("\n\nCongratulations! Your word wizardry has brought your tiny stick buddy back from the brink of a very awkward vertical hangout.\n")
                print(" \O/ \n"
                      "  | \n"
                      " / \ \n"
                )
                break

            g = input("Take a guess: ")
            g=g.lower()
            print()
            
            if ((g in w) and (count<6)):
                print("\nCorrect")
                for i in range(len(w)):
                    if (w[i]==g):
                        dashes[i]=g
                    if (i==len(w)-1):
                        break
            elif count>=6:
                print("Stick Figure Dead, you lost\n")
                break
            else:
                count+=1
                status = self.forWrong(count)
            
            if (status == "dead"):
                break

    def forWrong(self, count):
        print("\nWrong")
        if count == 1:
            print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("Wrong guess. 5 guesses remaining\n")

        elif count == 2:
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("4 guesses remaining\n")

        elif count == 3:
            print("   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
            print("3 guesses remaining\n")

        elif count == 4:
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print("2 guesses remaining\n")

        elif count == 5:
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |        \n"
                "__|__\n")
            print("One more wrong guess and he's dead\n")

        elif count==6:
            print("   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
            print("Ahhhhh, He's dead...\n")
            print("Thanks for playing, better luck next time\n\n")
            return "dead"
    

print("Welcome to the ultimate showdown of word wrangling - the one and only legendary Hangman Extravaganza!")
print("It's a battle between your vocabulary and the impending doom of a doodled stick figure.")
print("You get 5 chances to save your stick friend.")
print("Make sure you save our poor stick figure friend before he rethinks his life decisions.\n")
print("Please select a category: ")
print("1. Fruits")
print("2. Animals")
print("3. Countries")
print("4. Random\n")

words = {
    1: ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "pear", "quince", "raspberry", "strawberry", "watermelon"],
    2: ["cat", "dog", "elephant", "giraffe", "hippopotamus", "kangaroo", "lion", "monkey", "penguin", "tiger", "zebra", "koala", "panda", "rhinoceros", "gazelle", "crocodile", "polar bear", "ostrich"],
    3: ["canada", "brazil", "france", "japan", "australia", "germany", "india", "italy", "mexico", "egypt", "china", "southkorea", "russia", "spain", "southafrica", "argentina", "turkey", "greece", "thailand", "netherlands", "sweden", "chile", "vietnam", "ireland", "poland", "malaysia", "peru", "denmark", "norway", "switzerland"],
    4: ["beach", "mountain", "city", "forest", "desert", "island", "countryside", "cave", "jungle", "lake", "valley", "village", "ocean", "canyon", "castle", "waterfall", "volcano", "computer", "keyboard", "guitar", "television", "umbrella", "backpack", "sunflower", "moonlight", "puzzle", "candle", "rainbow", "butterfly", "jigsaw", "carousel", "fireworks", "hamburger", "pizza", "balloon", "parrot", "sunset"]
}

hm = HangMan(words)

#selection of category
while True:
    cat=input("Enter the category number: ")
    if (cat.isdigit()):
        cat=int(cat)
        if (1<=cat<=4):
            break
        else:
            print("Please enter a choice between 1 and 4.\n")
    else:
        print("Please enter a category number")



if (cat==4):
    print("Ah, I see you've bravely ventured into the treacherous realm of the 'Random' category!")
    print("Good luck with saving your stick friend tho.\n")
    print("Let's get started\n")
    count=0
    w = random.choice(words[4])
    hm.play(w)

elif (cat==3):
    print("Brace yourself for a global wordy adventure! You've chosen the 'Countries' category.")
    print("Get ready to jet-set through alphabetic landscapes and conquer the geography of giggles!")
    print("Let's get started\n")
    count=0
    w = random.choice(words[3])
    hm.play(w)

elif (cat==2):
    print("Welcome to the wild side of word play!")
    print("By selecting the 'Animals' category, you've embarked on a linguistic safari where every correct guess leads you deeper into the kingdom of letters.")
    print("Let's get started\n")
    count=0
    w = random.choice(words[2])
    hm.play(w)

else:
    print("Get ready to taste victory in the 'Fruits' category!")
    print("Your choice has set you on a fruity quest where every correct guess is as sweet as a ripe berry.")
    print("Peel away the mystery letters and savor the satisfaction of uncovering the juiciest words!")
    count=0
    w = random.choice(words[1])
    hm.play(w)






        
           






