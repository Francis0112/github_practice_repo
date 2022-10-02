


def bork(a, b, operator):
    eq = f"{a} {operator} {b}"
    new = eq.split()
    res = 0
    if operator == "+" or "-" or "*" or "/":
        res = eval(f"{a}{operator}{b}")
        print(f"\t  {new[0]}\n\t{new[1]} {new[2]}\n\t_____\n\t {res}")
        print(eq)
    else:
        pass


bork(12,12,"+")

 