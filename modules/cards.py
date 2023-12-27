import modules.Korisnik as Korisnik
import modules.Termin as Termin
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
        if isinstance(self.username,Korisnik.Korisnik):
            username = self.username.username
        else:
            username = self.username
        if isinstance(self.seller,Korisnik.Korisnik):
            seller = self.seller.username
        else:
            seller = self.seller
        
        if isinstance(self.term,Termin.Term):
           term = self.term.code
        else:
            term = self.term

        return f"{self.id}|{username}|{term}|{self.seat}|{self.type}|{seller}|{self.date.strftime('%Y-%m-%d %H:%M:%S')}|{self.price}\n"
    def to_list(self):
        if isinstance(self.username,Korisnik.Korisnik):
            username = self.username.name + " "+self.username.lastname
        else:
            username = self.username
        if self.type == "1":
            type = "rezervisana"
        else:
            type = "prodata"
        return[self.id,self.term.code,username, self.term.projection.movie.name,self.term.start_time().strftime('%Y-%m-%d %H:%M:%S'), self.term.end_time().strftime('%Y-%m-%d %H:%M:%S'),self.seat,type]

cards =  {}
def get_empty_seats(term_user):
    seats = Termin.bioskoska_projekcija.Sala.generate_seats(term_user.projection.hall)
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
    Termin.print_terms()
    term_user = input("Unesi zeljeni id termina: ")
    while not Termin.check_active_exsistence(term_user):
        term_user = input("Unesi id zeljene projekcije")
        if term_user == "X":
            return
    term_user = Termin.get_term(term_user)
    available_cards = get_empty_seats(term_user)
    PrintTabel.prepare_for_printing(available_cards)
    seat = " "
    while not check_seat(seat, available_cards):
        seat = input("Unesi zeljeno sediste: ")
        if seat == "X":
            return
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
            cards[line[0]] = Cards(line[0],Korisnik.get_by_username(line[1]),Termin.get_term(line[2]),line[3],line[4],Korisnik.get_by_username(line[5]),datetime.datetime.strptime(line[6],'%Y-%m-%d %H:%M:%S'),int(line[7]))
    file.close() 
def save():
    file = open("data\\cards.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\cards.txt","a",encoding="utf-8")
    for card in cards.values():
        file.write(card.to_string())
    file.close()
#Type 1 is reserved cards and 2 is sold cards
def effect_on_change(term):
    cards_for_delete = []
    for card in cards.values():
        if card.term == term:
                cards_for_delete.append(card.id)
    for uid in cards_for_delete:
        cards.pop(uid)
def print_all_cards():
    list_card = []
    cards_id = []
    for card in cards.values():
        list_card.append(card.to_list())
        cards_id.append(card.id)
    PrintTabel.prepare_for_printing(list_card)
    return cards_id
def print_all_reserved_cards():
    list_card = []
    cards_id = []
    for card in cards.values():
        if card.type == "1":
            list_card.append(card.to_list())
            cards_id.append(card.id)
    PrintTabel.prepare_for_printing(list_card)
    return cards_id
def print_users_cards(user):
    list_card= []
    for card in cards.values():
        if card.username == user:
            list_card.append(card.to_list())
    PrintTabel.prepare_for_printing(list_card)
def print_reserved_cards(user):
    list_card= []
    cards_ids = []
    for card in cards.values():
        if card.username == user and card.type == "1":
            list_card.append(card.to_list())
            cards_ids.append(card.id)
    PrintTabel.prepare_for_printing(list_card)  
    return cards_ids
def delete_it(id):
    cards.pop(id)
def change_card():
    cards_id = cards.print_all_cards()
    user_input = input("Unesi kod rezervacije koju menjaš ")
    while not user_input in cards_id:
        user_input = input("Unesi kod rezervacije koju menjaš ")
        if user_input == "X":
            return True


def price_calc(term, user):
    sum = 0
    price = term.price
    if datetime.datetime.weekday(term.date) == 1:
        price = price - 50
    for card in cards.values():
        if isinstance(card.username, Korisnik.Korisnik):
            if card.username == user:
                if card.date > datetime.datetime.now() - datetime.timedelta(days=365):
                    sum = sum + card.price
    if sum >  5000:
          price = price * 0.9
    if datetime.datetime.weekday(term.date) == 6 or datetime.datetime.weekday(term.date) == 5:
        price = price + 50
    return price
def sold_reserved(id,seller):
    cards[id].type = "2"
    cards[id].date = datetime.datetime.now()
    cards[id].price = price_calc(cards[id].term,cards[id].username )
    cards[id].seller = seller

def search_cards(name= "", projection_code= "", date_term = "" , start_time_term = "",end_time_term ="",  sale_date = "", type = ""):
    list_of_cards = []
    list_for_print = []
    for card in cards.values():
        if check(card,name,projection_code, date_term, start_time_term, end_time_term,  sale_date, type):
            list_of_cards.append(card)
            list_for_print.append(card.to_list())

def check(card,name,projection_code, date_term, start_time_term, end_time_term, sale_date, type): 
    pass














def unreserve_cards():
    list_of_codes_for_dell = []
    for card in cards.values():
        if datetime.datetime.now() - card.term.start_time() < datetime.timedelta(minutes=30):
            print(card.id, card.type)
            if card.type == "1":
                list_of_codes_for_dell.append(card.id)
    print(list_of_codes_for_dell)
    for code in list_of_codes_for_dell:
        cards.pop(code)
    print(cards.values())