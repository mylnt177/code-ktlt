import math
h=int(input("Nhập số dòng: "))
s=0
for i in range (h,0,-1):
   s=math.sqrt(s+(math.sqrt((i-1)+math.sqrt(i))))
print(s)
