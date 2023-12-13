import PrintTabel
class Sala:
    def __init__(self, hall_code,hall_name, hall_number_row, hall_signe_seat,active):
        self.hall_code = hall_code
        self.hall_name = hall_name
        self.hall_number_row = int(hall_number_row) 
        self.hall_signe_seat = int(hall_signe_seat)
        self.active = active
    def to_string(self):
        return f"{self.hall_code}|{self.hall_name}|{self.hall_number_row}|{self.hall_signe_seat}|{self.active}\n"    
    def to_list(self):
        return [self.hall_code, self.hall_name, str(self.hall_number_row), str(self.hall_signe_seat)]
halls = {}

def validate_input(name):
    if name == "":
        return False
    if "|" in name:
        return False
    return True
def validate_number_row(row):
    return row.isdigit()
def validate_number(number):
    return number.isdigit()
def validate_code(code):
    if code in halls.keys():
        return False
    if not validate_input(code):
        return False
    return True
def check_seat(hall,seat):
    size = 0
    for letter in seat:
        number = ord(letter) - 65
        size += number
        size = size * 26

    if size > hall.hall_signe_seat:
        return False
    return True
def create_seat(number_seat):
    seat_str = ""
    while number_seat > 0:
        
        letter =chr( ((number_seat - 1)% 26) + 65)
        seat_str = letter + seat_str
        number_seat = (number_seat - 1) // 26
    return seat_str
def check(hall):
    if hall in halls.keys():
        return halls[hall].active
    return False
def gethall(code):
    if code in halls.keys():
        return halls[code]
        
    return None
#rad sa memorijom (load save i dodavanje novih sala)
def add_hall():
    code = input("Unesi kod sale, on ne sme da sadrzi znak | ")
    while(not validate_code(code)):
        code = input("Unesi kod sale, on ne sme da sadrzi znak | ")
        if code == "X":
            return
    name = input("Unesi ime sale bez znaka | ")
    while(not validate_input(name)):
        name = input("Unesi ime sale bez znaka | ")
        if name == "X":
            return 
    row = input("Unesi broj redova sale ")
    while(not validate_number(row)):
        row = input("Unesi broj redova sale ")
        if row == "X":
            return 
    seat = input("Unesi broj sedista u redu sale ")
    while(not validate_number(seat)):
        seat = input("Unesi broj sedista u redu sale ")
        if seat == "X":
            return 
    halls[code] = Sala(code, name, row, seat,True)
def load():
    file = open("data\Sala.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            halls[line[0]] = Sala(line[0],line[1],line[2],line[3],line[4] == "True")
    file.close() 
def save():
    file = open("data\Sala.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\Sala.txt","a",encoding="utf-8")
    for hall in halls.values():
        file.write(hall.to_string())
    file.close()
def print_halls():
    halls_for_print = []
    max_size = [0,0,0,0]
    for hall in halls.values():
        if hall.active:
            halls_for_print.append(hall.to_list())
            i = 0      
            for thing in hall.to_list():
                max_size[i] = max(max_size[i],len(thing))
                i = i + 1
    PrintTabel.print_tabel_start_end(max_size)
    for hall in halls_for_print:
            PrintTabel.print_tabel_row(hall,max_size)
    PrintTabel.print_tabel_start_end(max_size)      
#brisanje
#izmenu podataka
#poruke klijentu
