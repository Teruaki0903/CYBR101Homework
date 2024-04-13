"""
* This is spanish dictionary
* Teruaki Murakami
* 2023/11/1
"""
#open file
dictinary = open("spanishDictionary.csv","r+")

intro = "this is english spanish dictionary please input english word"
#define english and spanish
ENGSPA = []
count = 0
#read file and input data to ENGSPA
for x in dictinary:
    count += 1
    currentline = x
    ENGSPA.append(currentline.split())

print(intro)

while 1 == 1:
    wrongword = 0
    keyword = input("input:")

    for k in keyword:
        if k.isalpha() == 0:
            print("please input proper word")
            wrongword = 1
            break

    if keyword == 'q':
        break

    for y in range(count):
        if keyword == ENGSPA[y][0]:
            print("English = "+str(keyword)+" ,Spanish = "+str(ENGSPA[y][1]))
            wrongword = 2

    if wrongword == 0:
        print("Error not found")
        if 'y' == input("would you like to add new word?"):
            spanish = input("what is the spanish word: ")
            dictinary.write("\n"+keyword+" "+spanish)
            print("write complete ")
            print("New word can not read after new RUN")

    wrongword = 0