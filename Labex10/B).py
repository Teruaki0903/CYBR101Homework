"""
* This program add ing add ly
* Teruaki Murakami
* 2023/11/17
"""
"""
* 1. check ing
* 2. check ly
"""
#introduction
intro = "This program add ing add ly"
#string for input
word = []

#print ans
print(intro)
word = input("Input word:")

if word[len(word)-3] == "i" and word[len(word)-2] == "n" and word[len(word)-1] == "g":
    word = word + "ly"
elif len(word) >= 3:
    word = word + "ing"
else:
    word = word

print("result:" + str(word))