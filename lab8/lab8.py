"""
* this program calculate gpa
* Teruaki Murakmi
* 2023/10/24
* Algorithm
* 1. start loop
* 2. input name
* 3. check name if it is 0 quit
* 4. input grade
* 4.5 . input grade if it is 0 quit
* 5. convert grade to number
* 6. grade * number / number
"""
intro = "this is GPA Calculator please input name grade and hours\n" \
"The grade is (A+ A A- B+ B B- C+ C C- D+ D D- F)"
explain = "input the grade and if you want to quit input 0 when names and grade"
outputintro = "\n" \
"the courses "
formatoutput = "Grade Hours"
# list of grade and hours
# listnameave = []
listgrade = []
listhours = []
# sum of grade*hours and hours
sumgpahours = 0
sumhours = 0
allave = 0
numberofpeople = 0
print(intro)
print(explain)
# loop until inputed 0
while 1 == 1:
    name = input("name =")
    if name == "0":
        break

    numberofpeople += 1

    grade = input("grade =")
    listgrade.append(grade)
    # convert grade character to number
    if 'A+' == grade:
        gradepoint = 4.33
    elif 'A' == grade:
        gradepoint = 4
    elif 'A-' == grade:
        gradepoint = 3.67
    elif 'B+' == grade:
        gradepoint = 3.33
    elif 'B' == grade:
        gradepoint = 3
    elif 'B-' == grade:
        gradepoint = 2.67
    elif 'C+' == grade:
        gradepoint = 2.33
    elif 'C' == grade:
        gradepoint = 2
    elif 'C-' == grade:
        gradepoint = 1.67
    elif 'D+' == grade:
        gradepoint = 1.33
    elif 'D' == grade:
        gradepoint = 1
    elif 'D-' == grade:
        gradepoint = 0.67
    elif 'F' == grade:
        gradepoint = 0

    hours = int(input(" hours ="))
    listhours.append(hours)

    sumgpahours += gradepoint * hours
    sumhours += hours
    resultgpa = sumgpahours / sumhours

    print(outputintro + str(name) + "are:")
    print(formatoutput)
    for x in range(len(listgrade)):
        print(str(listgrade[x]) + "\t\t\t " + str(listhours[x]))

    print("\nresulting in a GPA of " + str(round(resultgpa, 1)))
    allave += resultgpa

allave = allave / numberofpeople
print("the all averages:" + str(round(allave, 1)))
