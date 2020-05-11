import json
from difflib import get_close_matches

data= json.load(open("firstapp/data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]

    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        yn= input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        if yn.upper()== "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word doesnt exist. Please recheck it."
        else:
            return "we didn't undersand your entry."
    else:
        return "The word doesnt exist. Please recheck it."

while True:
    string = "Welcome to the Dictionary"
    mainMenu = input("Please Choose: \n1. Dictionary\n2. Quit\n")
    if mainMenu == "1":
        print("                               ", string)
        while True:
            loops = input("Enter a word to find: ")
            if loops == "/end":
                print("Thank you, See you!")
                break
            elif loops:
                output = translate(loops)
                if type(output)==list:
                    for item in output:
                        print(item)
                    
                else:
                    print(output)
            else:
                break
    elif mainMenu == "2":
        print("Bye, Bye")
        exit()
    else:
        print("Try again")