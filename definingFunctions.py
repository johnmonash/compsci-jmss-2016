# define a triangle function that takes two characters and the height as parameters

# def triangle(height,c1,c2): # height, c1 and c2 are parameters
#     for i in range(height):
#         spaces = height - i - 1
#         xs = 2 * i + 1
#         print(c1 * spaces + c2 * xs + c1 * spaces)
#
# h = int(input("how many lines?"))
# a = input("first char?")
# b = input("second char?")
#
# triangle(h,a,b) #h, a, and b are arguments
# triangle(h+1,a,b)
# triangle(6,a,b)

#print (c1)


# Define a function that takes a list as a parameter and prints out each item and
# its index one line per item, eg for l = [3,5,7]
# 0 3
# 1 5
# 2 7
# or if l=["cat","dog","glider"]
# 0 cat
# 1 dog
# 2 glider

def printItems(l):

    for i in range(len(l)):
        print (i,l[i])

words = ["fish","sun","cat","book"]
#printItems(words)

#define your own length function that takes a list as a parameter
# and returns the length of that list, without using the "len" function

def length(l):
    count=0
    for item in l:
        count = count + 1
    return count

print (length([4,3,2,6,8,9]))
print (length(words))

#write a function that returns the sum of all the numbers in a list

def sumList(l):