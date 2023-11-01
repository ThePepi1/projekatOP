import PrintTabel 
types_of_movies = ["Horro", "Action", "Adventure", "Romance", "Comedy"]
class Film:
    def __init__(self, name, type, length, director, roles, countyr_of_origin,year,Description):
        self.name = name
        self.type = type
        self.lenght = length
        self.director = director
        self.roles = roles
        self.countryOfOrigin = countyr_of_origin
        self.year = year
        self.description = Description

#TO DO think aboaut best way to serch inside
# idea pass lists for it (use it to check if movie is watchable(if movie is in certan category))
def print_movies():
    file = open("film.txt","r")
    movies_for_print = []
    max_size = [0,0,0,0,0,0,0,0]
    for line in file:
        line = line[:-1]
        movie =  line.split("|") 
        movies_for_print.append(movie)
        i = 0
        for thing in movie:        
            if len(thing) > max_size[i]:
                max_size[i] = len(thing)
            i+= 1 
    PrintTabel.PrintTabel_start_end(max_size)
    for movie in movies_for_print:
        PrintTabel.PrintTabel_row(movie,max_size,8)
    PrintTabel.PrintTabel_start_end(max_size)
    file.close()

    

print_movies()