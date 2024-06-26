from art import logo
from replit import clear

def add(n1, n2):
  return n1 + n2
def sustract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sustract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  isContinue = "y"
  while isContinue == "y":
    for symbols in operations:
      print(symbols + "\n")
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    isContinue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if isContinue == 'y':
      num1 = answer
    else:
      clear()
      calculator()

calculator()