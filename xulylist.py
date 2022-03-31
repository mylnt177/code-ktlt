#Chèn 1 phần tử vào trong list tăng đảm bảo list vẫn tăng
print(" Yêu cầu : chèn 1 phần tử vào trong list tăng đảm bảo list vẫn tăng")
list=[1,3,4,6,7,8,9,10]
a=int(input(" Nhập phần tử muốn chèn : "))
i=0
vt=0
while (a > list[i]):
    i=i+1
    vt=i
print(vt)
list=list+[a]
for i in range (vt,len(list)-1):
   q = list[-1]
   list[-1]=list[i]
   list[i]=q
   i+=1
print(list)
#Đếm xem trong đây có bao nhiêu list con tăng
print(" Yêu cầu :nhập vô 1 list số nguyên")
print("Đếm xem trong đây có bao nhiêu list con tang")
list1=[]
b=0
n=int(input("Số các số hạng bạn muốn nhập vào : "))
for i in range (1,n+1):
    print("Số hạng thứ", i ,"là " , end="")
    a=int(input())
    list1.append(a)
print(list1)
for i in range (len(list1)-1):
    if list1[i] > list1[i+1]:
        b=b+1
print(">>> Số list con tăng là : " , b+1)
#Trộn 2 list tăng thành 1 list tăng
print(" Yêu cầu :trộn 2 list tăng thành 1 list tăng")
a1=[1,3,5,7,9,11]
a2=[2,4,6,8,10,12]
a3=a1+a2
print(a1)
print(a2)
for i in range (len(a3)):
    for j in range (i):
        if a3[i]<a3[j]:
            t=a3[i]
            a3[i]=a3[j]
            a3[j]=t
print(" List tăng dần " ,a3)

