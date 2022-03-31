n=int(input(" Nhập số khách hàng: "))
ds = []
sdt = []
diachi = []
dien = []
def dskh():
  for i in range (1,n+1):
    print(" Nhập tên khách hàng: ")
    a=str(input())
    ds.append(a)
print(dskh())
def nhapthongtin():
  for i in range(n):
    c = int(input(" Số điện thoại của  "+ ds[i] +" là " ))
    d = int(input(" Số kwh của "+ ds[i] + " là " ))
  sdt.append( c )
  dien.append( d )
print(nhapthongtin())

import pandas as pd

data = {
  "ds":[] ,
  "sdt": []
}

myvar = pd.DataFrame(data)

print(myvar)
n=int(input(" Nhập số khách hàng: "))
ds = []
sdt = []
diachi = []
dien = []
def dskh():
  for i in range (1,n+1):
    print(" Nhập tên khách hàng: ")
    a=str(input())
    ds.append(a)
print(dskh())
def nhapthongtin():
  for i in range(n):
    c = int(input(" Số điện thoại của  "+ ds[i] +" là " ))
    d = int(input(" Số kwh của "+ ds[i] + " là " ))
  sdt.append( c )
  dien.append( d )
print(nhapthongtin())

import pandas as pd

data = {
  "ds":[Ngân, Hoa , Hạnh , Mỹ ] ,
  "sdt": [0129 , 0123, 1234 , 1237 ]
}

myvar = pd.DataFrame(data)
print(myvar)
