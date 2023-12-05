class Sala:
    def __init__(self, hall_id,hall_name, hall_number_row, hall_signe_seat):
        self.hall_id = hall_id
        self.hall_name = hall_name
        self.hall_number_row = int(hall_number_row) 
        self.hall_signe_seat = int(hall_signe_seat)
        
Halls = {}
def validate_name(name):
    if name == "":
        return False
    if "|" in name:
        return False
    return True
def validate_number_row(row):
    return row.isdigit()
def validate_sites(hall_seat):
    return hall_seat.isdigit()
def check_seat(hall,seat):
    size = 0
    for letter in seat:
        number = ord(letter) - 65
        size += number

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
