from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator ():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for key in operations:
    print(key)

  should_continue = True

  while should_continue:
    operation = input("Pick and operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation]
    result = calculation_function(num1,num2) 
    print(f"{num1} {operation} {num2} = {result}")
    option = input("Type 'y' to continue calculating with "+str(result)+", or type 'n' to start a new calculation:\n")

    if option == "y":
      num1 = result
    
    else:
      should_continue = False
      clear()
      calculator() #HERE THE GODDAMNED FUNCTION CALLS ITSELF
      
calculator()
