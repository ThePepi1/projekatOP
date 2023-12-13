import PrintTabel 
types_of_movies = ["Horor", "Action", "Adventure", "Romance", "Comedy"]
class Movie:
    def __init__(self,id, name, type, length, director, roles, countyr_of_origin,year,description,active):
        self.id = id
        self.name = name
        self.type = type
        self.lenght = length
        self.director = director
        self.roles = roles
        self.country_of_origin = countyr_of_origin
        self.year = year
        self.description = description
        self.active = active
    def to_list(self):
        return [str(self.id), self.name, self.type,str(self.lenght), self.director, self.roles, self.country_of_origin,self.year,self.description]
    def to_string(self):
        return f"{str(self.id)}|{self.name}|{self.type}|{str(self.lenght)}|{self.director}|{self.roles}|{self.country_of_origin}|{self.year}|{self.description}|{self.active}\n"
    def equal(self,movie):
        print(movie.to_string(),self.to_string())
        return self.name == movie.name and self.type == movie.type and movie.lenght == self.lenght and movie.roles == self.roles and movie.year == self.year


movies = {}

def print_movies(movie_names = "", type = "", max_lenght="", min_lenght="", directors="", roles = "", year_of_recording = "", coutrys_of_origins = "",print = True): 
    movies_for_print = []
    max_size = [0,0,0,0,0,0,0,0,0]
    for movie in movies.values():
        if(check_movie(movie,movie_names, type, max_lenght, min_lenght, directors, roles , year_of_recording, coutrys_of_origins) and movie.active): 
            movies_for_print.append(movie.to_list())
            i = 0
            for thing in movie.to_list():        
                if len(thing) > max_size[i]:
                    max_size[i] = len(thing)
                i+= 1 
    if print:           
        PrintTabel.print_tabel_start_end(max_size)
        for movie in movies_for_print:
            PrintTabel.print_tabel_row(movie,max_size)
        PrintTabel.print_tabel_start_end(max_size)
    else:
        return movies_for_print
def check_movie(movie, movie_names = "", type = "", max_lenght="", min_lenght="", directors="", roles = "", year_of_recording = "", coutrys_of_origins = ""):
    if not check_one(movie.name, movie_names):
        return False
    if not check_one(movie.type, type):
        return False
    if not check_one(movie.director, directors):
        return False
    if not check_one(movie.roles, roles):
        return False
    if not check_one(movie.country_of_origin, coutrys_of_origins):
        return False
    if not check_one(movie.year, year_of_recording):
        return False
    if not max_lenght == "":
        if int(max_lenght) < movie.lenght:
            return False
    if not min_lenght == "":
        if int(min_lenght) > movie.lenght:
            return False
    return True
def check_one(movie, tester):
    tester = tester.split(", ")
    testing_data = movie.split(", ")
    if "" in tester:
        tester.remove("")
    if tester and not all(i in tester for i in testing_data):
        return False
    return True
def save():
    file = open("data\\film.txt","w",encoding="utf-8")
    file.write("")
    file.close()
    file = open("data\\film.txt","a",encoding="utf-8")
    for movie in movies.values():
        file.write(movie.to_string())
    file.close()
def load():
    file = open("data\\film.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            movies[line[0]] = (Movie(int(line[0]),line[1],line[2],int(line[3]),line[4],line[5],line[6],line[7],line[8],line[9] == "True")) 
def validate_input(input):
    if input == "":
        return False
    if "|" in input:
        return False
    return True
def validate_type(types):
    return all(type in types_of_movies for type in types.split(", "))
def validate_number(lenght):
    return lenght.isdigit()
def validate_roles(roles):
    if not validate_input(roles):
        return False
    roles = roles.split(", ")
    for role in roles:
        if role == "": 
            return False
        if role[0] == " ":
            return False
        if role[-1] == " ":
            return False
    return True
def pretraga_filmova(printing = True):
    print("Ukoliko zelite da pretrazite filmove po imenu ukucajte 1")
    print("Ukoliko zelite da pretrazite filmove po zanru ukucajte 2")
    print("Ukoliko zelite da pretrazite filmove tako da budu kraci od unetog vremena ukucajte 3")
    print("Ukoliko zelite da pretrazite filmove tako da budu duzi od unetog vremena ukucajte 4")
    print("Ukoliko zelite da pretrazite filmove po direktorima ukucajte 5")
    print("Ukoliko zelite da pretrazite filmoce po glavnim ulogama ukucajte 6")
    print("Ukoliko zelite da pretrazite filmoce po godini ukucajte 7")
    print("Ukoliko zelite da pretrazite filmoce po zemlji porekla ukucajte 8")
    user_input2 = input()
    user_input2 = user_input2.split(" ")
    if "1" in user_input2:
        user_input_movie_name = input("Unesi ime filma koji zelis da pretrazis. Ukoliko ih ima vise odvojite ih , i razmakom ") 
    else:
        user_input_movie_name = ""
    if "2" in user_input2:
        user_input_movie_type = input("Unesi zanr koji zelis da pretrazis. Ukoliko ih ima vise odvojite ih , i razmakom ")
    else:
        user_input_movie_type = ""            
    if "3" in user_input2:
        user_input_movie_max_lenght = input("Unesi maximalnu duzinu ")
    else:
        user_input_movie_max_lenght = ""
    if "4" in user_input2: 
        user_input_movie_min_lenght = input("Unesi minimalnu duzinu ")
    else:
        user_input_movie_min_lenght = ""
    if "5" in user_input2:
        user_input_movie_directors  = input("Unesi direktore po kojima zelis da pretrazis, ukoliko ih ima vise odvoji ih , i razmakom ")
    else:
        user_input_movie_directors = ""
    if "6" in user_input2:
        user_input_movie_roles  = input("Unesi uloge po kojima zelis da pretrazis, ukoliko ih ima vise odvoji ih , i razmakom ")
    else:
        user_input_movie_roles = ""
    if "7" in user_input2:
        user_input_movie_year = input("Unesi godine po kojima zelis da pretrazis, ukoliko ih ima vise odvoji ih , i razmakom ")
    else:
        user_input_movie_year = ""
    if "8" in user_input2:
        user_input_movie_country_of_origin = input("Unesi zemlje porekla po kojima zelis da pretrazis, ukoliko ih ima vise odvoji ih , i razmakom ")
    else:
        user_input_movie_country_of_origin = ""

    return print_movies(user_input_movie_name,user_input_movie_type,user_input_movie_max_lenght,user_input_movie_min_lenght, user_input_movie_directors, user_input_movie_roles,user_input_movie_year, user_input_movie_country_of_origin,printing)
def check(movie_id):
    if movie_id in movies.keys():
        return movies[movie_id].active
    return False
def get_movie(movie_id):
    if movie_id in movies.keys():
            return movies[movie_id]
def add_movie():
    print("Ukoliko zelite da prekinete ukucajte X u bilo kom trenutku, nijedan unos ne sme da zadrzi znak |")
    name = ""
    while not validate_input(name):
        name = input("Unesi ime fulma ")   
        if name == "X":
            return 
    type = ""
    while not validate_type(type):
        print("Postojeci zanrovi su: ")
        for type_of_movie in types_of_movies:
            print(type_of_movie, end= " ")
        print("")
        type = input("Unesi zanr filma od postojecih zanrova ukoliko postoje vise razdvojite ih zarezom i razmakom ")
        if name == "X":
            return 
    length = ""
    while not validate_number(length):
        length = input("Unesi duzinu filma ")
        if length == "X":
            return 
    director = ""
    while not validate_input(director):
        director = input("Unesi ime rezisera")
        if director == "X":
            return 
    roles = ""
    while not validate_roles(roles):
        roles = input("Unesi ime glavnih likova, ako ih ima vise odvojite ih zarezom i razmakom ")
        if roles == "X":
            return  
    country = ""
    while not validate_input(country):
        country = input("Unesi zemlju porekla ")
        if country == "X":
            return
    year = ""
    while not validate_number(year):
        year = input("Unesi godinu snimanja ")
        if year == "X":
            return
    description = ""
    while not validate_input(description):
        description = input("Unesi opis filma ")
        if description == "X":
            return
    id = 1
    while str(id) in movies.keys():
        id = id + 1    
    
    movie_save = Movie(str(id),name,type,int(length),director,roles,country,year,description,True)           
    for movie in movies.values():
        if movie.equal(movie_save):
            movie.active = True
            return
    movies[movie_save.id] = movie_save
def delete():
    print_movies()
    user_input = ""
    while not user_input in movies.keys():
        user_input = input("Unesi index filma koji zelite da obrisite ")
        if user_input == "X":
            return 
    movies[user_input].active = False
#To Do izmena odredjenog dela filma(sve sem id)
load()
print_movies()