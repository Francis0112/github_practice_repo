

def getlist(thelist):
    if len(thelist)<3:
        print("the list is less than 3")
    else:
        for i in thelist:
            a = i.split()
            print(f"\t  {a[0]}\n\t{a[1]} {a[2]}\n\t____\n\t  {eval(i)}\n\n")


getlist(["12 + 10","20 - 3","5 * 5","10 / 3"])

