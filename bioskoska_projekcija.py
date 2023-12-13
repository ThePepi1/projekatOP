import Film
import Sala
import datetime
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
    def to_string(self):
        return f"{self.code}|{self.hall.hall_code}|{self.start_time.strftime('%H:%M:%S')}|{self.end_time.strftime('%H:%M:%S')}|{','.join(self.dates)}|{self.movie.id}|{self.price}|{self.active}\n"    
projections = {}

def validate_date(date_Projections):
    dates = ['pon','uto','sre','cet','pet','sub','ned']
    
    if date_Projections == "":
        return False
    for i in date_Projections:
        if i in dates:
            dates.remove(i)
        else:
            return False 
    return True
def validate_code(code):
    if code in projections:
        return False
    if  not validate_input(code):
        return False
    if len(code) == 4:
        return True
    return False
def validate_input(name):
    if name == "":
        return False
    if "|" in name:
        return False
    return True
def validate_free_hall(hall, start_time,end_time,date):
    for projection in projections.values():
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
def validate_hall(hall):
    return Sala.check(hall)
def validate_number(number):
    return number.isdigit() 
def validate_movie(movie):
    return Film.check(movie)
def load():
    file = open("data\\bioskopske_projekcije.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            projections[line[0]] = Projection(line[0],Sala.gethall(line[1]),datetime.datetime.strptime(line[2],"%H:%M:%S"),datetime.datetime.strptime(line[3], "%H:%M:%S") ,line[4].split(","),Film.get_movie(line[5]),line[6],line[7] == "True")
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
    while not validate_code(code):
        code = input("unesi kod za projekciju ")
    hall_code = ""
    while not validate_hall(hall_code):
        hall_code = input("unesi kod sale ")
    hall = Sala.gethall(hall_code)
    start_time = ""
    end_time = ""
    date = ""
    while not validate_date(date):
        date = input("Unesi dane kojima se film prikazuje ")
        date = date.split(",")
    movie = ""
    while(not validate_movie(movie)):
        Film.print_movies()
        movie = input("Unesi id filma ")
    movie = Film.get_movie(movie)
    good_time = False
    free_hall = False
    while not (good_time and free_hall):
        start_time = input("unesi pocetno vreme  ")
        if start_time == "X":
            return
        if validate_time(start_time):
            start_time = datetime.datetime.strptime(start_time,'%H:%M:%S')
            end_time = start_time + datetime.timedelta(minutes=movie.lenght)
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
    projections[code] = Projection(code,hall,start_time,end_time,date,movie,price,True)
def get_projection(code):
    return projections[code]
def get_by_day(date):
    return_code = []
    for projection in projections.values():
        if date in projection.dates:
            return_code.append(projection.code)
    return return_code

#messeges for client
#delete and edit