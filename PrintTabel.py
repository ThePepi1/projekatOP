def PrintTabel_row(movie, sizes,coluns = 8): 
    print("|",end="")
    for i in range(coluns):        
        form = "{:^%d}" % sizes[i]
        print(form.format(movie[i]), end ="|")
    print()

def PrintTabel_start_end(sizes):
    for size in sizes:
        print("-"*(size+1), end="")
    print()