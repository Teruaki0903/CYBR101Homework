"""
* Teruaki Murakami
* 2023/09/20
* This program is calculate 4-digit numbers one place two place third place fourth
place of sum
"""
digit_number = int(input("Enter a 4-digit number: "))# input 4-digit
#sepalate each place
first = int(digit_number/1000)
second = int((digit_number/100)-(first*10))
third = int((digit_number/10)-(first*100)-(second*10))
forth = int((digit_number)-(first*1000)-(second*100)-(third*10))
#sum each place
sum = first +second+third+forth
print("The sum of digits of the number "+ str(digit_number) + " is "+ str(first)+"+ "+ str(second) +" + "+ str(third)+" + "+ str(forth)+" = " + str(sum))
