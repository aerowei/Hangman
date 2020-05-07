import random
import string as st 

# i is a contor variable
# letter list is a list containing all 27 lowercase letters
# tried_letters is a list that will contain all used letter
# error is a variable to check if a letter has been entered earlier
# I made difficulty like this so I can use it in the loop below

i = 0
letter_list = list(st.ascii_lowercase)
tried_letters = []
error = 0
difficulty = ''

# Ask the user for difficulty and check for correct input

while not difficulty.isalpha():
        difficulty = input('Please choose a difficulty: Easy, Medium or Hard: ').strip().lower()
        if not difficulty.isalpha():
                print('Please use only letters!')
        
# Open the file
# Create a list called words that will contain the words

file = open(r'wordlist.txt','r')
words = []
word = file.readline().strip().lower()

# Choose word and number of lives based on difficulty

while word:
        if word.isalpha():
                if difficulty == 'easy':
                        if len(word) <= 4:
                                words.append(word)
                                lives = 5
                elif difficulty == 'medium':
                        if len(word)> 4 and len(word) <= 6:
                                words.append(word)
                                lives = 4
                elif difficulty == 'hard':
                        if len(word)> 6 and len(word) <= 8:
                                words.append(word)
                                lives = 3
        word = file.readline().strip().lower()

# Use random to choose a random word from the list

ranword = random.choice(words)

# for i in range(len(ranword)):
#       hg.append('_')
# This is another method to add '_' to the list, but I used "for", for educational purposes

hg = ['_' for i in range(len(ranword))]
print('Good luck! You have chosen the {} difficulty and you have {} lives!'.format(difficulty,lives))

#   Input from user

def ask_letter():
    global error    
    c = input('\nEnter a letter: ').strip().lower()
    if c.isalpha():
            while len(c) > 1:
                    print('Error! Please enter just one letter!\n')
                    c = input('Please enter a letter: ').strip().lower()
            if c in letter_list:
                    tried_letters.append(c)
                    letter_list.pop(letter_list.index(c))
                    error = 0
            elif c not in letter_list:
                    error = 1
                    print('Error! Letter has been entered already. Please try other letter.')
                    print('You have tried the following letters:', end =' ')
                    print(*tried_letters)
    elif not c.isalpha():
            print('Plese enter a letter!')
            error = 1
            
    return c

# Creates a list with the positions of the chosen letter in the word

def get_letter_pos(letter):
    return [pos for (pos,char) in enumerate(ranword) if char == letter]

# Print
# I think I could've made this into a function as well, but eh - who cares.

print(*hg)
while lives > 0:
    if '_' not in hg:
        print("\nCongratulations! You're the winner!")
        break
    letter = ask_letter()
    if letter in ranword:
            if error == 0:
                    letter_pos = get_letter_pos(letter)
                    for i in range(len(letter_pos)):
                            hg[letter_pos[i]] = letter
    elif letter not in letter_list and letter.isalpha() and letter not in ranword:
            lives -= 1
            print('\nWrong! You have {} heart(s) left!'.format(lives))
    if lives == 0:
            print('\nGame over! The word was {}!'.format(ranword))
            break        
    if error == 0:
            print(*hg)    #print(*hg,sep=' ')  is also possible but *hg does the job (unpacking)  




