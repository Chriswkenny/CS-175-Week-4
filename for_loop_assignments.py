#Christopher Kenny
#CS 175
#Problem 1: Counting Vowels

#Setting Variables
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O","U"]
count = 0
input1 = input("Enter a word or sentence here: ")

#For loop
for char in input1:
  if char in vowels:
    count += 1

#Output
print(f"The number of vowels is: {count}")

#Christopher Kenny
#CS 175
#Problem 2: Multiplication Table

#Variables
user_input = int(input("Enter a number whose multiplication table you would like to see: "))
count = 0
result = 0

#For loop
for i in range(1, 11):
  count += 1
  result = user_input * i

#Output
  print(f"{user_input} * {i} = {result}")

#Christopher Kenny
#CS 175
#Problem 3: Dictionary

dictionary = {"Alice": 85,
              "Bob": 92,
              "Charlie": 78,
              "Diana": 88,
              "Eve": 91}

for key, value in dictionary.items():
  print(f"{key}: {value}")

#Christopher Kenny
#CS 175
#Problem 4: Evens and Odds


numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
evens = []
odds = []
even_numbers = 0
odd_numbers = 0

for num in numbers:
  if num % 2 == 0:
    even_numbers += 1
  else:
    odd_numbers += 1

print(f"The number of even numbers is: {even_numbers}")
print(f"The number of odd numbers is: {odd_numbers}")

#Christopher Kenny
#CS 175
#Problem 5: Largest/Smallest Number
numbers = [3, 5, 7, 2, 8, -1, 4]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num
  elif num < smallest:
    smallest = num

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
