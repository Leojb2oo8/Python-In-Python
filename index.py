variableTypes = ["int","str","bool","float"]

code = []
variables = [['aefd', '78'], ['age', ''], ['length', 'tyrye5']]


#Save Code
def saveCode():
    print("\n\n\n")
    print(code)
    print(variables)
    askForVar()



#Variable Modification
#def varMod():
#    choice = input("(1) New Variable\n(2) Existing Variable\n>> ")
#    if choice == "1":
#        variableName = input("What do you whant the variable to be named:\n>> ")
#        data = input("What do you whant the variable data to be:\n>> ")
#        code.append([len(code)+1, "a", data])
#
#        if variableName not in variables:
#            variables.append([variableName, ""])
#    elif choice == "2":
#        newInput()
#    else:
#        print("Error")
#        varMod()


def askForVar():
    choice = input("Do you want to use an existing variable? (Y/N)")
    if choice == "Y":
        if len(variables) == 0:
            print("No Variables")
            return False

        else:
            for x in variables:
                print("("+str(variables.index(x)+1)+") "+ x[0])
            choice = input(">> ")
            if choice.isdigit() == True:
                if int(choice) > 0 and int(choice) <= len(variables):
                    return variables[int(choice)-1]
            
    print("Error")
    
    askForVar()
    




#If Statement
def newIf():
    print("Value 1:")
    value1 = askForVar()
    if value1 == False:
        value1 = input("What do you want to compare (first value; e.g. 1, 2312, hello):\n>> ")
        value1 = [value1, value1]

    compareson = input("How do you want to compare (compareson; e.g. ==, !=, >=, <):\n>> ")

    print("Value 2:")
    value2 = askForVar()
    if value2 == False:
        value2 = input("What do you want to compare (second value; e.g. 1, 2312, hello):\n>> ")
        value2 = [value2, value2]
    
    
    code.append([len(code)+1, "if", value1, compareson, value2]) 








#Line Remover
def removeLine():
    choice = input("What line do you whant to remove? 1-"+str(len(code))+"\n>> ")
    if choice.isdigit() == True:
        if int(choice) <= len(code) and int(choice) >= 1:
            code.pop(int(choice)-1)
            for x in code:
                if x[0] > int(choice):
                    x[0] -= 1
            return
        
    print("Error")
    removeLine()

#Print
def newPrint():
    data = input("What do you want to print:\n>> ")
    code.append([len(code)+1, "print", data])

#input
def newInput():
    variableName = input("What do you want the variable to be named:\n>> ")
    data = input("What do you want the text to be:\n>> ")
    code.append([len(code)+1, "input", [variableName, data]])

    if variableName not in variables:
        variables.append([variableName, ""])
   
#View Code
def viewCode():
    print("////////////////CODE/////////////////\n")

    for x in code:
        if x[1] == "print":
            print(str(x[0])+"    "+x[1] + "('"+x[2]+"')")
        elif x[1] == "input":
            print(str(x[0])+"    "+x[2][0] +" = "+ x[1] + "('"+x[2][1]+"')")
        
        elif x[1] == "if":
            print("if "+x[2][0]+" "+x[3]+" "+x[4][0]+":")

        else:
            print(str(x[0])+"    ")

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
            print(x[2])
        elif x[1] == "input":
            variables[find(variables, x[2][0])][1] = input(x[2][1]+"\n>> ")
        else:
            print("")

    print("\n//////////////OUTPUT///////////////////")
   
#View Variables
def viewVariables():
    print("////////////////VARIABLES/////////////////\n")
   
    for x in variables:
        print(x[0]+" >>"+x[1]+"<<")

    print("\n//////////////VARIABLES///////////////////")

#Menu
def menu():
    choice = input("(1) Code Edditing\n(2) Code Actions\n(3) Quit\n>> ")
    if choice == "1":
        choice = input("(1) Print\n(2) Input\n(3) Input\n(4) Remove Line\n>> ")
        if choice == "1":
            newPrint()
        elif choice == "2":
            newInput()
        elif choice == "3":
            newIf()
        elif choice == "4":
            removeLine()
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
    
    elif choice == "3":
            quit()
    else:
        print("Error")

    menu()

menu()