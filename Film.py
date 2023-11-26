import PrintTabel 
types_of_movies = ["Horro", "Action", "Adventure", "Romance", "Comedy"]
class Film:
    def __init__(self, name, type, length, director, roles, countyr_of_origin,year,description):
        self.name = name
        self.type = type
        self.lenght = length
        self.director = director
        self.roles = roles
        self.country_of_origin = countyr_of_origin
        self.year = year
        self.description = description
    def to_list(self):
        return [self.name, self.type,str(self.lenght), self.director, self.roles, self.country_of_origin,self.year,self.description]

movies = []

def print_movies(movie_names = "", type = "", max_lenght="", min_lenght="", directors="", roles = "", year_of_recording = "", coutrys_of_origins = ""): 
    file = open("film.txt","r",encoding="utf-8")
    movies_for_print = []
    max_size = [0,0,0,0,0,0,0,0]
    for movie in movies:
        if(check_movie(movie,movie_names, type, max_lenght, min_lenght, directors, roles , year_of_recording, coutrys_of_origins)): 
            movies_for_print.append(movie.to_list())
            i = 0
            for thing in movie.to_list():        
                if len(thing) > max_size[i]:
                    max_size[i] = len(thing)
                i+= 1 
    PrintTabel.print_tabel_start_end(max_size)
    for movie in movies_for_print:
        PrintTabel.print_tabel_row(movie,max_size,8)
    PrintTabel.print_tabel_start_end(max_size)
    file.close()
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
    if tester and not any(i in tester for i in testing_data):
        return False
    return True

def load():
    file = open("film.txt","r",encoding="utf-8")
    for line in file:
        if line != "":
            line = line[:-1]
            line = line.split("|")
            movies.append(Film(line[0],line[1],int(line[2]),line[3],line[4],line[5],line[6],line[7])) 
def validate_input(input):
    if input != "":
        return False
    if "|" in input:
        return False
    return True
def validate_type(type):
    return type in types_of_movies
def validate_lenght(lenght):
    return lenght.isdigit()

def pretraga_filmova():
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

    print_movies(user_input_movie_name,user_input_movie_type,user_input_movie_max_lenght,user_input_movie_min_lenght, user_input_movie_directors, user_input_movie_roles,user_input_movie_year, user_input_movie_country_of_origin)
