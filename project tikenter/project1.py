import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from PIL import ImageTk , Image
import random  , math , time
from Crypto import Random
from sympy import *
from github import *

window = Tk()
window.geometry('850x800+500+50')
window.resizable(width=False , height=False)
window.title("hello tkinter")
l = Label(text="ALICE" ,font=("Arial",20,"bold")).place(x=50,y=40)
l = Label(text="BOB" ,font=("Arial",20,"bold")).place(x=720,y=40)

# open image database 
my_img = Image.open('./images/database.png')
# resized image 
resized = my_img.resize((120 , 120), Image.ANTIALIAS)
pic_database = ImageTk.PhotoImage(resized)
l2 = Label(image=pic_database).pack()

# open image user2 
user2 = Image.open("./images/user2.png")
resized2 = user2.resize((100 , 100), Image.ANTIALIAS)
pic_user2 = ImageTk.PhotoImage(resized2)
l2 = Label(image=pic_user2).place(x=50, y=80)

# #open image User
User = Image.open("./images/User.png")
resized3 = User.resize((100 , 100), Image.ANTIALIAS)
pic_user = ImageTk.PhotoImage(resized3)
l2 = Label(image=pic_user).place(x=700, y=80)

# # open image hacker 
hacker = Image.open("./images/hacker.png")
resized4 = hacker.resize((160 , 160), Image.ANTIALIAS)
pic_hacker = ImageTk.PhotoImage(resized4)
l2 = Label(image=pic_hacker).place(x=347, y=430)

# this for Alice
N = tk.StringVar()
l = Label(text="n" ,font=20).place(x=100,y=198)
text = tk.Entry(width=10, textvariable=N).place(x=120,y=200)

CLE_P = tk.StringVar()
l = Label(text="Public key" ,font=20).place(x=15,y=229)
text = tk.Entry(width=10 , textvariable=CLE_P).place(x=120,y=230)

CLE_pr = tk.StringVar()
l = Label(text="Private key" ,font=20).place(x=15,y=260)
text = tk.Entry(width=10 , textvariable=CLE_pr).place(x=120,y=260)

# and this for Bob
N2 = tk.StringVar()
l = Label(text="n" ,font=20).place(x=710,y=198)
text = tk.Entry(width=10, textvariable=N2).place(x=730,y=200)

CLE_P2 = tk.StringVar()
l = Label(text="Public key" ,font=20).place(x=620,y=229)
text = tk.Entry(width=10 , textvariable=CLE_P2).place(x=730,y=230)

CLE_pr2 = tk.StringVar()
l = Label(text="Private key" ,font=20).place(x=625,y=260)
text = tk.Entry(width=10 , textvariable=CLE_pr2).place(x=730,y=260)

# calculate n 


#   2. calculate n=p*q
def get_n(p,q):
    n = p*q
    return n

#   3. calculate t(n)=(p-1)*(q-1)
def get_phi(p,q):
    phi = (p-1)*(q-1)
    return phi ;

def get_e(phi):
    e=2 #prime number starts from 2
    #gcd(phi,e)=1 phi & e are relative prime
    while math.gcd(phi,e)!=1:
      e=e+1
    #  this way can find the minimal prime
    return e; 

def get_d(e, phi):
  # e is part of public key
  d = pow(e, -1, phi)
  return d

def Generer_les_clefs():
    # get the value of tn n e d
    global p_A
    global q_A
    global CLE_pr
    p_A = random.randint(0, 1000)
    q_A = random.randint(0, 1000)
    n=get_n(p_A,q_A)
    phi=get_phi(p_A,q_A)
    e=get_e(phi)
    d=get_d(e, n) 
    N.set(n)
    CLE_P.set(e+n)
    CLE_pr.set(d+n)
    # print public key and private key
    print ("Public Key:(",e+n,")")
    print ("Private Key:(",d+n,")")
    
def Generer_les_clefs2():
    # get the value of tn n e d
    global p_B
    global q_B
    global d
    p_B = random.randint(0, 1000)
    q_B = random.randint(0, 1000)
    n=get_n(p_B,q_B)
    phi=get_phi(p_B,q_B)
    e=get_e(phi)
    d=get_d(e, n) 
    N2.set(n)
    CLE_P2.set(e+n)
    CLE_pr2.set(d+n)
    # print public key and private key
    print ("Public Key:(",e+n,")")
    print ("Private Key:(",d+n,")")
    
 
# button of Alice
button = tk.Button(text='Generate the keys',command=Generer_les_clefs , cursor='hand2',takefocus = 0 ).place(x=120,y=290)

# button of Bob
button = Button(text='Generate the keys' ,command=Generer_les_clefs2 , cursor='hand2',takefocus = 0).place(x=700,y=290)

# for Alice
msg= Entry(width=25)
msg.place(x=10,y=325)

# for Bob
msg2 = Entry(width=25)
msg2.place(x=644,y=325)

# for Alice
Signer = Checkbutton(window, text ='Signer' ,command= lambda: Sign(), takefocus = 0).place(x = 180, y = 325)

# for Bob
Signer = Checkbutton(window, text ='Signer', takefocus = 0).place(x = 580, y = 325)

#Send Alice
envoyer = Button(text='Send' ,command = lambda: newmsg() , cursor='hand2',takefocus = 0).place(x=10,y=350)

#Send Bob
envoyer = Button(text='Send',command= lambda: newmsg2() , cursor='hand2',takefocus = 0).place(x=720,y=350)

# line 
w = Canvas(window, width=850, height=3, bg="gray").place(x=0 , y=400)

l = Label(text="ALICE" ,font=("Arial",20,"bold")).place(x=230,y=450)
l = Label(text="BOB" ,font=("Arial",20,"bold")).place(x=550,y=450)

def newmsg():
        butt = tk.Button(window, text="New msg",font=("Arial",14),bg="lightgreen",width=8,height=1,command= lambda:getmsg())
        butt.place(x=560, y=70)
        #  hack1.insert(0,n)

def newmsg2():
         butta =tk.Button(window, text="New msg",font=("Arial",14),bg="lightgreen",width=8,height=1,command= lambda:getmsg1())
         butta.place(x=200, y=70)
        #  hack2.insert(0,n)


def  getmsg():
         global top
         global chifreee
         global dechiffree
         msg1 = msg.get()
         print(msg1)
         a=chiffre(f[0], f[1], msg1)
         top = Tk()     
         top.geometry('400x160')
         top.resizable(width=False , height=False)
         top.title('Message')
         chifreee=chiffre(f[0], f[1], msg.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         #M chifree
         b=Label(top,text=" encrypted message :")
         b.place(x=4 , y=0)
         e = Entry(top, width=25)
         e.place(x=130 , y=0)
         e.insert(0,chifreee)
         botona = Button(top,text=" show ",command=lambda: msg11())
         botona.place(x=320 , y=20)
         return chifreee



def msg11():
    #message dechiffre
    mm=Label(top, text=" decrypted message : ")
    mm.place(x=4 , y=50)
    lo = Entry(top, width=25)
    lo.place(x=130 , y=50)
    lo.insert(0,dechiffree)


def  getmsg1():
         global top
         global chifreee
         global dechiffree
         msg = msg2.get()
         print(msg)
         a=chiffre(f[0], f[1], msg)
         top = Tk()     
         top.geometry('400x160')
         top.resizable(width=False , height=False)
         top.title('Message')
         chifreee=chiffre(f[0], f[1], msg2.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         #M chifree
         b=Label(top,text=" encrypted message :")
         b.place(x=4 , y=0)
         e = Entry(top, width=25)
         e.place(x=130 , y=0)
         e.insert(0,chifreee)
         botona = Button(top,text=" show ",command=lambda: msg11())
         botona.place(x=320 , y=20)
         return chifreee

def Sign():
         s = [str(integer) for integer in getmsg()]
         a_string = "".join(s)
         res = int(a_string)
         print(res)
         print(type(res))
         S = (res**d) % n
         #Signature
         Sm=Label(top, text="Signature : ")
         Sm.place(x=5 , y=75)
        #  lo = Entry(top, width=25)
        #  lo.place(x=130 , y=150)
        #  lo.insert(0,S)
         pm=Label(top, text="Signature 2 : ")
         pm.place(x=5 , y=130)
         M1 = ((S**get_e(phi)) % n)
         mo = Entry(top, width=25)
         mo.place(x=5 , y=100)
         mo.insert(0,M1)
         if M1 != S:
                  pm=Label(top, text="Message modifier")
                  pm.place(x=100 , y=130)
         return S

 
#for Alice
def new_win():
    win = Tk()
    win.geometry('500x160+700+100')
    win.resizable(width=False , height=False)
    win.title("hello tkinter")   
    def start(p_A,q_A):
        def sortir():
            win2.destroy()
            win.destroy()
            text = Entry(window ,textvariable=CLE_pr , width=15).place(x=220,y=570)
            l = Label(window,text="Private key" ,font=20).place(x=120,y=570)
        DEBUT = time.perf_counter()
        e.delete(0,END)
        e.insert(0,p_A)
        e2.delete(0,END)
        e2.insert(0,q_A)
        e3.delete(0,END)
        e3.insert(0,p_A*q_A)
        FIN = time.perf_counter()
        e4.delete(0,END)
        e4.insert(0, round(FIN-DEBUT, 7))
        print(p_A)
        print(q_A)
        win2 = Tk()
        win2.geometry('500x70+700+290')
        win2.resizable(width=False , height=False)
        l = Label(win2 ,text="Calculation completed" ,font=("Arial")).place(x=10,y=10)
        button = Button(win2 ,text='OK',command=sortir).place(x=400,y=40)
        return
    l = Label(win ,text="P" ,font=("Arial",16,"bold")).place(x=60,y=30)
    l = Label(win,text="Q" ,font=("Arial",16,"bold")).place(x=170,y=30)
    l = Label(win,text="N" ,font=("Arial",16,"bold")).place(x=290,y=30)
    l = Label(win,text="Temps" ,font=("Arial",16,"bold")).place(x=370,y=30)
    l = Label(win,text="ms" ,font=("Arial",13,"bold")).place(x=458,y=58)
    e = Entry(win,width=15)
    e.place(x=20,y=60)
    e2 = Entry(win  ,width=15)
    e2.place(x=135,y=60)
    e3 = Entry(win ,width=15 )
    e3.place(x=250,y=60)
    e4 = Entry(win ,width=15)
    e4.place(x=360,y=60)
    button = Button(win ,text='Start',command=lambda:start(p_A , q_A) ).place(x=90,y=100)
    button = Button(win ,text='exit',command=win.destroy , cursor='hand2',takefocus = 0 ).place(x=200,y=100)
    win.mainloop()

#for BOB
def new_win2():
    win = Tk()
    win.geometry('500x160+700+100')
    win.resizable(width=False , height=False)
    win.title("hello tkinter")     
    def start(p_B,q_B):
        def sortir():
            win2.destroy()
            win.destroy()           
            text = Entry(window ,textvariable=CLE_pr2 , width=15).place(x=530,y=570)
            l = Label(text="Private key" ,font=20).place(x=630,y=570)
        DEBUT = time.perf_counter()
        e.delete(0,END)
        e.insert(0,p_B)
        e2.delete(0,END)
        e2.insert(0,q_B)
        e3.delete(0,END)
        e3.insert(0,p_B*q_B)
        FIN = time.perf_counter()
        e4.delete(0,END)
        e4.insert(0, round(FIN-DEBUT, 7))
        print(p_B)
        print(q_B)
        win2 = Tk()
        win2.geometry('500x70+700+290')
        win2.resizable(width=False , height=False)
        l = Label(win2 ,text="Calculation completed" ,font=("Arial")).place(x=10,y=10)
        button = Button(win2 ,text='OK',command=sortir).place(x=400,y=40)
        return
    l = Label(win ,text="P" ,font=("Arial",16,"bold")).place(x=60,y=30)
    l = Label(win,text="Q" ,font=("Arial",16,"bold")).place(x=170,y=30)
    l = Label(win,text="N" ,font=("Arial",16,"bold")).place(x=290,y=30)
    l = Label(win,text="Temps" ,font=("Arial",16,"bold")).place(x=370,y=30)
    l = Label(win,text="ms" ,font=("Arial",13,"bold")).place(x=458,y=58)
    e = Entry(win,width=15)
    e.place(x=20,y=60)
    e2 = Entry(win  ,width=15)
    e2.place(x=135,y=60)
    e3 = Entry(win ,width=15 )
    e3.place(x=250,y=60)
    e4 = Entry(win ,width=15)
    e4.place(x=360,y=60)
    button = Button(win ,text='Start',command=lambda:start(p_B , q_B) ).place(x=90,y=100)
    button = Button(win ,text='exit',command=win.destroy , cursor='hand2',takefocus = 0 ).place(x=200,y=100)
    win.mainloop()
    
# for Alice
text = Entry(width=15 , textvariable=N).place(x=220,y=510)
l = Label(text="n" ,font=20).place(x=200,y=510)

text = Entry(width=15 , textvariable=CLE_P).place(x=220,y=540)
l = Label(text="Public key" ,font=20).place(x=120,y=540)

text = Entry(window , width=15).place(x=220,y=570)
l = Label(window,text="Private key" ,font=20).place(x=120,y=570)

# for Bob
text = Entry(width=15 , textvariable=N2).place(x=530,y=510)
l = Label(text="n" ,font=20).place(x=630,y=510)

text = Entry(width=15 , textvariable=CLE_P2).place(x=530,y=540)
l = Label(text="Public key" ,font=20).place(x=630,y=540)

text = Entry(width=15).place(x=530,y=570)
l = Label(text="Private key" ,font=20).place(x=630,y=570)

# button attack

# get the Private key of alice
attaque_Alice = Button(text='Attack' ,command=new_win , cursor='hand2',takefocus = 0).place(x=230,y=600)
# get the Private key of bob
attaque_Bob = Button(text='Attack',command=new_win2 , cursor='hand2',takefocus = 0).place(x=540,y=600)

l = Label(text="Hacker" ,font=("Arial",17,"bold")).place(x=375,y=580)
Signer = Checkbutton(window, text ='Signer', takefocus = 0).place(x = 20, y = 640)
envoyer = Button(text='Send' , cursor='hand2',takefocus = 0).place(x=80,y=640)
Attaque = Button(text='Attack_Alice' , cursor='hand2',command=lambda: msg12(),takefocus = 0)
Attaque.place(x=80,y=680)
text = Entry(width=25).place(x=170,y=640)
text = Entry(width=25).place(x=520,y=640)
envoyer = Button(text='Send' , cursor='hand2',takefocus = 0).place(x=690,y=640)
Attaque2 = Button(text='Attack_Bob' , cursor='hand2',command=lambda: msg13(),takefocus = 0)
Attaque2.place(x=690,y=680)
Signer = Checkbutton(window, text ='Signer', takefocus = 0).place(x = 780, y = 640)
Signer = Checkbutton(window, text ='Listen mode', takefocus = 0).place(x = 370, y = 680)


def msg12():
    #message dechiffre
    lo = Entry(width=25)
    lo.place(x=170,y=680)
    chifreee=chiffre(f[0], f[1], msg.get())
    print(chifreee)
    dechiffree=dechiffre(f[0], f[2], *chifreee)
    lo.insert(0,dechiffree)
    
def msg13():
    #message dechiffre
    lo = Entry(width=25)
    lo.place(x=520,y=680)
    chifreee=chiffre(f[0], f[1], msg2.get())
    print(chifreee)
    dechiffree=dechiffre(f[0], f[2], *chifreee)
    lo.insert(0,dechiffree)
    
window.mainloop()