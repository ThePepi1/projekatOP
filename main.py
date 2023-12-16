import Menu

if __name__ == "__main__":
    menu = ""
    user_input = ""
    Next = True
    Menu.start()
    while Next:
        menu = Menu.create_menu()
        user_input = input("Unesi naredbu ")
        if user_input in menu.keys():
            Next = menu[user_input]()
        else:
            print("Nepostojeca naredba")
           
