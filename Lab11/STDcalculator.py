"""
* This program calculate standard deviation from csv file
* Teruaki Murakami
* 2023/11/15
"""
"""
* 1. read csv file 
* 2. input the number to list
* 3. calculate avrage 
* 4. calculate sigma
"""
import math
import numpy as np

def STDcalculator(nparray):
    #all number from the array
    allnumber = 0.0
    #sigma number
    sigmanumbers = 0.0

    for a in range(100):
        allnumber += nparray[a]
    average = round(allnumber/100,3)

    for b in range(99):
        sigmanumbers += (nparray[b] - average) * (nparray[b] - average)

    answer = round(math.sqrt(sigmanumbers / 100), 3)

    print("is " + str(average) + " and standard deviation: " + str(answer))

    return answer



intro = "\nThe average of the numbers in the file: "
filename1 = "numbers1.csv"
file1 = open(filename1, "r")
numbers_list1: list[float] = []

for i in range(100):
    string = file1.readline()
    number = float(string.replace("\n",""))
    numbers_list1.append(round(float(number),3))

newarray1 = np.array(numbers_list1)

print(intro + filename1)
STDcalculator(newarray1)

#second line
filename2 = "numbers2.csv"
file2 = open(filename2, "r")
numbers_list2: list[float] = []

for j in range(100):
    string = file2.readline()
    number = float(string.replace("\n",""))
    numbers_list2.append(round(float(number),3))

newarray2 = np.array(numbers_list2)

print(intro + filename2)
STDcalculator(newarray2)