class Sala:
    def __init__(self, hall_id,hall_name, hall_number_row, hall_signe_site):
        self.hall_id = hall_id
        self.hall_name = hall_name
        self.hall_number_row = hall_number_row
        self.hall_signe_site = hall_signe_site
        
Halls = []

def validate_name(name):
    if name == "":
        return False
    if "|" in name:
        return False
    return True
def validate_number_row(row):
    return row.isdigit()
def validate_sites(hall_sites):
    return hall_sites.isdigit()