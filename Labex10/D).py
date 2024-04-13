"""
* This program convert lower to upper
* Teruaki Murakami
* 2023/11/17
"""
"""
* 1. input the word
* 2. swap word
"""
#introduction
intro = "This program convert lower to upper"
#string for input
word = []
#string for answer
answord = []
print(intro)
word = input("input word:")
for i in range(len(word)):
    if word[i].islower():
        answord += word[i].upper()
    elif word[i].isupper():
        answord += word[i].lower()

print("The result is :"+str(answord))