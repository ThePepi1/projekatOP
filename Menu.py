import modules.Korisnik as Korisnik
import modules.Film as Film
import modules.bioskoska_projekcija as bioskoska_projekcija
import modules.Sala as Sala
import modules.Termin as Termin
loged_user = None
def create_menu():
    if loged_user == None:
        print_menu_not_loged()
        return menu_not_loged
    if loged_user.type == 1:
        print_menu_loged()
        return menu_loged
    if loged_user.type == 2:
        return menu_loged_seller
    if loged_user.type == 3:
        print_menu_loged_meneager()
        return menu_loged_meneager
  

def start():
    Korisnik.load()
    Film.load()
    Sala.load()
    bioskoska_projekcija.load()
    Termin.load()
    Termin.generate_term()
def Exit():
    Korisnik.save()
    Film.save()
    Sala.save()
    bioskoska_projekcija.save()
    Termin.save()
    return False 
def login(): 
    global loged_user
    while loged_user ==  None:
        username = input("Unesi korisnicko ime ")
        if username == "X":
            return True
        password = input("Unesi lozinku ")
        loged = Korisnik.login(username, password)
        if loged !=  None:
            loged_user = loged
    return True
def registruj():
    Korisnik.register()
    Korisnik.save()
    return True        
def logout():
    global loged_user
    loged_user = None
    return True
def izmani_podatke():
    global loged_user
    loged_user = Korisnik.edit_profile(loged_user)
    Korisnik.save()
    return True
def pregled_filma():
    Film.print_movies()
    return True
def pretraga_filma1():
    Film.pretraga_filmova()
    return True
def pretraga_filmova2():
    print("Unesite brojeve koje zelite da pretrazite razdvojene razmakom")
    Film.pretraga_filmova()
    return True
def register_seller():
    Korisnik.create_seller()
    return True
def register_manager():
    Korisnik.create_manager()
    return True
def delete_movie():
    Film.delete()
    return True
def pregled_termina():
    Termin.search_terms()
    return True
def add_movie():
    Film.add_movie()
    return True
def edit_movie():
    Film.edit_movie()
    bioskoska_projekcija.save()
    bioskoska_projekcija.load()
    Termin.save()
    Termin.load()
    return True
def delete_movie():
    Film.delete()
    bioskoska_projekcija.save()
    bioskoska_projekcija.load()
    Termin.save()
    Termin.load()
    
    return True
def add_projection():
    bioskoska_projekcija.add_projection()
    Termin.generate_term()
    return True
def delete_projection():
    bioskoska_projekcija.delete()
    return True
def edit_projection():
    bioskoska_projekcija.edit()
    return True
def print_menu_not_loged():
    print("Ukucajte 1 ukoliko zelite da se prijavite")
    print("Ukucajte 2 ukoliko zelite da pregledate dostupne termine")
    print("Ukucajte 3 ukoliko zelite da pretrazite dostupne filmova ")
    print("Ukucajte 4 ukoliko zelite da pretrazite dostupne filmove po 1 stavci")
    print("Ukucajte 5 ukoliko zelite da pretrazite filmoce po vise stavki")
    print("Ukucajte 6 ukoliko zelite da se registrujete")
    print("Ukucajte X ukoliko zelite da izadjete iz aplikacije")
def print_menu_loged():
    print("Ukucajte 1 ukoliko zelite da se odjavite")
    print("Ukucajte 2 ukoliko zelite da pregledate dostupne termine")
    print("Ukucajte 3 ukoliko zelite da pretrazite dostupne filmova ")
    print("Ukucajte 4 ukoliko zelite da pretrazite dostupne filmove po 1 stavci")
    print("Ukucajte 5 ukoliko zelite da pretrazite filmoce po vise stavki")
    print("Ukucajte 6 ukoliko zelite da se izmenite podatke o nalogu")
    print("Ukucajte X ukoliko zelite da izadjete iz aplikacije")
    pass
def print_menu_loged_meneager():
    print("Ukucajte 1 ukoliko zelite da se odjavite")
    print("Ukucajte 2 ukoliko zelite da pregledate dostupne termine")
    print("Ukucajte 3 ukoliko zelite da pretrazite dostupne filmova ")
    print("Ukucajte 4 ukoliko zelite da pretrazite dostupne filmove po 1 stavci")
    print("Ukucajte 5 ukoliko zelite da pretrazite filmoce po vise stavki")
    print("Ukucajte 6 ukoliko zelite da se izmenite podatke o nalogu")
    print("Ukucajte 7 ukoliko zelite da registrujete novog prodavca")
    print("Ukucajte 8 ukoliko zelite da registrujete novog menadjra")
    print("Ukucajte 9 ukoliko zelite da dodate novi film")
    print("Ukucajte 10 ukoliko zelite da obrisete postojeci film")
    print("Ukucajte 11 izmenite postojeci film")
    print("Ujucajte 12 ako zelite da dodate novu projekciju")
    print("Ukucajte 13 ako zelite da obrisete projekciju")
    print("Ukucajte 14 ako zelite da izmenite projekciju")
    print("Ukucajte X ukoliko zelite da izadjete iz aplikacije")


menu_not_loged = {"1" : login, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":registruj, "X": Exit}
menu_loged= {"1" : logout, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":izmani_podatke, "X": Exit}
menu_loged_meneager = {"1" : logout, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":izmani_podatke, "7": register_seller, "8": register_manager, "9":add_movie,  "11" : edit_movie, "10": delete_movie,"12":add_projection,"13":delete_projection, "14": edit_projection, "X": Exit}
menu_loged_seller = {}
