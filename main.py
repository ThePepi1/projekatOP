import Korisnik
logedIn = False
script = "Ukoliko zeliteta da izadjete ukucajte: Exit\nUkoliko zelite da se Prijavite ukucajte prijava"
scriptNeReg = "Ukoliko zelite da se registrujete ukucajte registruj"
scriptloged = "Ukoliko zelite da se odjavite ukucajte odjava\nUkoliko zelite da promenite podatke ukucajte izmeni podatke"
if __name__ == "__main__":
    input1 = ""
    while input1 != "Exit":
        print(script)
        if not logedIn:
            print(scriptNeReg)
        if logedIn:
            print(scriptloged)
        input1 = input()
        if input1 == "Exit":
            break
        exit = False
        if input1 == "prijava" and not logedIn:
            while logedIn== False:
                Username = input("Unesi korisnicko ime ")
                Password = input("Unesi lozinku ")
                loged = Korisnik.Login(Username, Password)
                if loged ==  "Greska":
                    exit = input("Ukoliko zelite da prekinete ukucajte Ne ukoliko ne zelite da pokusate ponovo samo pritisnite enter ")
                    if exit == "Ne":
                        break
                    continue
                else: 
                    logedIn = True
            continue
        if input1 == "registruj" and not logedIn:
            Korisnik.Register()
            continue
        if input1 == "odjava":
            loged = ""
            logedIn = False    
            continue
        if input1 == "izmeni podatke":
            loged.EditProfile()
        print("Nepostojeca naredba")
