#Christopher Kenny
#CS-175

#Checking Temp Utilizing While Loop Within Function:
def check_temp():
    max_temp = 100
    temp = int(input("Enter the current temperature (in °F): "))
    while temp > max_temp:
        print("The temperature is too high.")
        temp = int(input("Please enter the re-adjusted temperature: "))
    else:
      print("The temperature is acceptable.")
#Print
check_temp()
