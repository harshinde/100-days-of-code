#Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

#print range from 1 to 100
#check if the number is divisible by 3 using modulo operator
#check if the number is divisible by 5 using modulo operator
#if the number is divisible i.e, if the remainder is 0 then print either "fizz" or "buzz" depending on the divisibility factor
#if the number is not divisible then print the number


for number in range(1,100):
  if number % 3 == 0 and number % 5 == 0:
    print("fizzbuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("buzz")
  else:
    print(number)
