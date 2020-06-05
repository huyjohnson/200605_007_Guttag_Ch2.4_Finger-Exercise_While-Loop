# - Finger exercise - Guttag chapter 2.4 - while loop
# Replace the comment in the following code with a while loop
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
# Below addition of while loop
while toPrint == '':                # While toPrint is still an empty str
    toPrint = 'X' * numXs
# Above addition of while loop
print(toPrint)
