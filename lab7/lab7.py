"""
* This program shows the number of the letter in string
* Teruaki Murakami
* 2023/aug/11
"""
#this function counts the number of the letter in string
def countChars(input, letter):
    i = 0
    countresult = 0
    while i < len(input):
        if input[i] == letter:
            countresult = countresult + 1
        i= i + 1
    #countresult = input.count(letter)
    return countresult
#this function prints the result of counting
def printResults(charCount):
    print("'"+str(letter)+"'"+"appears " +
    str(charCount)+" times(s) in "+"'"+str(inputstring)+"'")

#show the intro and input value
inputstring = input("Enter the string:")
letter = input("Enter the character to count:")
result = countChars(inputstring,letter)
printResults(result)
