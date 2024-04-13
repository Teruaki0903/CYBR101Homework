"""
* This program read file "C)file.txt" and print random number from the file
* Teruaki Murakami
* 2023/11/03
"""
"""
* 1. Open the file
* 2. Read the file
* 3. separate Raed string from file
* 4. make random number 
* 5. print the random number
"""
import random
intro = "This program read file C)file.txt and print random number from the file"
print(intro)

#open the file
file = open("C)file.txt","r+")

#read the file
numbersline = file.read()
#seoarete names
number_after_separate = numbersline.split(",")

sum_number = 0

for i in range(len(number_after_separate)):
    sum_number += int(number_after_separate[i])
else:
    print("The sum of the numbers are "+str(sum_number))

random_number = random.randint(0,len(number_after_separate)-1)
print("the random number are "+str(number_after_separate[random_number]))