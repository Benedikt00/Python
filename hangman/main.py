#clear screen
import os


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



word = 'secret'

print(HANGMANPICS[0])
print('Welcome to Hangman!')
print('I am thinking of a word that is', len(word), 'letters long.')

guesses = 0
wrong_letters_guessed = 0
right_letters_guessed = 0
gamerun = True

right_letters = []

while gamerun:
    os.system('CLS')
    if right_letters_guessed == len(word):
        print('You win!')
        gamerun = False
    print(HANGMANPICS[wrong_letters_guessed])
    for letter in word:
        if letter in right_letters:
            print(letter, end='')
        else:
            print('_', end='')
    print("\n")


    guess = input('Guess a letter: ')
    if guess in word:
        if guess in right_letters:
            print('You already guessed that letter!')

        else:
            print('Good guess!')
            right_letters.append(guess)
            right_letters_guessed += 1

    else:
        print('Wrong!')
        guesses += 1
        wrong_letters_guessed += 1






