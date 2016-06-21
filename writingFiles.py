
outfile = open("fish.csv","w")
outfile.write("day,period,temp\n")
temp=23.4


outfile.write("string value here\n")
line = "235768296,24.5,67.0,24"

outfile.write("Monday,p1,"+str(temp)+'\n')

outfile.close()
