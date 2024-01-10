import modules.projection as projection
import datetime
from random import randrange
import modules.PrintTabel as PrintTabel
from modules.cards import effect_on_change
dates = ["pon","uto","sre","cet","pet","sub","ned"]
class Term:
    def __init__(self,code,date,active):
        self.code = code
        self.date = date
        self.projection = projection.get_projection(code[:4])
        self.active = active
    def to_string(self):
        return f"{self.code}|{self.date}|{self.active}\n"
    def to_list(self):
        return [self.code, self.projection.hall.hall_code,self.projection.movie.name,self.date.strftime('%Y-%m-%d'),self.projection.start_time.strftime('%H:%M:%S'),self.projection.end_time.strftime('%H:%M:%S')]
    def start_time(self):
        return datetime.datetime.combine(self.date,self.projection.start_time.time())
    def end_time(self):
        return datetime.datetime.combine(self.date,self.projection.start_time.time()) + datetime.timedelta(minutes= self.projection.movie.lenght) # radim ovo da bi dobio novi dan(posto cuvam end time a on je posle 24h pa ispada da je prvo poceo film pa se onda zavrsio)




terms = {}
def check_existence(code, day):
    for term in terms.values():
        if term.code[:4] == code and term.date == day:
            return True
    return False
def generate_term():
    day = datetime.datetime.now()
    day_date = day.date()
    for i in range(14):
        list_of_codes = projection.get_by_day_active(dates[datetime.date.weekday(day_date)])  
        for code in list_of_codes:
            if not check_existence(code,day_date):
                if not check_pass(code, day_date):
                    first_letter = chr(randrange(65,90))
                    second_letter = chr(randrange(65,90))
                    while code + first_letter + second_letter in terms.keys(): 
                        first_letter = chr(randrange(65,90))
                        second_letter = chr(randrange(65,90))
                    terms[code+first_letter+second_letter] = Term(code+first_letter+second_letter,day_date,True)  
                    
        day_date = day_date + datetime.timedelta(days=1)

    check_active()
def validate_date(date):              
    try:
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
        return True
    except:
        print("Vreme mora da bude u formatu godina-mesec-dan")
        return False
def load():
    file = open("data\\termini.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            if line != "":
                line = line.split("|")
                day = datetime.datetime.strptime(line[1],"%Y-%m-%d")
                terms[line[0]] = Term(line[0],day.date(),line[2] == "True")
    check_active()
    file.close() 
def save():
    file = open("data\\termini.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\termini.txt","a",encoding="utf-8")
    for term in terms.values():
        file.write(term.to_string())
    file.close()
def check_active():
    today = datetime.datetime.now()
    for term in terms.values():
        if term.date < today.date():
            term.active = False
            continue
        if term.date == today.date():
            if term.projection.start_time.time() < today.time():
                term.active = False
                continue
def check_pass(code, day):
    today = datetime.datetime.now()
    start_time = projection.get_projection(code).start_time
    if today.date() == day:
        return start_time.time() < today.time() 
    return False
def effection(projection):
    check_active()
    terms_for_delete = []
    for term in terms.values():
        if term.projection.code == projection.code and term.active:
            terms_for_delete.append(term.code)
    for code in terms_for_delete:
        effect_on_change(terms[code])
        terms.pop(code)
def effection_change_code(projection,code):
    for term in terms.values():
        if not term.active:
            if term.projection.code == code:
                firs_letter = term.code[-1]
                second_letter = term.code[-2]
                code = projection.code + firs_letter +  second_letter
                term.code = code
                term.projection = projection
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
        projection.movie.print_movies()
        movies = projection.movie.pretraga_filmova(False)
    elif '2' in user_input:
        projection.hall.print_halls()
        halls = input("Unesite sale za koje zelite da pretrazite termine ")
    elif '3' in user_input:
        while not validate_date(date):
            date = input("Unesi datum za koje zelite da pretrazite ")
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
    elif '4' in user_input:
        while not projection.validate_time(start_time):
            start_time = input("Unesi datum za koje zelite da pretrazite ")
        start_time = datetime.datetime.strptime(start_time,'%H:%M:%S')
    elif '5' in user_input:
        while not projection.validate_time(end_time):
            end_time = input("Unesi datum za koje zelite da pretrazite ")
        end_time = datetime.datetime.strptime(end_time,'%H:%M:%S')
    print_terms(movies,halls,date,start_time,end_time)
def print_terms(movies = [], halls = "", date = "", start_time = "", end_time = ""): 
    terms_for_print = []
    for term in terms.values():
        if term.active:
            if not movies == []:
                if not term.projection.movie in movies:
                    continue
            if not halls == "":
                if not term.projection.hall.hall_code == halls:
                    continue
            if not date == "":
                if not date.date() == term.date:
                    continue
            if not start_time == "":
                if not start_time == term.projection.start_time:
                    continue
            if not end_time == "":
                if not end_time == term.projection.end_time:
                    continue
            terms_for_print.append(term.to_list())
            
    PrintTabel.prepare_for_printing(terms_for_print)
def get_term(term_id):
    if term_id in terms.keys():
        return terms[term_id]
def check_active_exsistence(term_id):
    if term_id in terms.keys():
        return terms[term_id].active
    return False 