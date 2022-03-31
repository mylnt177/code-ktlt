ds=[]
duong=[]
done=[]
while True:
    try:
        n = int(input(" Số phần tử bạn muốn nhập: "))
        if n>0:
            break
        else :
            print(" Vui lòng nhập số không âm ")
    except:
            print( ">>> Vui lòng nhập đúng kiểu dữ liệu ")
def nhap():
    for i in range (n):
        while True:
            try:
                print("Nhập phần tử thứ: ", i + 1)
                a = int(input())
            except:
                print(">>> Vui lòng nhập đúng dữ liệu ")
            else:
                ds.append(a)
                break
    return
def khongam():
    for i in ds:
        if i>0:
            duong.append(i)
    return
def chiahet():
    for i in duong:
        if (i%2==0) or (i%14==0):
            done.append(i)
    return(done)

def tong():
    s=0
    for i in done:
        s+=i
        i+=1
    return(s)

print(nhap())
print(khongam())
print("Dãy số đạt yêu cầu đề bài là : ", chiahet())
print("Tổng các số đạt yêu cầu : ", tong())