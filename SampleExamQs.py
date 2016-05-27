# Write a function that takes a list and a word as parameters and returns the
# index of that word in the list, or “False” if it does not appear in the list

def findIndex (list,word):
    result = False
    for i in range(len(list)):
        if list[i]==word:
            result = i

    return result
print(findIndex(["blah","stuff","things"],"stuff"))

# Write a program that reads in numbers from the keyboard, one per line,
# until the user enters the word “quit”, and then prints the sum of those numbers.


total = 0

x = 0
val = input("number to add")

while val!="quit":
    val = int(val)
    total += val
    val = input("number to add")

print(total)

# Write a program that reads in 10 numbers from the keyboard and prints out
# the smallest number entered

smallest = float(input("please enter a number"))
for i in range(9):
    x = float(input("please enter a number"))
    if x < smallest:
        smallest = x

print(smallest)


# Write a program that reads in numbers from a keyboard until the user enters -1,
# then prints out each of the numbers with their frequency.

