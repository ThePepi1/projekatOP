import Korisnik
import Film
import bioskoska_projekcija
import Sala
import Termin
loged_user = None
def create_menu():
    pass


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
menu_not_loged = {}
menu_loged= {}
menu_loged_meneager = {}
menu_loged_seller = {}

Film.load()
Sala.load()
bioskoska_projekcija.load()
print(bioskoska_projekcija.projections)
bioskoska_projekcija.save()