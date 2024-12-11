variableTypes = ["int","str","bool","float"]



code = []
variables = []


#Save Code
def saveCode():
    print("\n\n\n")
    print(code)
    print(variables)
    print(printData)
    print(inputData)



#Variable Modification
def varMod():
    choice = input("(1) New Variable\n(2) Existing Variable\n>> ")
    if choice == "1":
        variableName = input("What do you whant the variable to be named:\n>> ")
        data = input("What do you whant the variable data to be:\n>> ")
        code.append(["input", len(inputData)])

        if variableName not in variables:
            variables.append([variableName, ""])
    elif choice == "2":
        newInput()
    else:
        print("Error")
        varMod()








#Print
printData = []

def newPrint():
    if runCode == False:
        data = input("What do you whant to print:\n>> ")
        printData.append(data)
        code.append(["print", len(printData)])


#input
inputData = []

def newInput():
    variableName = input("What do you whant the variable to be named:\n>> ")
    data = input("What do you whant the text to be:\n>> ")
    inputData.append([variableName, data])
    code.append(["input", len(inputData)])

    if variableName not in variables:
        variables.append([variableName, ""])
   



#View Code
def viewCode():
    print("////////////////CODE/////////////////\n")

    for x in code:
        if x[0] == "print":
            print(x[0] + "('"+printData[x[1]-1]+"')")
        elif x[0] == "input":
            print(inputData[x[1]-1][0] +" = "+ x[0] + "('"+inputData[x[1]-1][1]+"')")
        else:
            print("")

    print("\n//////////////CODE///////////////////")

def find(listToFind, dataToFind):
    for x in listToFind:
        if dataToFind in x:
            return listToFind.index(x)

#Run Code
def runCode():
    print("////////////////CODE/////////////////\n")
    for x in code:
        if x[0] == "print":
            print(printData[x[1]-1])
        elif x[0] == "input":
            variables[find(variables, inputData[x[1]-1][0])][1] = input(inputData[x[1]-1][1]+"\n>> ")
        else:
            print("")

    print("\n//////////////CODE///////////////////")
   
#View Variables
def viewVariables():
    print("////////////////VARIABLES/////////////////\n")
   
    for x in variables:
        print(x[0]+" >>"+x[1]+"<<")

    print("\n//////////////VARIABLES///////////////////")


def menu():
    choice = input("(1) Print\n(2) Input\n(3) View Code\n(4) Run Code\n(5) View Variables\n(6) Save code\n>> ")
    if choice == "1":
        newPrint()
    elif choice == "2":
        newInput()
    elif choice == "3":
        viewCode()
    elif choice == "4":
        runCode()
    elif choice == "5":
        viewVariables()
    elif choice == "6":
        saveCode()
    else:
        print("Error")
    menu()

menu()
