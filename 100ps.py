#Tổng 100 phân số
a=1
while a!=0:
    while True:
        try:
            n=int(input("Nhập số phân số cần tính: "))
            if n>0:
                break
            else:
                print(" >>> Vui lòng nhập số phần tử hơn 0")
        except:
            print(">>> Vui lòng nhập đúng kiểu dữ liệu")
    ds=[]
    ps=[]
    def nhap():
        for i in range (1,n+1):
            print('- Nhập phân số thứ ',i)
            while True:
                try:
                    a =int(input(" Nhập tử số: "))
                    while True:
                        b=int(input(" Nhập mẫu số: "))
                        if b>0:
                            break
                        else:
                            print(" Vui lòng nhập mẫu số lớn hơn 0")
                except:
                    print(">>> Vui lòng nhập đúng kiểu dữ liệu")
                else:
                    ps.append([a,b])
                    break
        return(ps)
#phansolonnhat
    def lonnhat():
        v = 0
        m = 0
        for i in range (n-1):
            for j in range (1):
                if (ps[i][j] / ps[i][j+1] > ps[i+1][j] / ps[i+1][j+1]):
                    v=ps[i][j]
                    m=ps[i][j+1]
                else:
                    v=ps[i+1][j]
                    m=ps[i+1][j+1]
#phansonhonhat
    def nhonhat():
        q = 0
        w = 0
        min=0
        for i in range(n-1):
            for j in range(1):
                if (ps[i][j] / ps[i][j + 1] > ps[i + 1][j] / ps[i + 1][j + 1]):
                    q = ps[i + 1][j]
                    w =  ps[i + 1][j + 1]
                else:
                    q =ps[i][j]
                    w = ps[i][j + 1]
        print(">>> Phân số nhỏ nhất trong dãy là: ",q, "/", w)
#tinhtong
    tong = [0, 1]
    def tinhtong():
        for i in range(n):
            tong[0] = int(ps[i][0]) * tong[1] + int(ps[i][1])* tong[0]
            tong[1] = int(ps[i][1]) * tong[1]
        print("*** Tổng các phân số là: ", tong[0],"/",tong[1])

    def toigian():
        a = tong[0]
        b = tong[1]
        usc = 0
        for i in range(1, a):
            if (a % i == 0) and (b % i == 0):
                usc = i
        print(" Tối giản : ", a / usc, "/", b / usc)
    print(nhap())
    print(tinhtong())
    print(toigian())
    print(lonnhat())
    print(nhonhat())
