# # Write a function that takes a list and a word as parameters and returns the
# # index of that word in the list, or “False” if it does not appear in the list
#
# def findIndex (list,word):
#     result = False
#     for i in range(len(list)):
#         if list[i]==word:
#             result = i
#
#     return result
# #print(findIndex(["blah","stuff","things"],"stuff"))
#
# # Write a program that reads in numbers from the keyboard, one per line,
# # until the user enters the word “quit”, and then prints the sum of those numbers.
#
#
# total = 0
#
# x = 0
# #val = input("number to add")
#
# while val!="quit":
#     val = int(val)
#     total += val
#     val = input("number to add")
#
# #print(total)
#
# # Write a program that reads in 10 numbers from the keyboard and prints out
# # the smallest number entered
# '''
# smallest = float(input("please enter a number"))
# for i in range(9):
#     x = float(input("please enter a number"))
#     if x < smallest:
#         smallest = x
#
# # print(smallest)

'''
# Write a program that reads in numbers from a keyboard until the user enters -1,
# then prints out each of the numbers with their frequency.

# Write a function that takes a list as a parameter and returns a list with any duplicate entries removed from the list.
# (so that every entry appears only once). For example, given the list [1,4,1,2,4,5] your
# function should return [1,4,2,5])  [*]
'''


# def dedup(vals):
#     result = []
#     for item in vals:
#         if item not in result:
#             result.append(item)
#     return result
#
#
# print(dedup([2,3,2,4,5,2,5]))


# Write a program that reads in the data from a csv file called “data.csv” and calculates the average of the column labelled “temp”.
# There is a header row, and you may assume that all the entries are numeric apart from the header row.

# data = open("data.csv")
#
# headers = data.readline()
#
# headerlist = headers.split(",")
#
# for i in range(len(headerlist)):
#     if "temp" == headerlist[i]:
#         index = i
#
# total = 0
# count = 0
# for line in data:
#     nums = line.split(",")
#     total+=float(nums[index])
#     count = count+1
#
# average = total / count

# Write a program that reads in numbers from a keyboard until the user enters -1,
# then prints out each of the numbers with their frequency.


numbers = []
counts = []
num = float(input("enter numbers, -1 to finish"))
while num != -1:
    if num not in numbers:
        numbers.append(num)
        counts.append(1)
    else:
        for i in range(len(numbers)):
            if numbers[i]==num:
                counts[i] += 1
    num = float(input("enter numbers, -1 to finish"))

for i in range(len(numbers)):
    print(numbers[i],counts[i])




















