with open('./text.txt') as file:
    theContent = file.read()
print(theContent)

with open('./text.txt') as file1:
    theContent1 = file1.readlines()
print(theContent1)
