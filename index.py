variableTypes = ["int","str","bool","float"]
currentIndentation = 1

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
#        wichCodeToUse().append([len(code)+1, "a", data])
#
#        if variableName not in variables:
#            variables.append([variableName, ""])
#    elif choice == "2":
#        newInput()
#    else:
#        print("Error")
#        varMod()


def askForVar():
    choice = input("Do you want to use an existing variable? (Y/N)\n>> ")
    if choice == "Y" or choice == "y":
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
    elif choice == "N" or choice == "n":
        return False         
    print("Error")
    
    askForVar()
    
def askForOperators():
    choice = input("What operator do you whant to use?\n(1) '=='\n(2) '!='\n(3) '>'\n(4) '>='\n(5) '<'\n(6) '<='\n>> ")
    if choice == "1":
        return "=="
    elif choice == "2":
        return "!="     
    elif choice == "3":
        return ">"
    elif choice == "4":
        return ">="
    elif choice == "5":
        return "<"
    elif choice == "6":
        return "<="
    
    print("Error")
    askForOperators()

def wichCodeToUse():
    if len(code) == 0:
        return code
    elif code[len(code)-1][1] == "if":
        return code[len(code)-1][5]
    return code

#If Statement
def newIf():
    print("Value 1:")
    value1 = askForVar()
    if value1 == False:
        value1 = input("What do you want to compare (first value; e.g. 1, 2312, hello):\n>> ")
        value1 = [value1, value1]

    compareson = askForOperators()

    print("Value 2:")
    value2 = askForVar()
    if value2 == False:
        value2 = input("What do you want to compare (second value; e.g. 1, 2312, hello):\n>> ")
        value2 = [value2, value2]
    
    #ifCode = [[len(code)+2, "print", "hello"], [len(code)+2, "if", ["value1", "value1"], "==", "value2", ifCodeMaker([[len(code)+1, "print", "world"]])]]
    #wichCodeToUse().append([len(code)+1, "if", value1, compareson, value2, ifCodeMaker(len(code)+1, ifCode)])
    wichCodeToUse().append([len(code)+1, "if", value1, compareson, value2, []])


def lineNumMaker():
    counter = 1
    for x in code:
        if x[1] == "if":
            for y in x[1]:
                




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
    wichCodeToUse().append([len(code)+1, "print", data])

#input
def newInput():
    variableName = input("What do you want the variable to be named:\n>> ")
    data = input("What do you want the text to be:\n>> ")
    wichCodeToUse().append([len(code)+1, "input", [variableName, data]])

    for x in variables:
        if x[0] == variableName:
            return
    
    variables.append([variableName, ""])
   
#View Code
def viewCode(codeToRun, tabulation, start = True, ):
    if start: 
        print("////////////////CODE/////////////////\n")

    for x in codeToRun:
        if x[1] == "print":
            print(str(x[0])+tabulation+x[1] + "('"+x[2]+"')")
        elif x[1] == "input":
            print(str(x[0])+tabulation+x[2][0] +" = "+ x[1] + "('"+x[2][1]+"')")
        
        elif x[1] == "if":
            print(str(x[0])+tabulation+"if "+x[2][0]+" "+x[3]+" "+x[4][0]+":")
            viewCode(x[5], tabulation+"    ", False)

        else:
            print(str(x[0])+"    ")

    if start: 
        print("\n//////////////CODE///////////////////")

def find(listToFind, dataToFind):
    for x in listToFind:
        if dataToFind in x:
            return listToFind.index(x)


def ifStatementRunCode(value1, operator, value2):
    if operator == "==":
        if value1 == value2:
            return True
    elif operator == "!=":
        if value1 != value2:
            return True
    elif operator == ">":
        if value1 > value2:
            return True
    elif operator == ">=":
        if value1 >= value2:
            return True
    elif operator == "<":
        if value1 < value2:
            return True
    elif operator == "<=":
        if value1 <= value2:
            return True
    else:
        return False



#Run Code
def runCode(codeToRun):
    print("////////////////OUTPUT/////////////////\n")
    for x in codeToRun:
        if x[1] == "print":
            print(x[2])
        elif x[1] == "input":
            variables[find(variables, x[2][0])][1] = input(x[2][1]+"\n>> ")
        elif x[1] == "if":
            if ifStatementRunCode(x[2][0], x[3], x[4][0]):
                runCode(x[5])

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
        choice = input("(1) Print\n(2) Input\n(3) If\n(4) Remove Line\n>> ")
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
            viewCode(code, "    ")
        elif choice == "2":
            runCode(code)
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