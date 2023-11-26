class Korisnik:
    def __init__(self,username,password,name,lastname,row = 1, type = 1):
        self.row = row
        self.username = username
        self.password = password
        self.name = name
        self.lastname = lastname
        self.type = type
    def edit_profile(self):
        while True:
            print("Ukoliko zelite da promenite sifru ukucajte 1")
            print("Ukoliko zelite da promenite ime ukucajte 2")
            print("Ukoliko zelite da promenite prezime ukucajte 3")
            print("Ukolko odustajete ukucajte X")
            user_input = input()
            if user_input == "1":
                password = ""
                while True:
                    password = input("Unesi lozinku koja ima vise od 6 karaktera i mora sadrzati makar jedan bro, ukoliko ne zelite to da promenite ukucajte X ")
                    if password == "X":
                       users[self.row - 1] = self
                       return self
                    if validate_pass(password):
                        break
                self.password = password
            elif user_input == "2":
                name =""
                while True:
                    name = input("Unesite vase ime bez znaka |, ukoliko ne zelite to da promenite X ")
                    if name == "X":
                       users[self.row - 1] = self
                       return self
                    if check_every_input(name):
                        break   
                self.name = name 
            elif user_input == "3":
                lastname = ""
                while True:
                    lastname = input("Unesite vase prezime bez znaka |, ukoliko ne zelite to da promenite ukucajte X ")
                    if lastname == "X":
                       users[self.row - 1] = self
                       return self
                    if check_every_input(lastname):
                        break    
                self.lastname = lastname
            elif user_input == "X":
                break
            else:
                print("Uneli ste ne postojecu naredbu")
        users[self.row - 1] = self
        
        return self
    def to_string(self):
        return f"{self.row}|{self.username}|{self.password}|{self.name}|{self.lastname}|{self.type}\n"    
    def create_seller(self):
        if self.type == 3:
            register(2)
    def create_manager(self):
        if self.type == 3:
            register(3)


users = []




def login(username, password):
    for user in users:
        if username == user.username:
            if password == user.password:
                return user
            else:
                print("Pogresna lozinka pokusaj ponovo")
                return  
    print("Nepostojece korisnicko ime")
    return 
def check_every_input(text):
    if "|" in text:
        print("Unos ne sme da sadrzi znak |")
        return False
    if text == "":
        print("Unos ne sme da bude prazan")
        return False
    return True







def validate_pass(password):
        if len(password) < 6:
            print("Sifra mora da sadrzi vise od 6 karaktera, Pokusaj ponovo")
            return False
        if not check_every_input(password):
            return False
        for char in password:
            if char.isdigit():
                return True
        print("Sifra mora da sadrzi makar jedan broj")
        return False
def check_user_name(username):
    if not check_every_input(username):
        return False
    for user in users:
        if user.username == username:
            print("Korisnicko ime je vec u bazi pokusajte ponovo")
            return False
    return True
def register(Type = 1):
    print("Nijedan od unosa ne sme da sadrzi | znak \nUkoliko zelite da prekinete ukucajte X u bilo kom unosu")
    username = ""
    while True:
        username = input("Unesi korisnicko ime ")
        if username == "X":
            return
        if check_user_name(username):
            break 
    password = ""
    while True:
        password = input("Unesi lozinku koja ima vise od 6 karaktera i mora sadrzati makar jedan broj ")
        if password == "X":
            return
        if validate_pass(password):
            break
    name =""
    while True:
        name = input("Unesite vase ime bez znaka |")
        if name == "X":
            return
        if check_every_input(name):
            break
    
    lastname = ""
    while True:
        lastname = input("Unesite vase prezime bez znaka |")
        if lastname == "X":
            return 
        if check_every_input(lastname):
            break
        



    if users != []:
        user = Korisnik(username, password, name, lastname,users[-1].row + 1,Type)
    else :
        user = Korisnik(username, password, name, lastname,type= Type)
    users.append(user)

def load():
    file = open("users.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            users.append(Korisnik(line[1],line[2],line[3],line[4],int(line[0]),int(line[5])))
    file.close() 
def save():
    file = open("users.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("users.txt","a",encoding="utf-8")
    for user in users:
        file.write(user.to_string())
    file.close()
