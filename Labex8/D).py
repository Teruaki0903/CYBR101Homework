"""
* This program read file "numbers.txt" and print average from the file
* Teruaki Murakami
* 2023/11/03
"""
"""
* 1. Open the file
* 1.5 if fail to open the file require proper name of the file 
* 2. Read the file
* 2.5 if fail to open the file require proper name of the file 
* 3. separate Raed string from file
* 4. sum and print number 
"""
intro = "This program read number from the numbers.txt and print the average"
try:
    file = open("numbers1.txt", "r") #when you make IOError change the file name
except IOError:

    while True:
        print("something happen please check the file")
        try:
            filename = input("please input proper file name (include .txt ):")
            file = open(filename, "r")
        except IOError:
            print("same error occur")
        else:
            break

try:
    numbersline = file.read()
    number_after_separate = numbersline.split(",")

    sum_number = 0

    for i in range(len(number_after_separate)):
        sum_number += int(number_after_separate[i])
    else:
        print(intro)
        print("The average of the numbers are " + str(sum_number / len(number_after_separate)))

except ValueError:
    print("Something happened in the values")
