#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word_int = random.randint(0,2)
chosen_word = word_list[chosen_word_int]

chosen_word = chosen_word.lower()
chosen_word_list = list(chosen_word)
print(chosen_word)
print(chosen_word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("input a letter of your choice \n")
guess = guess.lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word_list:
  if letter == guess:
    print("letter exists in the word")

