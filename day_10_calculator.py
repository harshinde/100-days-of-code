from art import logo

print(logo)

def add(n1, n2):
  """adds two numbers"""
  return n1+n2

def subtract(n1, n2):
  """subtracts two numbers"""
  return n1-n2

def multiply(n1, n2):
  """multiplies two numbers provided as args"""
  return n1*n2

def divide(n1, n2):
  """divides two numbers provided as args"""
  return n1/n2


#defining a dict named operations to store the operators


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

#looping through the operations dict

for opt in operations:
  print(opt)

operations_symbol = input("pick a calc operator from the above: ")

calc_op = operations[operations_symbol]
answer = calc_op(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")
