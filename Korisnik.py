class Korisnik:
    def __init__(self,Username,Password,Name,Lastname,Type = 1,row = -1):
        self.row = row
        self.username = Username
        self.password = Password
        self.name = Name
        self.lastname = Lastname
        self.type = Type
    def SaveProfile(self):
        file = open("users.txt","r")
        last_line = file.readlines()[-1]
        number = int(last_line[0]) + 1 
        file.close()
        file = open("users.txt", "a")
        script = f"{number}|{self.username}|{self.password}|{self.name}|{self.lastname}|{self.type}\n"
        file.write(script)
        file.close()
    def EditProfile(self):
        input1 = input("Unesi sifru koju hoces da koristis ukoliko ne zelis da promenis sifru pritisnite enter ")
        while input1 != "" and not ValidatePass(input1):
              input1 = input("Unesi sifru koju hoces da koristis ukoliko ne zelis da promenis sifru pritisnite enter ")
        if input1 != "":
            self.password = input1
        input1 = input("Unesi ime ukoliko ne zelis da ga promenis pritisni enter ")
        while "|" in input1:
            input1 = input("Ime ne sme da sadrzi znak |. Pokusaj ponovo ")
        if input1 != "":
            self.name = input1
        input1 = input("Unesi prezime ukoliko ne zelis da ga promenis pritisni enter ")
        while "|" in input1:
            input1 = input("Prezime ne sme da sadrzi znak |. Pokusaj ponovo? ")
        if input1 != "":
            self.lastname = input1
        file = open("users.txt","r")
        Textlist = file.read().split("\n")
        Textlist[self.row-1] = f"{self.row}|{self.username}|{self.password}|{self.name}|{self.lastname}|{self.type}"
        file.close()
        file = open("users.txt","w")
        file.write("")
        file.close()
        file = open("users.txt","a")
        for Line in Textlist:
            if Line != "":
                file.write(Line+"\n")
        file.close()
        return self
#To DO razdvoji klase u posebne fajlove mnogo ce da bude sve u isto
class Manager(Korisnik):
    def CreateSeller():
        Register(2)
    def CreateManager():
        Register(3)
class Seller(Korisnik):
    pass



def Login(Username, Password):
    file = open("users.txt", "r")
    for line in file:
        User = line.split("|")
        if User[1] == Username and User[2] == Password:
            file.close()
            if User[5] == "1":
                return Korisnik(User[1],User[2],User[3],User[4],int(User[5]),int(User[0]))
            elif User[5] == "2":
                return Seller(User[1],User[2],User[3],User[4],int(User[5]),int(User[0]))
            else:
                return Manager(User[1],User[2],User[3],User[4],int(User[5]),int(User[0]))
    print("Pogresno uneseno korisnicko ime ili sifra")
    file.close()
    return "Greska"


def ValidatePass(password):
        if len(password) < 6:
            print("Sifra mora da sadrzi vise od 6 karaktera, Pokusaj ponovo")
            return False
        if "|" in password:
            print("Lozinka ne sme da sadrzi znak |")
            return False
        for char in password:
            if char.isdigit():
                return True
        print("Sifra mora da sadrzi makar jedan broj")
        return False
def CheckUserName(User):
    file = open("users.txt", "r")
    if "|" in User:
        print("Korisncko ime ne sme da sadrzi | ")
        return False
    for line in file:
        Username = line.split("|")[1]
        if User == Username:
            print("Korisnicko ime je zauzeto pokusajte ponovo")
            return False
    return True
def Register(Type = 1):
    print("Nijedan od unosa ne sme da sadrzi | znak")
    Username = input("Unesi korisnicko ime ")
    while(not CheckUserName(Username)):
        Username = input("Unesi korisnicko ime ")
    Password = input("Unesi lozinku koja ima vise od 6 karaktera i mora sadrzati makar jedan broj ")
    while(not ValidatePass(Password)):
        Password = input("Unesi lozinku koja ima vise od 6 karaktera i mora sadrzati makar jedan broj ")
    Name = input("Unesite vase ime ")
    while("|" in Name):
        Name = input("Unesite vase ime bez znaka |")
    Lastname = input("Unesite vase prezime ")
    while("|" in Lastname):
        Lastname = input("Unesite vase prezime bez znaka |")
    Korisnik(Username, Password, Name, Lastname,Type).SaveProfile()