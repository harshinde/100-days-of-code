import random

print ("--------------------------------")
print ("		Guess the number		")
print ("--------------------------------")
print ()

the_number = random.randint(0,100)

guess = -10


print ('the random number is :' + str(the_number))

name = input('what is your name:')


while guess != the_number:
	guess_text = input('Guess a number between 0 to 100 - ')
	guess = int(guess_text)

	if guess < the_number:
		print ('Sorry, {1} your guess {0} is lower than the actual number' .format(guess, name))
	elif guess > the_number:
		print ('Sorry, {1} your guess {0} is higher than the actual number' .format(guess, name))
	else:
		print ('you guessed it right!')

print ('game over')
