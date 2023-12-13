def print_tabel_row(movie, sizes): 
    print("|",end="")
    coluns = len(movie)
    for i in range(coluns):        
        form = "{:^%d}" % sizes[i]
        print(form.format(movie[i]), end ="|")
    print()

def print_tabel_start_end(sizes):
    for size in sizes:
        print("+"+ "-"*(size), end="")
    print("+")


# make ageneretor that just need movies for print halls for print etc not sizes (makes easyer for use in all scenarios)