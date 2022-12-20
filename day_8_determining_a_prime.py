#Write your code below this line 👇
def prime_checker(number):
    isPrime = True
    if number<1 or number%1>0:
        isPrime = False
    for i in (2, number // 2):
        if number % i == 0:
            isPrime = False
            print("not a prime number")
        else:
            print("It's a prime number")  




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
