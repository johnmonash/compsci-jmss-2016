# read in and process temperature data from Blackburn Sensor for March

data = open("visdata.csv")

headers = data.readline()
print (headers)

templist=[]
for line in data:
    line = line.strip()
    datalist = line.split(",")
    templist.append(float(datalist[1]))

print(templist)

# write code to separate the data into days, and that finds the maximum temp and humidity for each day.