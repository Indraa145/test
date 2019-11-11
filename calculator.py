print("Solution 1 (Only works for 2 numbers)")
while True:
    try:
        num1 = int(input("Enter the first number: "))
    except:
        print("Please enter a valid number")
        continue
    break

while True:
    try:
        num2 = int(input("Enter the second number: "))
    except:
        print("Please enter a valid number")
        continue
    break

while True:
    operator = input("Enter the operator (+,-,*,/): ")

    result = 0
    if(operator == "+"):
        result = num1 + num2
    elif(operator == "-"):
        result = num1-num2
    elif(operator == "*"):
        result = num1*num2
    elif(operator == "/"):
        result = num1/num2
    else:
        print("An error occurred, please enter an operator")
        continue

    print("The result is: " + str(result))
    break

print("")
print("Solution 2 (Using python built-in function)")
while True:
    try:
        operationResult = eval(input("Please enter an operation problem: "))
    except:
        print("Please enter a valid operation problem")
        continue
    print("The result is: " + str(operationResult))
    break

#Average Calculator
print("")
print("Average Calculator")

def calculateAverage(listOfNumbers):
    return sum(listOfNumbers)/len(listOfNumbers)

while True:
    try:
        inputString = input("Please enter a sequence of number (separated by ','): ")
        inputList = inputString.split(",")
        inputList = list(map(float, inputList))
    except:
        print("Please enter a valid sequence (separate the numbers using ','): ")
        continue

    result = calculateAverage(inputList)
    print("The result is: " + str(result))
    break