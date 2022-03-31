doanvan="Hôm nay tôi ăn cơm.Cơm gà 30k.Cơm thịt boà 50k.Cơm chiên trứng 45k."
print(doanvan)
#đếm từ cơm
a="cơm"
b="Cơm"
com1= doanvan.count(a)
com2= doanvan.count(b)
print(">>>Số từ cơm của đoạn văn là : " , com1+com2)
#đếm bao nhiêu từ
c=0
for i in range (len(doanvan)):
    if (doanvan[i]==" ") or (doanvan[i]=="."):
            c+=1
print (">>>Số từ của đoạn là: " ,c)
#đếm số câu
cau=doanvan.count(".")
print(" Số câu trong đoạn văn là : ", cau)
#đếm số đoạn
#tính tổng chuỗi phân số:
phanso= " 1/2 2/3 3/4 4/5 "
ps=phanso.split()
print(ps)
tong=[0,1]
def tinhtong():
    for i in range (len(ps)):
        tong[0] = int(ps[i][0]) * tong[1] + int(ps[i][2]) * tong[0]
        tong[1] = int(ps[i][2]) * tong[1]
    print("Tổng các phân số là: ", tong[0], "/", tong[1])
print(tinhtong())
def toigian():
    usc=0
    a = tong[0]
    b = tong[1]
    for i in range (1,a+1):
        if(a % i == 0) and (b % i == 0):
            a=a/i
            b=b/i
    print("Tổng các phân số sau tối giản là: ",a,"/",b)
print(toigian())
