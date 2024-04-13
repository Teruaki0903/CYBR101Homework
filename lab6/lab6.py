"""
* This program shows that the total bonus of the Sahara`s
styleEmployee
* Teruaki Murakami
* 2023/OCT/04
* Algorithm
* input code salary time
* check code 1:
* One week pay; maximum of $700
* code 3:
* One and a half weeks pay
"""
#Code 2: Two weekss pay
if Code == 1:
    totalBonus = Salary
elif Code == 2:
    totalBonus = Salary*2
if totalBonus >= 700:
    totalBonus = 700
elif Code == 3:
    totalBonus = float(Salary*1.5)
#-----------------------------------------------
#plus a section
if Time < 2:
    totalBonus = totalBonus /2
elif Time > 10:
    totalBonus = totalBonus + 100
print("\nThe total bonus is "+str(round(totalBonus)))
#+"\n"+str(Code)+" "+str(Salary)+" "+str(Time)) # debug the var