"""
* This program shows sales of the week
* Teruaki Murakami
* 2023/11/10
"""
"""
* 1. for list
* 2. if i in list
* 3. print result
"""


def function(list, n):
    for i in list:
        if list[i - 1] > n:
            print(str(list[i - 1]))


Dlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 5

function(Dlist, num)
