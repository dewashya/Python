#dice
import random
  
  
x = "y"
   
while x == "y":
      
    # Gnenerates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    no = random.randint(1,6)
      
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
          
    x=input("press y to roll again and n to exit:")
    print("\n")

#S.G.
    # Importing random module
import random
  
# Defining list of phrases which will help to build a story
  
Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
             ' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']
  
# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))



#GUESS
import random
# library that we use in order to choose
# on random words from a list of words
name = input("What is your name? ")
# Here the user is asked to enter the name first
print("Good Luck ! ", name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
# Function will choose one random
# word from this list of words
word = random.choice(words)
print("Guess the characters")
guesses = ''
# any number of turns can be used here
turns = 12
while turns > 0:
    # counts the number of times a user fails
    failed = 0
    # all characters from the input
    # word taking one at a time.
    for char in word:
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)
        else:
            print("_")
            # for every failure 1 will be
            # incremented in failure
            failed += 1
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
        # this print the correct word
        print("The word is: ", word)
        break
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")
    # every input character will be stored in guesses
    guesses += guess
    # check input with the character in word
    if guess not in word:
        turns -= 1
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")

# %%
