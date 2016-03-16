# Write a program to print out an isosceles triangle of Xs
# rewrite the program to work for an arbitrary number of rows (ie the user can
# enter the required number of rows)


def triangle(height):
    for i in range(height):
        spaces = height - i - 1
        xs = 2 * i + 1
        print("-" * spaces + "|" * xs + "-" * spaces)

h = int(input("how many lines?"))

triangle(h)
