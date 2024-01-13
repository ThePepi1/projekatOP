import modules.user as user
import modules.terms as terms
import modules.PrintTabel as PrintTabel 
import datetime
class Cards:
    def __init__(self,id,username, term, seat_signed,type, seller,date,price):
        self.id = id
        self.username = username
        self.term = term
        self.seat = seat_signed
        self.type = type
        self.seller = seller
        self.date = date
        self.price = price
    def to_string(self):
        if isinstance(self.username,user.Korisnik):
            username = self.username.username
        else:
            username = self.username
        if isinstance(self.seller,user.Korisnik):
            seller = self.seller.username
        else:
            seller = self.seller
        
        if isinstance(self.term,terms.Term):
           term = self.term.code
        else:
            term = self.term

        return f"{self.id}|{username}|{term}|{self.seat}|{self.type}|{seller}|{self.date.strftime('%Y-%m-%d %H:%M:%S')}|{self.price}|{isinstance(self.username,user.Korisnik)}\n"
    def to_list(self):
        if isinstance(self.username,user.Korisnik):
            username = self.username.username
        else:
            username = self.username
        if self.type == "1":
            type = "rezervisana"
        else:
            type = "prodata"
        return[self.id,self.term.code,username, self.term.projection.movie.name,self.term.start_time().strftime('%Y-%m-%d %H:%M:%S'), self.term.end_time().strftime('%Y-%m-%d %H:%M:%S'),self.seat,type]
    def set_term(self, term):
        self.term = term
    def set_seat(self, seat):
        self.seat = seat
    def set_username(self,username):
        self.username = username
cards =  {}
def get_empty_seats(term_user):
    seats = terms.projection.hall.generate_seats(term_user.projection.hall)
    for card in cards.values():
        if card.term == term_user:
            for row in seats:
                for i in range(len(row)):
                    if row[i] == card.seat:
                        row[i] = "Z"
    return seats
def check_seat(seat, available_cards):
    if seat == "Z":
        return False
    
    for cards in available_cards:
        if seat in cards:
            return True
    return False

def reserve_card_for_self(user):
    who = user
    terms.print_terms()
    term_user = input("Unesi zeljeni id termina: ")
    while not terms.check_active_exsistence(term_user):
        print("Termin ne postoji ukoliko zelite da izadjete ukucajte X ili pokusajte da ukucate jos jedan termin")
        term_user = input("Unesi id zeljenog termina ")
        if term_user == "X":
            return None
    term_user = terms.get_term(term_user)
    available_cards = get_empty_seats(term_user)
    PrintTabel.prepare_for_printing(available_cards)
    seat = " "
    while not check_seat(seat, available_cards):
        seat = input("Unesi zeljeno sediste: ")
        if seat == "X":
            return None
    id = 1
    if len(cards) != 0:
        while str(id) in cards.keys():
            id = 1 + id
    cards[str(id)] = Cards(str(id),who,term_user,seat,"1",None,datetime.datetime.now(),0)
    return cards[str(id)]
def load():
    file = open("data\\cards.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            cards[line[0]] = Cards(line[0],user.get_by_username(line[1],line[8]),terms.get_term(line[2]),line[3],line[4],user.get_by_username(line[5],""),datetime.datetime.strptime(line[6],'%Y-%m-%d %H:%M:%S'),int(line[7]))
    file.close() 
def save():
    file = open("data\\cards.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\cards.txt","a",encoding="utf-8")
    for card in cards.values():
        file.write(card.to_string())
    file.close()
def effect_on_change(term):
    cards_for_delete = []
    for card in cards.values():
        if card.term == term:
                cards_for_delete.append(card.id)
    for uid in cards_for_delete:
        cards.pop(uid)
def print_all_cards():
    cards_ids = []
    cards = print_cards()
    for card in cards:
        cards_ids.append(card.id)
    return cards_ids
def print_all_reserved_cards():
    cards = print_cards(type= "1")
    list_of_ids = []
    for card in cards:
        list_of_ids.append(card.id)
    return list_of_ids
def print_users_cards(user):
    print_cards(name = user)
def print_reserved_cards(user):
    cards_ids = []
    cards = print_cards(name = user, type = "1")
    for card in cards:
        cards_ids.append(card.id)
    return cards_ids
def delete_it(id):
    cards.pop(id)
def change_card():
    cards_id = print_all_cards()
    user_input = input("Unesi kod rezervacije koju menjaš ")
    while not user_input in cards_id:
        user_input = input("Unesi kod rezervacije koju menjaš ")
        if user_input == "X":
            return 
    card_id = user_input
    while True:
        print("Ukoliko zelis da izmenis termin ukucaj 1")
        print("Ukoliko zelis izmenis korisnicko ime ili ime i prezime ukucaj 2")
        print("Ukoliko zelis da izmenis sediste u sali unesi 3")
        print("Ukoliko zelis da prekines ukucaj X")
        user_input = input("Unesi broj ")
        if user_input == "1":
            terms.print_terms()
            term_user = input("Unesi zeljeni id termina: ")
            while not terms.check_active_exsistence(term_user):
                term_user = input("Unesi id zeljene projekcije")
                if term_user == "X":
                    break
            if term_user != "X":
                cards[card_id].set_term(terms.get_term(term_user))
                user_input = "3"
         
        if user_input == "2":
            print("Ukoliko zelite da promenite u registrovanog korisnika ukucajte 1, ako ocete da promenite u neregistrovanog ukucajte 2")
            user_type = input("Vrsta: ")
            if user_type == "1":
                data_username = user.print_all_users()
            user_name =""
            while True:
                user_name = input("Unesi korisnocko ime za kartu ")
                if user_name == "X":
                    break
                if user_type == "1":
                    if user_name in  data_username:
                        user_name = user.get_by_username(user_name)
                        break
                elif user_type == "2":
                    if user.check_every_input(user_name):
                        break
            if user_name != "X": 
                cards[card_id].set_username(user_name)
        if user_input == "3":
            term_user = cards[card_id].term
            available_cards = get_empty_seats(term_user)
            PrintTabel.prepare_for_printing(available_cards)
            seat = " "
            while not check_seat(seat, available_cards):
                seat = input("Unesi zeljeno sediste: ")
                if seat == "X":
                    break
            if seat != "X":
                cards[card_id].set_seat(seat)
        if user_input == "X":
            return 
def price_calc(term, user_name):
    sum = 0
    price = term.projection.price
    if datetime.datetime.weekday(term.date) == 1:
        price = price - 50
    for card in cards.values():
        if isinstance(card.username, user.Korisnik):
            if card.username == user_name:
                if card.date > datetime.datetime.now() - datetime.timedelta(days=365):
                    sum = sum + card.price
    if sum >  5000:
          price = price * 0.9
    if datetime.datetime.weekday(term.date) == 6 or datetime.datetime.weekday(term.date) == 5:
        price = price + 50
    return int(price)
def sold_reserved(id,seller):
    cards[id].type = "2"
    cards[id].date = datetime.datetime.now()
    cards[id].price = price_calc(cards[id].term,cards[id].username )
    cards[id].seller = seller
def print_cards(name= "", projection_code= "", date_term = "" , start_time_term_first = "", start_time_term_second="", end_time_term_first="", end_time_term_second ="",  sale_date = "", type = "",projection = "", printing=True,):
    list_of_cards = []
    list_for_print = []
    for card in cards.values():
        if check(card,name,projection_code, date_term, start_time_term_first, start_time_term_second, end_time_term_first, end_time_term_second,  sale_date, type,projection):
            list_of_cards.append(card)
            list_for_print.append(card.to_list())
    if printing:
        PrintTabel.prepare_for_printing(list_for_print)
    return list_of_cards
def check(card,name,projection_code, date_term, start_time_term_first, start_time_term_second, end_time_term_first, end_time_term_second, sale_date, type,projection): 
    start_time = card.term.start_time()
    end_time = card.term.end_time()
    date = card.term.date
    date_of_sale = card.date.date()
    type_of_card = card.type
    date_of_term = card.term.date
    code = card.term.projection.code
    if name != "":
        if name != card.username:
            return False    
    if start_time_term_first != "":
        if start_time.time()  < start_time_term_first:
            return False
    if start_time_term_second != "":
        if start_time.time() > start_time_term_second:
            return False
    if end_time_term_first !=  "":
        if end_time.time()  < end_time_term_first:
            return False
    if end_time_term_second != "":
        if end_time.time() > end_time_term_second:
            return False
    if date_term != "":
        if date != date_term:
            return False
    if projection_code != "":
        if code != projection_code:
            return False
    if date_term != "":
        if date_term != date_of_term:
            return False
    if sale_date != "":
        if sale_date != date_of_sale:
            return False
    if date_term != "":
        if date_term != date_of_term:
            return False
    if type != "":
        if type != type_of_card:
            return False
    if projection != "":
        if projection != card.term.projection:
            return False
    return True
def search_cards(printing = True):
    print("Unesi 1 ukoliko želiš da pretražiš karte po sifri porjekcije ")
    print("Unesi 2 ukoliko želiš da pretražiš karte po imenu prezimenu ili korisnickom imenu za registrovane korisnike")
    print("Unesi 3 ukoliko želiš da pretražiš karte po datumu termina ")
    print("Unesi 4 ukoliko želiš da pretražiš katrt po vremenu početka ")
    print("Unesi 5 ukoliko želiš da pretražiš katrt po vremenu kraja ")
    print("Ukucaj 6 ukoliko želiš da pretražiš karte po tome da li su prodate ili rezervisane")
    user_input = input()
    user_input = user_input.split(" ")
    code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date, projection = input_for_search(user_input)
    return print_cards(name, code, date,start_time_first, start_time_second, end_time_first, end_time_second,"", type_card, "", printing)
       
def input_for_search(user_input):
    code = ""
    if "1" in user_input:
        terms.projection.print_projections()
        code = input("Unesi kod projekcije po kojoj pretražuješ ")    
    name = ""
    if "2" in user_input:
        name = input("Unesi ime ili korisničko ime po kojem pretražujete ")
        is_it_looged = input("Unesi 1 ako ovo nije logovan kupac ")
        if is_it_looged == "1":
            is_it_looged = "False"
        name = user.get_by_username(name,is_it_looged)
    date = ""
    if "3" in user_input:
        while not terms.validate_date(date):
            date = input("Unesi datum: ")    
        date = datetime.datetime.strptime(date,'%Y-%m-%d').date()
    start_time_first = ""
    start_time_second = ""
    end_time_first = ""
    end_time_second = ""
    type_card = ""
    if "4" in user_input:
        start_time_first, start_time_second = input_time()
    if "5" in user_input:
        end_time_first, end_time_second = input_time()
    if "6" in user_input:
        type_card = input("Unesi 1 ukoliko zelis da pretrazis rezervisane karte, 2 ukoliko zelite da pretrazite prodate karte ")
    sale_date = ""
    if "7" in user_input:
        while not terms.validate_date(sale_date):
            sale_date = input("Unesi datum: ")    
        sale_date = datetime.datetime.strptime(sale_date,'%Y-%m-%d').date()
    projection_code = ""
    projection = ""
    if "8" in user_input:
        terms.projection.print_projections()
        while not terms.projection.check_code(projection_code):
            projection_code = input("unesi kod projekcije ")
        projection = terms.projection.get_projection(projection_code)
    return code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date, projection
def input_time():
    time_first = ""
    time_second = ""
    print("Ukoliko zelite da pretrazite sve termine pre odredjenog vremena ukucajte 1")
    print("Ukoliko zelite da pretrazite sve termine posle odredjenog vremena ukucajte 2")
    print("Ukoliko zelite da pretrazite sve termine u tacno vreme 3")
    print("Ukoliko zelite da pretrazite sve termine koji po dva vremena ukucajte 4")
    user_input = input()
    if user_input == "2" or user_input == "4":
        while not terms.projection.validate_time(time_first):
            time_first = input("Unesi vreme ")
        time_first = datetime.datetime.strptime(time_first,'%H:%M:%S').time()
    if user_input == "1" or user_input == "4":
        while not terms.projection.validate_time(time_second):
            time_second = input("Unesi vreme ")
        time_second = datetime.datetime.strptime(time_second,'%H:%M:%S').time()
    if user_input == "3":
        while not terms.projection.validate_time(time_first):
            time_first = input("Unesi vreme ")
        time_first = datetime.datetime.strptime(time_first,'%H:%M:%S').time()
        return time_first, time_first

    return time_first, time_second
def unreserve_cards():
    list_of_codes_for_dell = []
    for card in cards.values():
        if datetime.datetime.now() - datetime.timedelta(minutes=30) > card.term.start_time():
            if card.type == "1":
                list_of_codes_for_dell.append(card.id)
    for code in list_of_codes_for_dell:
        cards.pop(code)
#Type 1 is reserved cards and 2 is sold cards