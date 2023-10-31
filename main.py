import Korisnik
if_loged = False
menu = "Ukoliko zeliteta da izadjete ukucajte: Exit\nUkoliko zelite da se Prijavite ukucajte prijava"
menu_not_loged = "Ukoliko zelite da se registrujete ukucajte registruj"
menu_loged = "Ukoliko zelite da se odjavite ukucajte odjava\nUkoliko zelite da promenite podatke ukucajte izmeni podatke"
if __name__ == "__main__":
    user_input = ""
    while user_input != "Exit":
        print(menu)
        if not if_loged:
            print(menu_not_loged)
        if if_loged:
            print(menu_loged)
        user_input = input()
        if user_input == "Exit":
            break
        exit = False
        if user_input == "prijava":
            while if_loged== False:
                Username = input("Unesi korisnicko ime ")
                Password = input("Unesi lozinku ")
                loged = Korisnik.Login(Username, Password)
                if loged ==  "Greska":
                    exit = input("Ukoliko zelite da prekinete ukucajte Ne ukoliko ne zelite da pokusate ponovo samo pritisnite enter ")
                    if exit == "Ne":
                        break
                    continue
                else: 
                    if_loged = True
            continue
        if user_input == "registruj" and not if_loged:
            Korisnik.Register()
            continue
        if user_input == "odjava":
            loged = ""
            if_loged = False    
            continue
        if user_input == "izmeni podatke":
            loged = loged.EditProfile()
        print("Nepostojeca naredba")
