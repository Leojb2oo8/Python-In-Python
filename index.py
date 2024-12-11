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
        code.append([len(code)+1, "input", len(inputData)])

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
    data = input("What do you whant to print:\n>> ")
    printData.append(data)
    code.append([len(code)+1, "print", len(printData)])


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
        if x[1] == "print":
            print(x[1] + "('"+printData[x[2]-1]+"')")
        elif x[1] == "input":
            print(inputData[x[2]-1][0] +" = "+ x[1] + "('"+inputData[x[2]-1][1]+"')")
        else:
            print("")

    print("\n//////////////CODE///////////////////")

def find(listToFind, dataToFind):
    for x in listToFind:
        if dataToFind in x:
            return listToFind.index(x)

#Run Code
def runCode():
    print("////////////////OUTPUT/////////////////\n")
    for x in code:
        if x[1] == "print":
            print(printData[x[2]-1])
        elif x[1] == "input":
            variables[find(variables, inputData[x[2]-1][0])][1] = input(inputData[x[2]-1][1]+"\n>> ")
        else:
            print("")

    print("\n//////////////OUTPUT///////////////////")
   
#View Variables
def viewVariables():
    print("////////////////VARIABLES/////////////////\n")
   
    for x in variables:
        print(x[1]+" >>"+x[2]+"<<")

    print("\n//////////////VARIABLES///////////////////")


def menu():
    choice = input("(1) Code Edditing\n(2) Code Actions\n(3) Quit\n>> ")
    if choice == "1":
        choice = input("(1) Print\n(2) Input\n>> ")
        if choice == "1":
            newPrint()
        elif choice == "2":
            newInput()
        elif choice == "3":
            quit)
        else:
            print("Error")

    elif choice == "2":
        choice = input("(1) View Code\n(2) Run Code\n(3) View Variables\n(4) Save code\n>> ")
        if choice == "1":
            viewCode()
        elif choice == "2":
            runCode()
        elif choice == "3":
            viewVariables()
        elif choice == "4":
            saveCode()
        else:
            print("Error")
    else:
        print("Error")

    menu()

menu()