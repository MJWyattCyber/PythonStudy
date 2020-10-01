#Function to take the input and divide it by two until the output is 1, storing this in the list numDividedBy2
def divideBy2(numberEntered):
    while int(numberEntered) != 1:
        numDividedBy2.append(int(numberEntered))
        numberEntered = int(numberEntered)/2
    numDividedBy2.append(1)

#Function to take the list of divided numbers and convert it to binaray values
def convertToBinary(numDividedBy2):
    for i in numDividedBy2:
        if i % 2 == 0:
            convertedToBinary.append(0)
            #(Remove this comment to add Verbose)print('Added ' + str(i) + ' to the list.')
        else:
            convertedToBinary.append(1)
            #(Remove this comment to add Verbose)print('Added ' + str(i) + ' to the list.')

#Function to print the binary list
def printBinaryNum(convertedToBinary):
    convertedToBinary.reverse()
    print(*convertedToBinary, sep='')

    
numDividedBy2 = []
convertedToBinary = []

print("Welcome, please enter a number to convert this to Binary:")
numberEntered = input()

#Completes the two function calls to complete the lists
divideBy2(numberEntered)
convertToBinary(numDividedBy2)

#Prints the output to the user
print('Thanks, ' + str(numberEntered) + ' in binary is:')
printBinaryNum(convertedToBinary)
