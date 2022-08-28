import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_names = len(names)

print(length_names)

pick_name_index = random.randint(1, (length_names-1))

print(pick_name_index)

print(f"{names[pick_name_index]} is going to pay the bill")
