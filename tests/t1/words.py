# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

wordlist=[]
word = ""

while word!="quit":
    word = input("please enter a word: ")
    wordlist.append(word)

#wordlist.remove("quit")
wordlist=wordlist[:-1]

wordlist.sort()
for word in wordlist:
    print(word)

print (wordlist)