#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total_bill = input("What was the total bill?")
tip_percent = input("How much tip would you like to give? 10, 12, or 15?")
split_ppl = input("How many people to split the bill?")

total_with_tip = int(total_bill)*(1+int(tip_percent)/100)
per_person = total_with_tip/int(split_ppl)

per_person = float(round(per_person,2))

print(f"Each person should pay: ${per_person}")
