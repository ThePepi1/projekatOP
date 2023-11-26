import Korisnik
import Film
# TODO rewrite main (make it cleaner and easyer to read use functions to create menus, probavbly another file)
menu = "Ukoliko zeliteta da izadjete ukucajte: Exit\nUkoliko zelite da vidite sve dostupne filmove unesite pregled filma\nUkoliko zelite da pretrazite filmove po jednoj stavci ukucajte pretraga filmova 1\nUkoliko zelite da pretrazite filmove po vise stavaka ukucajte pretraga filmova 2"
menu_not_loged = "Ukoliko zelite da se Prijavite ukucajte prijava\nUkoliko zelite da se registrujete ukucajte registruj"
menu_loged = "Ukoliko zelite da se odjavite ukucajte odjava\nUkoliko zelite da promenite podatke ukucajte izmeni podatke"
menu_loged_meneager = "Ukoliko zelite da registrujete novog prodavca ukucajte registruj prodavca.\nUkoliko zelite da registrujete novog menadzera ukucajte registruj menadzera."
def login():
    while if_loged== False:
        username = input("Unesi korisnicko ime ")
        if username == "X":
            return False , None
        password = input("Unesi lozinku ")
        loged = Korisnik.login(username, password)
        if loged !=  None:
            return True, loged





if __name__ == "__main__":
    if_loged = False
    user_input = ""
    user = None
    Korisnik.load()
    Film.load()
    while True:
        print(menu)
        if not if_loged:
            print(menu_not_loged)
        if if_loged:
            print(menu_loged)
            if user.type == 3:
                print(menu_loged_meneager)

        user_input = input()
        if user_input == "Exit":
            break
        elif user_input == "prijava":
            if_loged, user = login()
        elif user_input == "registruj" and not if_loged:
            Korisnik.register()
            Korisnik.save()
        elif user_input == "odjava" and if_loged:
            user = None
            if_loged = False    
            continue
        elif user_input == "izmeni podatke" and if_loged:
            user = user.edit_profile()
            Korisnik.save()
        elif user_input == "pregled filma":
            Film.print_movies()
        elif user_input == "pretraga filmova 1":
            Film.pretraga_filmova()
        elif user_input == "pretraga filmova 2":
            print("Unesite brojeve koje zelite da pretrazite razdvojene razmakom")
            Film.pretraga_filmova()
        elif user_input == "registruj menadzera" and if_loged == True and user.type == 3:
            user.create_manager() 
        elif user_input == "registruj prodavca" and if_loged == True and user.type == 3:
            user.create_seller()   
        else:
            print("Nepostojeca naredba")

    Korisnik.save()