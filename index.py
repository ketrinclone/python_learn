from account import *
def displayMenu():
    print("welcome Hacktoberfest! :D\n")
    print("Sign in & Sign up\n")
    print("- type y to Login\n- type n to Sign up\n- type q to Quit\n- type h to see me!\n")
    status = input("Answer : ")
    if status == "y":
        oldUser()
    elif status == "q":
        exit()
    elif status == "n":
        newUser()
    elif status == "h" or "H":
        hand()
    else:
        wrongAns()

def hand():
    import webbrowser
    link_ig = "https://www.instagram.com/ferrrmi"
    webbrowser.open(link_ig)
 
def newUser():
    print("\n-----Sign up-----")
    createLogin = input("Create username : ")
 
    if createLogin in users:
        print("\nusername already exist!")
        newUser()
    else:
        createPassw = input("Create password : ")
        users[createLogin] = createPassw
        print("\nUser created! Please Log in to your account.")
        oldUser()
 
def oldUser():
    print("\n-----Login-----")
    login = input("Enter username : ")
    passw = input("Enter password : ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!")
        mainmenu()

    else:
        print("\nUsername doesn't exist or wrong password!")
        create_account = input("want to create your account?\n- y for yes\n- n for no\nAnswer : ")
        if create_account == "y":
            newUser()
        elif create_account == "n":
            oldUser()
        else:
            displayMenu()

def mainmenu():
    print("\n------ MAIN MENU ------\n")
    choose_mainmenu = input("Choose what you wanna do!\nSee the mulitiple choice above!\n- for Hektobercode type hek\n- for youtube type youtube\n- for Google Search type google\n- for Yandex Search type yandex\n- for exit type exit\n- for hacktoberfest site type xxx\nAnswer : ")
    if choose_mainmenu == "hek":
        hekfestcode()
    elif choose_mainmenu == "google":
        google()
    elif choose_mainmenu == "yandex":
        yandex()
    elif choose_mainmenu == "youtube":
        youtube()
    elif choose_mainmenu == "xxx":
        hacktoberSite()
    elif choose_mainmenu == "exit":
        exit()
    else:
        wrongAns()

def hacktoberSite():
    import webbrowser
    link_hacktoberfest = "https://hacktoberfest.digitalocean.com/"
    webbrowser.open(link_hacktoberfest)

def youtube():
    import webbrowser
    print("\n--- Google Searcher ---")
    print("what do you want to search?")
    youtube_search = input("Answer : ")
    link_youtube = "https://www.youtube.com/results?search_query="
    webbrowser.open(link_youtube + youtube_search)
    exit()

def google():
    print("\n--- Google Searcher ---")
    print("what do you want to search?")
    print("1 = web search\n2 = images search\n3 = videos search")
    choose_pick_google = input("Answer : ")
    if choose_pick_google == "1":
        import webbrowser
        input_web_google = input("\nWhat do you want to search?\nAnswer : ")
        link_web_google = "https://www.google.com/search?q="
        webbrowser.open(link_web_google + input_web_google)
        retryGoogle()
    elif choose_pick_google == "2":
        import webbrowser
        input_images_google = input("\nWhat do you want to search?\nAnswer : ")
        link_images_google = "https://www.google.com/search?q="
        encrypt_link_google_images = "&sxsrf=ALeKk00fjz7RfbMwi2wFrVB_ng7z11nVNQ:1601287281064&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKv8j8y4vsAhXc7XMBHUn8BU4Q_AUoA3oECB4QBQ&biw=1920&bih=969"
        webbrowser.open(link_images_google + input_images_google + encrypt_link_google_images)
        retryGoogle()
    elif choose_pick_google == "3":
        import webbrowser
        input_videos_google = input("\nWhat do you want to search?\nAnswer : ")
        link_videos_google = "https://www.google.com/search?q="
        encrypt_link_google_videos = "&source=lmns&tbm=vid&bih=969&biw=1920&hl=id&sa=X&ved=2ahUKEwj2vM6KzIvsAhW5y3MBHQ5wDr0Q_AUoAnoECAEQAg"
        webbrowser.open(link_videos_google + input_videos_google + encrypt_link_google_videos)
        retryGoogle()
    else:
        wrongAns()

def retryGoogle():
    retry_google = input("\nWant to exit? go to main menu? or repeat searching?\ntype q to quit\ntype d to go to main menu\ntype r to repeat search\nAnswer : ")
    if retry_google == "q":
        exit()
    elif retry_google == "d":
        oldUser()
    elif retry_google == "r":   
        google()
    else:
        wrongAns()

def yandex():
    print("\n--- Yandex Searcher ---")
    print("what do you want to search?")
    print("1 = web search\n2 = images search\n3 = videos search")
    choose_pick_yandex = input("Answer : ")
    if choose_pick_yandex == "1":
        import webbrowser
        input_web_yandex = input("\nWhat do you want to search?\nAnswer : ")
        link_web_yandex = "https://yandex.com/search/?text="
        webbrowser.open(link_web_yandex + input_web_yandex)
        retryYandex()
    elif choose_pick_yandex == "2":
        import webbrowser
        input_images_yandex = input("\nWhat do you want to search?\nAnswer : ")
        link_images_yandex = "https://yandex.com/images/search?text="
        webbrowser.open(link_images_yandex + input_images_yandex)
        retryYandex()
    elif choose_pick_yandex == "3":
        import webbrowser
        input_videos_yandex = input("\nWhat do you want to search?\nAnswer : ")
        link_videos_yandex = "https://yandex.com/video/search?text="
        webbrowser.open(link_videos_yandex + input_videos_yandex)
        retryYandex()
    else:
        wrongAns()

def retryYandex():
    retry_yandex = input("\nWant to exit? go to main menu? or repeat searching?\ntype q to quit\ntype d to go to main menu\ntype r to repeat search\nAnswer : ")
    if retry_yandex == "q":
        exit()
    elif retry_yandex == "d":
        oldUser()
    elif retry_yandex == "r":   
        yandex()
    else:
        wrongAns()

def hekfestcode():
    print("\nFork it and edit it!")
    print("--------------------------------")
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