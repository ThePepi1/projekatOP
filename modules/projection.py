import modules.movie as movie
import modules.hall as hall
import modules.PrintTabel as PrintTabel
import datetime
from modules.terms import effection , effection_change_code
class Projection:
    def __init__(self, code, hall, start_time, end_time, dates,movie,price,active):
        self.code = code
        self.hall = hall
        self.start_time = start_time
        self.end_time = end_time
        self.dates = dates
        self.movie = movie
        self.price = int(price)
        self.active = active
    def copy(self):
        code = self.code
        hall = self.hall
        start_time = self.start_time
        end_time = self.end_time
        dates = self.dates
        movie = self.movie
        price = self.price
        active = self.active
        return Projection(code, hall, start_time, end_time, dates,movie,price,active)
    def to_string(self):
        return f"{self.code}|{self.hall.hall_code}|{self.start_time.strftime('%H:%M:%S')}|{self.end_time.strftime('%H:%M:%S')}|{','.join(self.dates)}|{self.movie.id}|{self.price}|{self.active}\n"    
    def to_list(self):
        return [str(self.code), self.hall.hall_code, self.start_time.strftime('%H:%M:%S'),self.end_time.strftime('%H:%M:%S'),','.join(self.dates),self.movie.name,str(self.price)]

projections = {}

def validate_date(date_Projections):
    dates = ['pon','uto','sre','cet','pet','sub','ned']
    print("Dani se oznacavaju sa pon, uto, sre, cet, pet, sub, ned, i moraju biti odvojeni razmakom")
    if date_Projections == "":
        return False
    for i in date_Projections:
        if i in dates:
            dates.remove(i)
        else:
            return False 
    return True
def validate_code(code):
    if code in projections.keys():
        print("Kod je vec zauzet")
        return False
    if  not validate_input(code):
        print("Kod ne sme da sadrzi | i razmake")
        return False
    if len(code) == 4:
        return True
    print("Kod mora da bude duzine 4")
    return False
def validate_input(name):
    if name == "":
        return False
    if "|" in name:
        return False
    return True
def validate_free_hall(hall, start_time,end_time,date,projection_change = None):
    for projection in projections.values():
        if projection.active and projection != projection_change:
            if projection.hall == hall:
                if any(i in projection.dates for i in date):
                    lower = start_time < projection.start_time
                    lower = end_time < projection.start_time and lower
                    bigger = start_time > projection.end_time
                    bigger = start_time > projection.end_time and bigger
                    if not (lower or bigger):
                        return False 
    return True
def validate_time(time):
    try:
        date = datetime.datetime.strptime(time,'%H:%M:%S')
        return True
    except:
        print("Vreme mora da bude u formatu sati:minuti:sekunde")
        return False
def validate_hall(hall_code):
    return hall.check(hall_code)
def validate_number(number):
    return number.isdigit() 
def validate_movie(movie_id):
    return movie.check(movie_id)
def load():
    file = open("data\\bioskopske_projekcije.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            projections[line[0]] = Projection(line[0],hall.gethall(line[1]),datetime.datetime.strptime(line[2],"%H:%M:%S"),datetime.datetime.strptime(line[3], "%H:%M:%S") ,line[4].split(","),movie.get_movie(line[5]),line[6],line[7] == "True")
            projections[line[0]].active = projections[line[0]].movie.active and projections[line[0]].hall.active and projections[line[0]].active
    file.close() 
def save():
    file = open("data\\bioskopske_projekcije.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\bioskopske_projekcije.txt","a",encoding="utf-8")
    for projection in projections.values():
        file.write(projection.to_string())
    file.close()
def add_projection():
    code = ""
    print("Ukoliko u bilo kom trenutku zelita da prestanete sa ovom radnjom ukucajte X")
    while not validate_code(code):
        code = input("unesi kod za projekciju ")
        if code == "X":
            return
    hall_code = ""
    hall.print_halls()
    while not validate_hall(hall_code):
        hall_code = input("unesi kod sale ")
        if hall_code == "X":
            return
    hall_code = hall.gethall(hall_code)
    start_time = ""
    end_time = ""
    date = ""
    while not validate_date(date):
        date = input("Unesi dane kojima se film prikazuje ")
        if date == "X":
            return
        date = date.split(" ")
    movie_id = ""
    while(not validate_movie(movie_id)):
        movie.print_movies()
        movie_id = input("Unesi id filma ")
        if movie_id == "X":
            return
    movie_id = movie.get_movie(movie_id)
    good_time = False
    free_hall = False
    while not (good_time and free_hall):
        start_time = input("unesi pocetno vreme  ")
        if start_time == "X":
            return
        if validate_time(start_time):
            start_time = datetime.datetime.strptime(start_time,'%H:%M:%S')
            end_time = start_time + datetime.timedelta(minutes=movie_id.lenght)
            good_time = True
        if good_time:
            if validate_free_hall(hall,start_time,end_time,date):
                free_hall = True
            else:
                print("Sala je u tom terminu zauzeta pokusajte da unesete drugi termin ")
             
    price  = ""
    while not  validate_number(price):
        price = input("Unesi cenu kao broj ")
        if price == "X":
            return 
    projections[code] = Projection(code,hall_code,start_time,end_time,date,movie_id,price,True)
def get_projection(code):
    return projections[code]
def get_by_day(date):
    return_code = []
    for projection in projections.values():
        if date in projection.dates:
            return_code.append(projection.code)
    return return_code
def check_code(code):
    return code in projections.keys()

def get_by_day_active(date):
    return_code = []
    for projection in projections.values():
        if date in projection.dates and projection.active:
            return_code.append(projection.code)
    return return_code

def delete():
    print_projections()
    user_input = ""
    while not user_input in projections.keys():
        user_input = input("unesi kod projekcije koje zelis da obrises")
        if user_input == "X":
            return 
    projections[user_input].active = False
    effection(projections[user_input])
def edit():
    print_projections()
    user_input = ""
    while(user_input not in projections.keys()):
        user_input = input("Unesi kod projekcije koje zelite da izmenite ")
        if user_input == "X":
            return
    projection = projections[user_input]
    new_projection = projection.copy()
    movie = projection.movie
    hall= projection.hall
    date = projection.dates
    price = projection.price
    time = projection.start_time.strftime('%H:%M:%S')
    new_key = 1000
    while str(new_key) in projections.keys():
        new_key = new_key + 1
    print("Izaberite stavke koje zelite da izmenite kod projekcije ako ih ima vise razdvojite ih razmakom:")
    print("Ukoliko zelite da izmenite filmove prikazuje ukucajte 1")
    print("Ukoliko zelite da promenite salu ukucajte 2")
    print("Ukoliko zelite da promenite dane kojima se film pokazuje ukucajte 3")
    print("Ukoliko zelite da promenite cenu karte ukucajte 4")
    print("ukoliko zelite da izmenite pocetno vreme ukucajte 5")
    print("Ukoliko zelite da izadjete ukucajte X")        
    user_input = input("Unesi podatke koje zelis da izmenis ")
    if user_input == "X":
            return    
    user_input = user_input.split(" ") 
    if "1" in user_input:
        movie = ""
        while not validate_movie(movie):
            movie.print_movies()
            movie = input("Unesite film ")
            if movie == "X":
                movie = projection.movie.id
                break
        movie = movie.get_movie(movie)
    if "2" in user_input:
        hall = ""
        while not validate_hall(hall):
            hall.print_halls()
            hall = input("Unesi kod sale ")
            if hall == "X":
                hall = projection.hall.code
                break
        hall = hall.gethall(hall)
    if "3" in user_input:
        date = ""
        while not validate_date(date):
            date = input("Unesi dane kojima se prikazuje film ako ih je vise razdvojite ih zatezom i razmakom ")
            if date == "X":
                date = projection.date
                break
            date = date.split(", ")
    if "4" in user_input:
        price = ""
        while not validate_number(price):
            price = input("Unesi cenu karte ")
            if price == "X":
                price = projection.price
                break
    if "5" in user_input:
        time = ""
        while not validate_time(time):
            time = input("Unesi pocetno vreme ")
            if time == "X":
                time = projection.time.strftime('%H:%M:%S')
                break
    time = datetime.datetime.strptime(time,'%H:%M:%S')
    end_time = time + datetime.timedelta(minutes=movie.lenght)
    while not validate_free_hall(hall, time,end_time,date,projection):
            print("Sala je zauzeta u tom trenutku izaberite dal ce te da odustanete sa unosom X ili pokusate ponovo sa 3 promenom dana, 5 sa promenom vremena ili 2 promenom sale ")
            user = input("Unesi sledeci korak")
            if user == "3":
                date = ""
                while not validate_date(date):
                    date = input("Unesi dane kojima se prikazuje film ")
                    if date == "X":
                        return
                date = date.split(",")
            if user == "5":
                time = ""
                while not validate_time(time):
                    time = input("Unesi pocetno vreme ukoliko unesete X odma izlazite iz aplikacije")
                    if time == "X":
                        return
                time = datetime.datetime.strptime(time,'%H:%M:%S')
                end_time = time + datetime.timedelta(minutes=movie.lenght)
            if user == "2":
                hall = ""
                while not validate_hall(hall):
                    hall.print_halls()
                    hall = input("Unesi kod sale ")
                    if hall == "X":
                        hall = projection.hall
                        break
            if user == "X":
                return 
    projection.hall = hall
    projection.start_time = time
    projection.end_time = end_time
    projection.movie = movie
    projection.dates = date 
    projection.price = price
    print(projection.to_string())
    print(new_projection.to_string())
    if new_projection.to_string() != projection.to_string():
        new_projection.active = False
        new_projection.code = str(new_key)
        effection(projection)        
        
        effection_change_code(new_projection,projection.code)
        projections[str(new_key)] = new_projection
        
def effect(movie):
    for projection in projections.values():
        if projection.movie == movie:
            projection.active = False
            effection(projection)
def print_projections():
    projection_for_print = []
    for projection in projections.values(): 
        if projection.active:
            projection_for_print.append(projection.to_list())
    PrintTabel.prepare_for_printing(projection_for_print)






#messeges for client
#delete and edit
