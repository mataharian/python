from tkinter import *
import math

root = Tk()
root.title("Turunan Maju")

# JUDUL TURUNAN MAJU
judul = Label( root, text = "TURUNAN MAJU", font=("Times New Roman", 20, "bold"), justify="center") 
judul.grid(row=1, column=0, columnspan=4, padx=0, pady=5)

# LOGO UNDIP
undip = PhotoImage(file="logo_undip.png")
undipkecil = undip.subsample(5,5)
logo = Label(image=undipkecil)
logo.grid(row=1, column=4, padx=10, pady=10)

# ANGGOTA KELOMPOK
Anggota = Label(root,text="Rachmad Rifai\t\t\t(24060122120014)\nDzu Sunan Muhammad\t\t(24060122120034)",justify="center")
Anggota = Label(root,text="\nThoriq Hadiwinata\t\t(24060122130086)\nMuhammad Fakhrell Andreaz\t(24060122140042)\nFarid Rahman Fadhilah\t\t(24060122140142)",justify="center")
Anggota.grid(row=2,column=0,columnspan=5, padx=40, pady=5)

labinp = Label(text="\nINPUT", font=("Times New Roman", 12, "bold"))
labinp.grid(row=3, column=1, padx=50)

# INPUT X
inp1 = Label(text="x", font=("Times New Roman", 10, "bold"))
inp1.grid(row=4, column=1, pady=5)
e1 = Entry()
e1.grid(row=4, column=2)

# INPUT H
inp2 = Label(text="h", font=("Times New Roman", 10, "bold"))
inp2.grid(row=5, column=1, pady=5)
e2 = Entry()
e2.grid(row=5, column=2)

# INPUT F(X)
inp3 = Label(text="f(x)", font=("Times New Roman", 10, "bold"))
inp3.grid(row=6, column=1, pady=5)
e3 = Entry()
e3.grid(row=6, column=2)

# ALGORITMA
pilihan = 0

def pilturunan1() :
   global pilihan
   pilihan = 1

def pilturunan1dua() :
   global pilihan
   pilihan = 2

def pilturunan2() :
   global pilihan
   pilihan = 3

def pilturunan2dua() :
   global pilihan
   pilihan = 4
   
# NGUBAH INPUT JADI FUNGSI PUNYA PARELL
def f(a, b, fa) :
   fh = fa.replace('x', str(a+b))
   fh = fh.replace('X', str(a+b))
   fh = fh.replace("cos", "math.cos")
   fh = fh.replace("sin", "math.sin")
   fh = fh.replace("tan", "math.tan")
   return eval(fh)

# RUMUS TURUNAN MASUKIN SINIII
def turunan():
   global pilihan
   a = float(e1.get())
   b = float(e2.get())
   fa = (e3.get())
   if pilihan == 1:
      turunan1 = (f(a, b, fa)-f(a, 0, fa)) / b
      turunan1 = round(turunan1,5)
      out.config(text=turunan1)
   elif pilihan == 2:
      turunan1dua = (4*(f(a, b, fa)) - f(a, 2*b, fa) - 3*(f(a, 0, fa))) / (2*b)
      turunan1dua = round(turunan1dua,5)
      out.config(text=turunan1dua)
   elif pilihan == 3:
      turunan2 = (f(a, 2*b, fa) - 2*(f(a, b, fa)) + f(a, 0, fa)) / (b**2)
      turunan2 = round(turunan2,5)
      out.config(text=turunan2)
   elif pilihan == 4:
      turunan2dua = ((2*f(a,0,fa)) - (5*(f(a,b,fa))) + (4*(f(a,2*b,fa))) - f(a,3*b,fa)) / ((b**3)*10)
      turunan2dua = round(turunan2dua,5)
      out.config(text=turunan2dua)
   #LANJUTT ELIFFF

   #INI BUAT KALO INPUTANNYA ABIS DI HITUNG ILANG
   #e1.delete(0, END)
   #e2.delete(0,END)
   #e3.delete(0,END)



b1 = Button(text="Turunan pertama O(h)", bg="pink", activebackground="red", border=5, relief=RIDGE, command=pilturunan1)
b1.grid(row=7, column=1, padx=50)

b1 = Button(text="Turunan pertama O(h2)", bg="pink", activebackground="red", border=5, relief=RIDGE, command=pilturunan1dua)
b1.grid(row=7, column=2, columnspan=2, padx=5)

b2 = Button(text="Turunan kedua O(h)", bg="pink", activebackground="red", border=5, relief=RIDGE, command=pilturunan2)
b2.grid(row=8, column=1, padx=50)

b2 = Button(text="Turunan kedua O(h2)", bg="pink", activebackground="red", border=5, relief=RIDGE, command=pilturunan2dua)
b2.grid(row=8, column=2, columnspan=2, padx=5)

run = Button(text="HITUNG", border=6, relief=GROOVE, command=turunan, bg="light green", font=("Times New Roman", 12, "bold"))
run.grid(row=9, column=1, columnspan=5, pady=20)

labout = Label(text="OUTPUT", font=("Times New Roman", 12, "bold"))
labout.grid(row=10, column=0, columnspan=5)

out = Label(text="", font=("Times New Roman", 15, "bold"))
out.grid(row=11, column=0, columnspan=5, pady=20)

c = Label(text="Tugas Metode Numerik", borderwidth=1, relief="solid")
c.grid(row=12, column=0, columnspan=5, pady=10)
  
root.mainloop()