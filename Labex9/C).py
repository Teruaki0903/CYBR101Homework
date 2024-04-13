"""
* This program shows sales of the week
* Teruaki Murakami
* 2023/11/10
"""
"""
* 1. input monthly rainfall
* 2. sum average max min
* 3. print result
"""

monthryrainfall = []
weekdays = ["January","February","March","April","May","June","Jury","August","September","october","November","December"]

for i in weekdays:
    rainfall = int(input("input " + str(i)+ " days sales:"))
    monthryrainfall.append(rainfall)

result = sum(monthryrainfall)
averesult = round(result/12)
maxresult = max(monthryrainfall)
minresult = min(monthryrainfall)

print("The sum of the Rainfalls are "+str(result))
print("The ave of the Rainfalls are "+str(averesult))
print("The max of the Rainfalls are "+str(maxresult))
print("The min of the Rainfalls are "+str(minresult))