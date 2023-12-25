def print_tabel_row(things_for_prints, sizes): 
    print("|",end="")
    coluns = len(things_for_prints)
    for i in range(coluns):        
        form = "{:^%d}" % sizes[i]
        print(form.format(things_for_prints[i]), end ="|")
    print()

def print_tabel_start_end(sizes):
    for size in sizes:
        print("+"+ "-"*(size), end="")
    print("+")
def prepare_for_printing(things_for_prints):
    max_size = []
    if things_for_prints == []:
        print("Ne postoji takva stvar")
        return
    for i in range(len(things_for_prints[0])):
        max_size.append(0)
    for things in things_for_prints:
        i = 0
        for thing in things:
            max_size[i] = max(max_size[i], len(thing))
            i = i + 1
    print_tabel_start_end(max_size)
    for things in things_for_prints:
        print_tabel_row(things, max_size)
    print_tabel_start_end(max_size)
