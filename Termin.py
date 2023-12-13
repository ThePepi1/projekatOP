import bioskoska_projekcija
import datetime
from random import randrange
dates = ["pon","uto","sre","cet","pet","sub","ned"]
class Term:
    def __init__(self,code,date,active):
        self.code = code
        self.date = date
        self.projection = bioskoska_projekcija.get_projection(code[:4])
        self.active = active
    def to_string(self):
        return f"{self.code}|{self.date}|{self.active}\n"
terms = {}
def check_existence(code, day):
    for term in terms.values():
        if term.code[:4] == code and term.date == day:
            return True
    return False
def generate_term():
    day = datetime.datetime.now().date()
    for i in range(14):
        list_of_codes = bioskoska_projekcija.get_by_day(dates[datetime.date.weekday(day)])  
        for code in list_of_codes:
            if not check_existence(code,day):
                first_letter = chr(randrange(65,90))
                second_letter = chr(randrange(65,90))
                while code + first_letter + second_letter in terms.keys(): 
                    first_letter = chr(randrange(65,90))
                    second_letter = chr(randrange(65,90))
                terms[code+first_letter+second_letter] = Term(code+first_letter+second_letter,day,True)  

        day = day + datetime.timedelta(days=1)
                

def load():
    file = open("data\\termini.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            if line != "":
                line = line.split("|")
                day = datetime.datetime.strptime(line[1],"%Y-%m-%d")
                terms[line[0]] = Term(line[0],day.date(),bool(line[2]))
    file.close() 
def save():
    file = open("data\\termini.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\termini.txt","a",encoding="utf-8")
    for term in terms.values():
        file.write(term.to_string())
    file.close()

def search_terms():
    print("Ukoliko hocete da pretrazite termine po filmu ukucajte 1")
    print("Ukoliko hocete da pretrazite termine po sali ukucajte 2")
    print("Ukoliko hocete da pretrazite termine po datumu ukucajte 3")
    print("Ukoliko hocete da pretrazite termine po pocetku projekcije ukucajte 4")
    print("Ukoliko hocete da pretrazite termine po kraju projekcije ukucajte 5")
    user_input = input()
    user_input = user_input.split(", ")
    movies = []
    halls = ""
    start_time = ""
    end_time = ""
    date = ""
    if '1' in user_input:
        movies = bioskoska_projekcija.Film.pretraga_filmova(False)
    elif '2' in user_input:
        pass
    elif '3' in user_input:
        pass
    elif '4' in user_input:
        pass
    elif '5' in user_input:
        pass
    



