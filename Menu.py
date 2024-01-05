import modules.Korisnik as Korisnik
import modules.Film as Film
import modules.bioskoska_projekcija as bioskoska_projekcija
import modules.Sala as Sala
import modules.Termin as Termin
import modules.cards as cards
import modules.reports as report
loged_user = None
def create_menu():
    if loged_user == None:
        print_menu_not_loged()
        return menu_not_loged
    if loged_user.type == 1:
        print_menu_loged()
        return menu_loged
    if loged_user.type == 2:
        print_menu_loged_seller()
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
    cards.load()
def Exit():
    Korisnik.save()
    Film.save()
    Sala.save()
    bioskoska_projekcija.save()
    Termin.save()
    cards.save()
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
    Termin.generate_term()
    return True
def edit_projection():
    bioskoska_projekcija.edit()
    Termin.generate_term()
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
    print("Ukucajte 7 ukoliko zelite da rezervišete kartu ")
    print("Ukucajte 8 ukoliko zelite da prikažete sve rezervisane karte ")
    print("Ukucajte 9 ukoliko zelite da obrišete rezervisanu kartu ")
    print("Ukucajte X ukoliko zelite da izadjete iz aplikacije")
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
    print("Ukucajte 15 ako zelite da vidite izvestaje")
    print("Ukucajte X ukoliko zelite da izadjete iz aplikacije")
def print_menu_loged_seller():
    print("Ukucajte 1 ukoliko zelite da se odjavite")
    print("Ukucajte 2 ukoliko zelite da pregledate dostupne termine")
    print("Ukucajte 3 ukoliko zelite da pretrazite dostupne filmova ")
    print("Ukucajte 4 ukoliko zelite da pretrazite dostupne filmove po 1 stavci")
    print("Ukucajte 5 ukoliko zelite da pretrazite filmoce po vise stavki")
    print("Ukucajte 6 ukoliko zelite da se izmenite podatke o nalogu")
    print("Ukucajte 7 ukoliko zelite da rezervišete kartu")
    print("Ukucajte 8 ukoliko zelite da ostampate sve karte")
    print("Ukucajte 9 ukoliko zelite da obrišete kartu")
    print("Ukucajte 10 ukoliko zelite da prodate rezervisanu kartu ")
    print("Ukucajte 11 ukoliko zelite da prodate ne rezervisanu kartu ")
    print("Ukucajte 12 ukoliko zelite da pretrazite kartu ")
    print("Ukucajte 13 ukoliko zelite da izmenite karte ")
    print("Ukucajte 14 ukoliko zelite da odrezervisite karte pola sata pre projekcije ")
    print("Ukucajte X ukoliko zelite da izadjete")

def reserve_card_for_self():
    while True:
        cards.reserve_card_for_self(loged_user)
        user_iput = input("Ukoliko zelite da rezervisete jos jednu kartu ukucajte Da ")
        if user_iput != "Da":
            return True
def register_card_for_registred():
    data_username = Korisnik.print_all_users()
    user_name =""
    while not user_name in data_username:
        user_name = input("Unesi korisnocko ime za kartu ")
        if user_name == "X":
            return 
    return cards.reserve_card_for_self(user_name)
def reserve_card_for_unregistered():
    user_name = ""
    while not Korisnik.check_every_input(user_name):
        user_name = input("Unesi ime za koje prodaješ kartu ona ne sme da ima | i ne moze da bude prazan string ")
    return cards.reserve_card_for_self(Korisnik.get_by_username(user_name,"False"))
def reserve_card_for_someone():
    while True:
        user_input = input("Ukoliko želite da rezervišete kartu za registrovanog kupca ukucajte 1 a ukoliko zelite da rezervišete kartu za ne registrovanopg kupca ukucajte 2 ili za odustajanje X")
        if user_input == '1':
            register_card_for_registred()
        elif user_input == '2':
            reserve_card_for_unregistered()
        elif user_input == 'X':
            return True
        else :
            print("Losa naredba")
            continue
        user_iput = input("Ukoliko zelite da rezervisete jos jednu kartu ukucajte Da ")
        if user_iput != "Da":
            return True
def print_all_cards():
    cards.print_all_cards()
    return True
def print_my_cards():
    cards.print_users_cards(loged_user)
    return True
def dell_reserved_cards():
    while True:
        cards_id = cards.print_reserved_cards(loged_user)
        user_input = input("Unesi kod rezervacije koju brišeš ")
        while not user_input in cards_id:
            user_input = input("Unesi kod rezervacije koju brišeš ")
            if user_input == "X":
                return True
        cards.delete_it(user_input)
        continue_user = input("Ukucaj Da ako zeliš da obrišeš još neku kartu ")
        if continue_user != "Da":
            return True
def dell_card():
    while True:
        cards_id = cards.print_all_cards()
        user_input = input("Unesi kod rezervacije koju brišeš ")
        while not user_input in cards_id:
            user_input = input("Unesi kod rezervacije koju brišeš ")
            if user_input == "X":
                return True
        cards.delete_it(user_input)
        continue_user = input("Ukucaj Da ako zeliš da obrišeš još neku kartu ")
        if continue_user != "Da":
            return True

def sell_reserved_card():
    cards_id = cards.print_all_reserved_cards()
    user_input = input("Unesi kod rezervacije koju prodaješ ")
    while not user_input in cards_id:
        user_input = input("Unesi kod rezervacije koju prodaješ ")
        if user_input == "X":
            return True
    cards.sold_reserved(user_input,loged_user)
    return True
def sell_direct():
    user_input = input("Ukoliko želite da prodate kartu za registrovanog kupca ukucajte 1 a ukoliko zelite da rezervišete kartu za ne registrovanopg kupca ukucajte 2 ")
    if user_input == '1':
        card = register_card_for_registred()
    elif user_input == '2':
        card = reserve_card_for_unregistered()
    cards.sold_reserved(card.id,loged_user)
    return True
def edit_cards():
    cards.change_card()
    return True
def search_cards():
    cards.search_cards()
    return True
def unreserve_cards():
    cards.unreserve_cards()
    return True
def report_chose():
    report.chose_report()
    return True
menu_not_loged = {"1" : login, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":registruj, "X": Exit}
menu_loged= {"1" : logout, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":izmani_podatke,"7":reserve_card_for_self, "8": print_my_cards,"9": dell_reserved_cards,  "X": Exit}
menu_loged_meneager = {"1" : logout, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":izmani_podatke, "7": register_seller, "8": register_manager, "9":add_movie,  "11" : edit_movie, "10": delete_movie,"12":add_projection,"13":delete_projection, "14": edit_projection,"15":report_chose,"X": Exit}
menu_loged_seller = {"1" : logout, "2": pregled_termina, "3":pregled_filma, "4":pretraga_filma1, "5": pretraga_filmova2, "6":izmani_podatke,"7":reserve_card_for_someone,"8": print_all_cards,"9": dell_card,"10": sell_reserved_card,"11": sell_direct,"12":search_cards ,"13": edit_cards,"14": unreserve_cards,"X": Exit} 
