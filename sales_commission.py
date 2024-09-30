#Christopher Kenny
#CS 175
#Series of Commission Assignment
sales = 0

#Individual sales commission calculator

while sales >= 0:
  sale_amount = float(input("Enter sales: "))
  total = sale_amount
  sales + 1
  user_input = str(input("Do you have another sale to enter? "))
  if user_input == "yes":
    continue
  else:
    commission_rate = float(input("Enter commission rate (in decimal form): "))
    break
commission = total * commission_rate
print("Your commission is:", "$", "{:.2f}".format(commission))
