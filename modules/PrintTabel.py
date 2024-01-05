def print1(string):
    print(string, end= '')




def print_tabel_row(things_for_prints, sizes, function): 
    function("|")
    coluns = len(things_for_prints)
    for i in range(coluns):        
        form = "{:^%d}" % sizes[i]
        function(form.format(things_for_prints[i]) + "|")
    function("\n")

def print_tabel_start_end(sizes, function):
    for size in sizes:
        function("+"+ "-"*(size))
    function("+\n")
def prepare_for_printing(things_for_prints, function = print1):
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
    print_tabel_start_end(max_size, function)
    for things in things_for_prints:
        print_tabel_row(things, max_size, function)
    print_tabel_start_end(max_size, function)
