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
    pass 




def cards_projection_day():
    date = ""
    while not validate_date(date):
        date = input("Unesi datum: ")
    date =  datetime.datetime.strptime(date,'%Y-%m-%d').date()
    list_of_cards = []
    PrintTabel.prepare_for_printing(list_of_cards)


def cards_sold_day():

    date = ""
    while not validate_date(date):
        date = input("Unesi datum: ")
    date =  datetime.datetime.strptime(date,'%Y-%m-%d').date()
    list_of_cards = []
    PrintTabel.prepare_for_printing(list_of_cards)

