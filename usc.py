a=1
b=1
while True:
    try:
        a = int(input("Nhập số a :"))
        b = int(input("Nhập so b :"))
        r = a % b
    except:
        print(" Mời bạn nhập đúng điều kiện các số nhập vào lớn hơn 0")
    else:
        if r==0:
            print("Ước lớn nhất là", b)
        else:
            while r != 0:
                a = b
                b = r
                r = a%b
        print("Ước lớn nhất là", b )


