'''
* The purpose of this program is to caluculate sum
* Auther: Teruaki Murakami
* Last Edit Data: 09/13/2023
'''
number1st =int(input("Enter the first 4-digit number:"))
number2st =int(input("Enter the second 4-digit number:"))
number3st =int(input("Enter the third 4-digit number:"))
answer = number1st + number2st + number3st
print(" " + str(number1st))
print(" " + str(number2st))
print("+" + str(number3st))
print("-----")
print(" " + str(answer))
print("The average is:"+ str(answer/3))
print("Program Terminating.")
