"""
* This program shows sales of the week
* Teruaki Murakami
* 2023/11/10
"""
"""
* 1. generate random number
* 2. print result
"""
import random

lottery = []
for i in range(7):
    number = random.randint(0,9)
    lottery.append(number)

for x in range(7):
    print(lottery[x])

print(lottery)