"""
* This program counts names of the file "name.txt"
* Teruaki Murakami
* 2023/11/02
"""
"""
* 1. Open the file
* 2. Read the file
* 3. separate Raed string from file
* 4. counts the numbers
* 5. print the counted number
"""
intro = "This program counts name of this file"
#sum of the numbers
number = 0
#open the file
file = open("name.txt","r")

#read file
namesline = file.read()
#seoarete names
names = namesline.split(',')

for i in names:
    number += 1

print(intro)
print("the number of the names are: "+str(number))