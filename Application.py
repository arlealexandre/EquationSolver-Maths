from tkinter import *
import math

fenetre = Tk()

# CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE

fenetre.title("Résolution d'une équation du second degrée")
fenetre.geometry('800x400')
fenetre.iconbitmap("maths.ico")
fenetre.minsize(800, 400)

# FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS 

def resoudre():

    box3 = Frame(master)
    box3.pack()

    delta = float(b.get())*float(b.get())-4*float(a.get())*float(c.get())

    if delta>0:
        
        x1 = round((-float(b.get()) - float(math.sqrt(delta))) / 2*float(a.get()), 3)
        x2 = round((-float(b.get()) + float(math.sqrt(delta))) / 2*float(a.get()), 3)

        if (float(b.get()) < 0):
            btn_plus_b = " "
        else:
            btn_plus_b = "+"

        if (float(c.get()) < 0):
            btn_plus_c = " "
        else:
            btn_plus_c = "+"

        res_box = LabelFrame(box3, text="F(x) = "+a.get()+"x²"+btn_plus_b+b.get()+"x"+btn_plus_c+c.get())
        res_box.pack()

        delta = Label(res_box, text="Delta = "+str(delta))
        delta.pack()

        res = Label(res_box, text="L'équation admet deux solutions réelles et distinctes :")
        res.pack()   

        x1 = Label(res_box, text="x1 = "+str(x1))
        x1.pack()

        x2 = Label(res_box, text="x2 = "+str(x2))
        x2.pack()

        btn_erase = Button(res_box, text="Effacer", command=lambda:[box3.pack_forget(), btn_erase.pack_forget()])
        btn_erase.pack(side=RIGHT)
        
    else:
        if delta==0:
            
            x = round((-float(b.get())) / 2*float(a.get()), 3)

            if (float(b.get()) < 0):
                btn_plus_b = " "
            else:
                btn_plus_b = "+"

            if (float(c.get()) < 0):
                btn_plus_c = " "
            else:
                btn_plus_c = "+"

            res_box = LabelFrame(box3, text="F(x) = "+a.get()+"x²"+btn_plus_b+b.get()+"x"+btn_plus_c+c.get())
            res_box.pack()

            delta = Label(res_box, text="Delta = "+str(delta))
            delta.pack()

            res = Label(res_box, text="L'équation admet une seule solution :")
            res.pack()   

            x = Label(res_box, text="x = "+str(x))
            x.pack()

            btn_erase = Button(res_box, text="Effacer", command=lambda:[box3.pack_forget(), btn_erase.pack_forget()])
            btn_erase.pack(side=RIGHT)
            
        else:

            if (float(b.get()) < 0):
                btn_plus_b = " "
            else:
                btn_plus_b = "+"

            if (float(c.get()) < 0):
                btn_plus_c = " "
            else:
                btn_plus_c = "+"

            res_box = LabelFrame(box3, text="F(x) = "+a.get()+"x²"+btn_plus_b+b.get()+"x"+btn_plus_c+c.get())
            res_box.pack()

            delta = Label(res_box, text="Delta = "+str(delta)+" < 0")
            delta.pack()
            
            res = Label(res_box, text="L'équation admet aucune solution.")
            res.pack() 

            btn_erase = Button(res_box, text="Effacer", command=lambda:[box3.pack_forget(), btn_erase.pack_forget()])
            btn_erase.pack(side=RIGHT)
    
    return

# AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE 

master = Frame(fenetre)
master.pack(fill=X)

# Box 1 

box1 = Frame(master)
box1.pack()

titre = Label(box1, text="RÉSOLUTION D'UNE ÉQUATION DU SECOND DEGRÉE", font=(22))
titre.pack(fill=X)

sous_titre = Label(box1, text="Un polynôme du second degré est une fonction f définie pour tout réel x par :\nf(x) = ax² + bx + c, où a, b et c sont trois constantes réelles avec a ≠ 0. ")
sous_titre.pack(fill=X)

# Box 2

box2 = Frame(master)
box2.pack()

a = Entry(box2, width=10)
a.insert(0, "Entrez a")
a.grid(column=1, row=1, padx=2, pady=10)

b = Entry(box2, width=10)
b.insert(0, "Entrez b")
b.grid(column=2, row=1, padx=2, pady=10)

c = Entry(box2, width=10)
c.insert(0, "Entrez c")
c.grid(column=3, row=1, padx=2, pady=2)

btn_side = Button(box2, text="Calculer", command=resoudre, width=10)
btn_side.grid(column=4, row=1, padx=2, pady=2)

# Box 3

box3 = Frame(master)
box3.pack()

fenetre.mainloop()