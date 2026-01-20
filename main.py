def qoshish(a, b):
    a = str(a)
    b = str(b)
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        return a + b
    else:
        return "xatolik bor"


def ayirish(a, b):
    a = str(a)
    b = str(b)
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        return a - b
    else:
        return "xatolik bor"


def bolish(a, b):
    a = str(a)
    b = str(b)
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        return a / b
    else:
        return "xatolik bor"


def kopaytirish(a, b):
    a = str(a)
    b = str(b)
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        return a * b
    else:
        return "xatolik bor"


def hisobla(son_1, amal_, son_2):
    if amal == "+":
        return qoshish(son1, son2)
    elif amal == "-":
        return ayirish(son1, son2)
    elif amal == "/":
        return bolish(son1, son2)
    elif amal == "*":
        return kopaytirish(son1, son2)
    else:
        return "Xatolik bor"


son1 = int(input("1_son kirit: "))
son2 = int(input("2_son kirit: "))
amal = input("Amal kirit(+, -, *, /): ")
res = hisobla(son_1=son1, amal_=amal, son_2=son2)
print(res)
