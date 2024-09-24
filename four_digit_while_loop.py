#Christopher Kenny
#CS-175

def four_digit_function():
  digits = int(input("Enter a four digit integer: "))
  while digits > 9999 or digits <= 999:
    print("Your input was not four digits.")
    digits = int(input("Please enter a FOUR digit integer: "))
  else:
    digit1 = digits // 1000 % 10
    digit2 = digits // 100 % 10
    digit3 = digits // 10 % 10
    digit4 = digits % 10
    sum = digit1 + digit2 + digit3 + digit4
    print(f"The individual digits of your input are: {digit1}, {digit2}, {digit3}, {digit4}" )
    print(f"The sum of your inputs is: {sum}")
#Print
four_digit_function()
