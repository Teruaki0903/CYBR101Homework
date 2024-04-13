"""
* This program write random numbers to the "B)file.txt"
* Teruaki Murakami
* 2023/11/02
"""
"""
* 1. Open the file
* 2. input some numbers
* 3. make random number
* 4. write random numbers that inputted numbers
"""
import random

intro = "input number for number of random number"

#open the file
file = open("B)file.txt","a")

print(intro)
number = int(input("input the number: "))
#write names for inputted number
for i in range(number):
    #at the end of the file dont write ","
    if i+1 != number:
        file.write(str(random.randint(1,500))+",")
    else:
        file.write(str(random.randint(1,500)))