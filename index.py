from account import *
def displayMenu():
    print("welcome Hacktoberfest! :D\n")
    print("Sign in & Sign up\n")
    print("Are you already sign up here?")
    print("y = yes\nn = no\nq = quit\n")
    status = input("Answer : ")
    if status == "y":
        oldUser()
    elif status == "q":
        exit()
    elif status == "n":
        newUser()
    else:
        wrongAns()
 
def newUser():
    createLogin = input("\nCreate username : ")
 
    if createLogin in users:
        print("\nLogin name already exist!")
    else:
        createPassw = input("Create password : ")
        users[createLogin] = createPassw
        print("\nUser created! Please Log in your account.")
 
def oldUser():
    login = input("\nEnter username : ")
    passw = input("Enter password : ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!")
        mainmenu()

    else:
        print("\nUser doesn't exist or wrong password!")
        oldUser()

def mainmenu():
    z = input("\nChoose what you wanna do!\nHektober unknown code or Google Search?\nfor Hektober type hek\nfor Google Search type google\nAnswer : ")
    if z == "hek":
        hekfestcode()
    elif z == "google":
        google()
    else:
        wrongAns()

def google():
    i = 1
    while i == 1:
        import webbrowser
        print("\n--- Google Searcher ---")
        go = input("\nWhat do you want to search?\nAnswer : ")
        link = "https://www.google.com/search?q="
        webbrowser.open(link + go)
        q = input("\n\nWant to exit? go to main menu? or repeat searching?\ntype q to quit\ntype d to go to main menu\ntype r to repeat search\nAnswer : ")
        if q == "q":
            exit()
        elif q == "d":
            oldUser()
        elif q == "r":   
            continue
        else:
            wrongAns()

def hekfestcode():
    print("\nFork it and edit it!")
    print("\n--------------------------------")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("--------------------------------\n")
    print("to go back type back")
    num = input("Choose them now!\nAnswer : ")
    if(num == "1"):
    # indented four spaces
        print ("\n#hacktoberfest")
        rows = 6
        for jail in range(rows):
            for i in range(jail):
                print(jail, end=" ")  # print number
            # line after each row to display pattern correctly
            print(" ")

    elif(num == "2"):
    # indented four spaces
        print ("\nFORK IT!")
        rows1 = 5
        for crit in range(1, rows1+1):
            for column in range(1, crit+1):
                print(column, end=" ")
            print(" ")

    elif(num == "3"):
    # indented four spaces
        print ("\nPULL IT!")
        rows2 = 5
        b = 0
        for crit1 in range(rows2, 0, -1):
            b +=1
            for column1 in range(1, crit1 + 1):
                print(b, end=" ")
            print("\r")
        
    elif(num == "4"):
    # indented four spaces
        print ("\nCOMMIT NOW!")
        rows3 = 5
        c = rows3
        for crit2 in range(rows3, 0, -1):
            for column2 in range(0, crit2):
                print(c, end=' ')
            print("\r")

    elif(num == "5"):
    # indented four spaces
        print ("\nwhat r u doing n o w????")
        s = str(input("ur answer : "))
        print("you are doing",(s),"everyday???? LOL")

    elif(num == "hacktoberfest"):
    # indented four spaces
        from hckfest import Hckfest
        Hckfest()

    elif(num == "back"):
        oldUser()
    
    else:
        wrongAns()

def wrongAns():
    print("\nwrong answer!\n")
    print("want to try again?\ny = yes\nn = no")
    ans = input("Answer : ")
    if ans == "y":
        displayMenu()
    elif ans == "n":
        exit()
    else:
        exit()

while status != "q":
    displayMenu()