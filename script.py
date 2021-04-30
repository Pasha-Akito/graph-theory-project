
import shuntingre
import thompson

def menu():
    print("-------------------------------------------------")
    print("Pavel Antonov ------------------------- G00373627")
    print("-------------------------------------------------")
    print("Press 1 to Input a Regex-------------------------")
    print("Press 2 to exit program--------------------------")
    print("-------------------------------------------------")

    userInput = int(input("Please enter a number\n"))
    if(userInput == 1):

        fileReader = "" # will be used to read all the strings
        regexInput = input("Please input a regex\n")

        fileInput = open(input("Please enter the file name/path\n"))
        fileReader += fileInput.read()
        print(fileReader)

        infix = regexInput
        print(f"infix: {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix: {postfix}")

        nfa = thompson.re_to_nfa(postfix)
        print(f"NFA from Thompsons Construction: {nfa}")
        matches = nfa.match(fileReader)
        print(f"matches: {matches}")

        if matches:
            print(f"The regex {nfa} has been found in the text file {fileReader}\n")
        else:
            print(f"The regex {nfa} has not been found in the text file {fileReader}\n")
    
    elif(userInput == 2):
        exit()
    
    menu()
    
    

menu()



