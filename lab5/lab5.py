
"""
* This program ask question about good time to go to office.
* Teruaki Murakami
* 2023/09/27
"""
intro = "For your visit to our office, would you prefer Monday or Friday\n"\
"For Monday, enter 'm'\n"\
"For Friday, enter 'f'\n"
askprefer = "For morning, enter 'm'\n"\
"For afternoon, enter 'a'\n"
day = input(intro)
#convert m,f to Monday,Friday
if (day == 'm'):
    day = "Monday"
elif(day == 'f'):
    day = "Friday"
print("\nOn "+ str(day)+ " Would you prefer the morning or afternoon")
moraft = input(askprefer)
#convert m,a to morning,afternoon
# moraft means morning or afternoon
# time is the available time. it chages morning or afternoon
if(moraft == 'm'):
    moraft = "morning"
    time = "8:00 and 12:00"
if(moraft == 'a'):
    moraft = "afternoon"
    time = "1:00 and 4:00"
#show the day and morning of afternoon , and time
print("\nOn " + day + " " + moraft + " between "+ time +", what time would you like?")
apotime = input("")
print("\nYour next appointment is on " + day +" " +moraft +" at "+ apotime + ".")
