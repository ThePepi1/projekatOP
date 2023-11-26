def print_tabel_row(movie, sizes,coluns): 
    print("|",end="")
    for i in range(coluns):        
        form = "{:^%d}" % sizes[i]
        print(form.format(movie[i]), end ="|")
    print()

def print_tabel_start_end(sizes):
    for size in sizes:
        print("+"+ "-"*(size), end="")
    print("+")