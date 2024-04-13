"""
* This program shows sales of the week
* Teruaki Murakami
* 2023/11/10
"""
"""
* 1. input sales of the week
* 2. show the result
"""


weeksales = []
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for i in weekdays:
    sales = int(input("input " + str(i)+ " days sales:"))
    weeksales.append(sales)

result = sum(weeksales)
print("The sum of the weeks are "+str(result))