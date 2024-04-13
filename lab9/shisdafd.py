#My name is Shingo Kitamura
#11/6/2023
#Here is about Lab 9.

#==================================================================
#1.Input a name, grades and hours while users are trying to enter.
#2.Change the grades to GPA.
#2.Show the result for one student.
#3.Show the results for all of stundents that users type.
#==================================================================

 #These are the sentences for introductions.
intro1 = "Welcome to The English-Spanish dictionary\n"\
         "(PLease Enter 'Q' or 'q' when you finish.)"

Qengword = "Enter the English word to translate to Spanish : "
Qnoword = "There is no such a word in the dictionary.\n"\
          "Do you want to add the word to the dictionary?\n"\
          "(Please enter 'Yes' or 'No')\n"
Qengwordtoadd = "Enter the English to word to add to the dictionary : "
Dictionary = []
i = 0
try:
    file1 = open("spanishDictionary.csv", 'r')


    # Read the file and add the sentences to the list of Dictionary
    for x in file1:
        i += 1
        currentline = x
        Dictionary.append(currentline.split())

except:
    print("The file is not found")

while 1 == 1:
    Aengword = input(Qengword)
    KEY = 0

    if Aengword == "Q":
        break

    for y in range(i):
        if Aengword == Dictionary[y][0]:
            print(str(Aengword) + " is " + str(Dictionary[y][1]) + " in Spanish.")
            KEY = 1

    for z in Aengword:
        if Aengword.isalpha() == 0:
            print("Input the correct word")
            KEY = 1

    if KEY == 0:
        print("There is not the word that you entered.")
        if 'y' == input("would you like to add new word?"):
            spanish = input("what is the spanish word: ")
            Dictionary.append([Aengword, spanish])
            print("write complete ")
            print("New word can read after new RUN")
            print(Dictionary)
            i+=1

