def Myfourth_progaram():
    num = int(input("type Number: "))
    l = []
    for u in range(1, 10):
        if u % num == 0:
            l.append(u)
    return l
print(Myfourth_progaram())