import modules.cards as cards
import datetime
import modules.PrintTabel as PrintTabel

def validate_date(unos):
    try:
        unos = datetime.datetime.strptime(unos,'%Y-%m-%d')
        return True
    except:
        print("Vreme mora da bude u formatu godina-mesec-dan")
        return False

def chose_report():
    izvestaji = {"a": cards_sold_day, "b": cards_projection_day, "c":cars_sold_by_seller, "d":card_by_week_day,
                 "e":sold_cards_in_week_day_projection, "f":sold_card_for_movie, "g": sold_cards_by_seller, "h": sold_cards_by_all_sellers}
    while True:
        print("Ukoliko zelite lista prodatih karata za odabran datum prodaje ukucajte a")
        print("Ukoliko zelite Lista prodatih karata za odabran datum termina bioskopske projekcije ukucajte b")
        print("Ukoliko zelite Lista prodatih karata za odabran datum prodaje i odabranog prodavca ukucajte c")
        print("Ukoliko zelite Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje d")
        print("Ukoliko zelite Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije ukucajte e")
        print("Ukoliko zelite Ukupna cena prodatih karata za zadati film u svim projekcijama ukucajte f")
        print("Ukoliko zeliteUkupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca ukucajte g")
        print("Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakog prodavca) u poslednjih 30 dana. ukucajte h")
        print("Unesi X ako zelis da izadjes")
        user_input = input("Unesi zeljeni izvestaj ")
        if user_input in izvestaji.keys():
            data = izvestaji[user_input]()
            save_report = input("Ukucaj DA ukoliko zelis da sacuvas izvestaj ")
            if save_report == "DA":
                file_name = user_input + "\\"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                file = open("reports\\" + file_name + ".txt", "x")
                file.close()
                file = open("reports\\" + file_name + ".txt","a",encoding="utf-8")
                PrintTabel.prepare_for_printing(data, file.write)
                file.close()
        elif user_input == "X":
            return 
        else:
            print("Uneli ste ne postojeci izvestaj pokusajte ponovo")





def cards_projection_day():
     code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date, projection = cards.input_for_search(["3"])
     type_card = "2"
     data_for_print = cards.print_cards(code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, sale_date, type_card)
     for i in range(len(data_for_print)):
         data_for_print[i] = data_for_print[i].to_list()   
     return data_for_print 
def cards_sold_day():
    code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date,projection = cards.input_for_search(["7"])
    type_card = "2"
    data_for_print = cards.print_cards(code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, sale_date, type_card)      
    for i in range(len(data_for_print)):
        data_for_print[i] = data_for_print[i].to_list()
    return data_for_print
def cars_sold_by_seller():
    code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date, projection = cards.input_for_search(["7"])
    type_card = "2"
    card_ids = cards.print_cards(code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, sale_date, type_card,printing= False)      
    all_sellers = cards.Korisnik.print_all_users(type_of_user= 2)
    saller = ""
    while saller not in all_sellers:
        saller = input("Unesi username prodavca ")
    saller = cards.Korisnik.get_by_username(saller)
    list_for_print = []
    for card in card_ids:
        if card.seller == saller:
            data_for_print  = card.to_list()
            data_for_print.append(str(card.price))
            list_for_print.append(data_for_print)
    PrintTabel.prepare_for_printing(list_for_print)
    return list_for_print
def card_by_week_day():
    date_week = ""
    dates = {"pon": 0, "uto" : 1, "sre" : 2,"cet" : 3,"pet":4,"sub":5, "ned":6}
    while not date_week in dates.keys():
        date_week = input("Unesi dan u nedelji kao pon, uto, sre, cet, pet, sub, ned ")
    cards_ids = cards.print_cards(printing= False, type= "2")
    printing_data = [[date_week,"" , ""]]
    number = 0
    price = 0
    for card in cards_ids:
        if datetime.datetime.weekday(card.term.date) == dates[date_week]:
            number += 1
            price += card.price
    printing_data[0][1] = str(number)
    printing_data[0][2] = str(price)
    PrintTabel.prepare_for_printing(printing_data)
    return printing_data
def sold_cards_in_week_day_projection():
    code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date,projection = cards.input_for_search(["8"])
    type_card = "2"
    cards_ids = cards.print_cards(code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, sale_date, type_card,projection=projection, printing= False)  
    date_week = ""
    dates = {"pon": 0, "uto" : 1, "sre" : 2,"cet" : 3,"pet":4,"sub":5, "ned":6}
    while not date_week in dates.keys():
        date_week = input("Unesi dan u nedelji kao pon, uto, sre, cet, pet, sub, ned ")
    printing_data = [[projection.code, date_week, "" , ""]]
    number = 0
    price = 0
    for card in cards_ids:
        if datetime.datetime.weekday(card.term.date) == dates[date_week]:
            number += 1
            price += card.price
    printing_data[0][2] = str(number)
    printing_data[0][3] = str(price)
    PrintTabel.prepare_for_printing(printing_data)
    return printing_data
def sold_card_for_movie():
    cards_ids = cards.print_cards(type="2",printing=False)
    cards.Termin.bioskoska_projekcija.Film.print_movies()
    movie = ""
    while not cards.Termin.bioskoska_projekcija.Film.check(movie):
        movie = input("Unesi ime filma")
    movie = cards.Termin.bioskoska_projekcija.Film.get_movie(movie)
    printing_data = [[movie.name,"" , ""]]
    number = 0
    price = 0
    for card in cards_ids:
        if card.term.projection.movie == movie:
            number += 1
            price += card.price
    printing_data[0][1] = str(number)
    printing_data[0][2] = str(price)
    PrintTabel.prepare_for_printing(printing_data)
    return printing_data
def sold_cards_by_seller():
    code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, type_card, sale_date, projection = cards.input_for_search(["7"])
    type_card = "2"
    card_ids = cards.print_cards(code, name, date, start_time_first, start_time_second, end_time_first, end_time_second, sale_date, type_card,printing= False)      
    all_sellers = cards.Korisnik.print_all_users(type_of_user= 2)
    saller = ""
    while saller not in all_sellers:
        saller = input("Unesi username prodavca ")
    saller = cards.Korisnik.get_by_username(saller)
    list_for_print = [[saller.username,"",""]]
    number = 0
    price = 0
    for card in card_ids:
        if card.seller == saller:
            number += 1
            price += card.price
    list_for_print[0][1] = str(number)
    list_for_print[0][2] = str(price)
    PrintTabel.prepare_for_printing(list_for_print)
    return list_for_print
def sold_cards_by_all_sellers():
    type_card = "2"
    card_ids = cards.print_cards (type = type_card,printing= False)      
    all_sellers = cards.Korisnik.print_all_users(type_of_user= 2, printing=False)
    price_seller = {}
    number_seller = {}
    for seller in all_sellers:
        price_seller[seller] = 0
        number_seller[seller] = 0
    for card in card_ids:
        if datetime.datetime.now() - card.date < datetime.timedelta(days=30):
            price_seller[card.seller.username] += card.price
            number_seller[card.seller.username] += 1
    data_for_print = []
    for key in price_seller.keys():
        values = [key, str(price_seller[key]),  str(number_seller[key])]
        data_for_print.append(values)
    PrintTabel.prepare_for_printing(data_for_print)
    return data_for_print