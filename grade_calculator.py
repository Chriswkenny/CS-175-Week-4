#Christopher Kenny
#CS 175

#Squaring a list of elements
num = [2, 4, 6, 8]
for i in num:
  squared = i ** 2
  print(squared)

#Grade Calculator
marks = [85, 92, 78, 90, 88]
total = 0
average = 0

for i in marks:
  total += i

average = total / len(marks)
print("Your average grade is:",average)
if average >= 90:
    print("Your grade is: A")
elif average < 90 and average >= 80:
    print("Your grade is: B")
elif average < 80 and average >= 70:
    print("Your grade is: C")
elif average < 70 and average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
#End
