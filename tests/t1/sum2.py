# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

total = 0
num = float(input("please enter a number"))

while num!=-1:

    total = total + num
    num = float(input("please enter a number"))

#
# x=0
# i=0
# notneg=True
# while notneg:
#     response = input("num")
#     if int(response) == -1:
#         notneg=False
#     else:
#         x = x+int(response)
#         i=i+1
#
# y=0
# x=0
# while x<10:
#     num = int(input("num"))
#     if num==-1:
#         x=11
#     else:
#         y = y+ num
#
# total = 0

numbers = []
argument = True
while argument:
    thisnum = input("num")
    if "-1" in thisnum:
        argument = False
        print(sum(numbers))
    else:
        numbers.append(int(thisnum))



# print(y)
# print (total)