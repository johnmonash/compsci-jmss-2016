
datafile = open("data.txt")

# line = datafile.readline()
#
# print (line)
# linelist = line.split()
# print (linelist)

# work through every word in the line to find the word random and replace it with
# "ticklish"

for line in datafile:
    linelist = line.split()
    sentence = ""
    for i in range(len(linelist)):
        if linelist[i] == "random":
            linelist[i] = "ticklish"
        sentence = sentence + linelist[i]+ " "
    print (sentence)



