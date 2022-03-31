#append
list = []
print (" >>> APPEND ")
a=int(input(" Bạn cần thêm bao nhiêu phần tử vào list: "))
for i in range (1,a+1):
    print(" Nhập phần tử cần thêm thứ ",i," : ",end=" ")
    b=input()
    list= list + [b]
print("=> List sau khi thực hiện phương thức append: " , list)
#insert
print(" >>> INSERT ")
c=input(" Nhập phần tử cần chèn : ")
d=int(input(" Nhập vị trí muốn chèn : "))
list=list+[c]
for i in range (d,len(list)-1):
   q = list[-1]
   list[-1]=list[i]
   list[i]=q
   i+=1
print(list)
#index
print(">>> INDEX ")
list1=str(input(" Nhập chuỗi : "))
list=list1.upper()
q1=input(" Nhập phần tử cần tìm trong list : ")
q=q1.upper()
vt=0
z=[]
for i in range (len(list1)):
    if list[i]==q:
        vt = i
        z.append(vt)
print(" Vị trí ", q1, " xuất hiện là ", z)
#reverse
print(">>> REVERSE")
d=str(input(" Nhập chuỗi : "))
ds=[]
for i in range(1,len(d)+1):
    ds=ds+[d[-i]]
print(" Chuỗi sau khi thực hiện phương thức reverse : ", ds)
#queue
print(" QUEUE")
queue=[]
a=int(input(" Bạn cần thêm bao nhiêu phần tử vào list: "))
for i in range (1,a+1):
    print(" Nhập phần tử cần thêm thứ ",i," : ",end=" ")
    d=input()
    queue= queue +  [d]
queue.pop(0)
queue.pop(0)
print(queue)

#stack
print(" STACK ")
stack = []
a=int(input(" Bạn cần thêm bao nhiêu phần tử vào list: "))
for i in range (1,a+1):
    print(" Nhập phần tử cần thêm thứ ",i," : ",end=" ")
    t=input()
    stack= stack + [t]
stack.pop()
stack.pop()
print(stack)
