#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#pick n letters in random from the list of letters, symbols and numbers
#picking random elements from a list - for the number of elements requested, create a random int range
#find the length of each list to iterate

letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)

#creating a list of random indexes


rand_letters =[]
rand_numbers =[]
rand_symbols = []

for x in range(nr_letters):
  if len(rand_letters) < nr_letters:
    rand_letters_index = random.randint(0, letters_length-1)
    rand_letters.append(letters[rand_letters_index])
    rand_word = "".join(rand_letters)

for y in range(nr_numbers):
  if len(rand_numbers) < nr_numbers:
    rand_numbers_index = random.randint(0, numbers_length-1)
    rand_numbers.append(numbers[rand_numbers_index])
    rand_number = "".join(rand_numbers)
    
for z in range(nr_symbols):
  if len(rand_symbols) < nr_symbols:
    rand_symbols_index = random.randint(0, symbols_length-1)
    rand_symbols.append(symbols[rand_symbols_index])
    rand_symbol = "".join(rand_symbols)

print(rand_word)
print(rand_number)
print(rand_symbol)
random_password = rand_word+rand_symbol+rand_number
print(random_password)






#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
rand_password_scramble =[]
random_password = list(random_password)
print(random_password)
print(len(random_password))
#take the concatenated password string and scramble it to create a randomized password
for z in range(0,len(random_password)):
  rand_password_index = random.randint(0, (len(random_password)-1))
  print(rand_password_index)
  rand_password_scramble.append(random_password[rand_password_index])
  rand_pass_scramble = "".join(rand_password_scramble)

print(rand_pass_scramble)
