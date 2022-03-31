tenmon = ["Toan", "Lý", "Hoa", "Sinh", "Su", "Dia", "Van", "Anh"]
A=[]
def nhapdiem(doe):
    for i in range(len(tenmon)):
        a=float(input("Nhap diem mon " + tenmon[i] + "i"))
        A.append(a)
def doichuhoa(tenmon):
    for i in range (len(tenmon)):
        tenmon[i]=tenmon[i].upper()
    return(tenmon)
def laydiem(Diem,tenmon,mon):
    tenmon=doichuhoa(tenmon)
    return(Diem[tenmon.index(mon.upper())])
tong=0
def tinhdiem(a,b,c):
    tong = a*2 + b +c
    return(tong)
