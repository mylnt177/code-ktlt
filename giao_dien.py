import tkinter as tk
import cmath

root = tk.Tk()
root.title("Giải phương trình bậc 2")
root.geometry("400x350")


entry1 = tk.Entry(root)
entry1.place(x=200, y=60)

entry2 = tk.Entry(root)
entry2.place(x=200, y=100)

entry3 = tk.Entry(root)
entry3.place(x=200, y=140)

#entry4=tk.Entry(root)
#entry4.place(x=60,y=240)

lbl1 = tk.Label(root, text=" Hệ số a")
lbl1.place(x=60, y=50)

lbl2=tk.Label(root, text=" Hệ số b")
lbl2.place(x=60,y=100)

lbl3=tk.Label(root, text=" Hệ số c")
lbl3.place(x=60, y=140)

lbl4=tk.Label(root, text=" Phương trình có dạng ax^2 + bx + c = 0")
lbl4.place(x=100, y=20 )

lbl5=tk.Label(root,text="Kết quả: ")
lbl5.place(x=60,y=240)



def giai_pt():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    delta=b**2 - (4*a*c)
    if delta > 0:
        x1 = float((-b - cmath.sqrt(delta)) / (2 * a))
        x2 = float((-b + math.sqrt(delta)) / (2 * a))
        kq = "x1={0};  x2={1}".format(x1, x2)

    elif delta == 0:
        kq= "Nghiệm kép x =" + str(-b / 2 * a)
    else :
        kq=" Vô nghiệm  "
        entry4.place(x=60,y=240)

def clear():
    entry1.delete(0,None)
    entry2.delete(0,None)
    entry3.delete(0,None)
    entry4.delete(0,None)


btn_giaipt = tk.Button(text='Giải phương trình', command=giai_pt)
btn_giaipt.place(x=150,y=180)
btn_clear=tk.Button(root,text=" Clear", command=clear)
btn_clear.place(x=295,y=179)
root.mainloop() 