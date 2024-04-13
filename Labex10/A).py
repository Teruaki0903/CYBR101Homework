"""
* This program convert double character to $
* Teruaki Murakami
* 2023/11/17
"""
"""
* 1. input the word
* 2. double for 
* 3. check double 
* 4. edit word
"""
#introduction
intro = "This program convert double character to $"
#string for input
word = []
#string for check
checkbox = []
end_flag = False

print(intro)
word = input("String : ")
checkbox.append(word[0])
i = 1
for i in range(len(word)):
    if end_flag == True:
        break
    for j in range(len(checkbox)):
        if checkbox[j] == word[i]:
            if i == 0 & j == 0:
                break

            word = word[:i] + "$" + word[i+1:]
            end_flag = True
            break
    else:
        checkbox.append(word[i])

print("Result : "+str(word))