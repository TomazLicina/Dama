__author__ = 'T L'

polja = []
poteza = False
drugic = []
mores = {}
drugic_vzames = 0
mores_vzeti = 0

with open("save.txt", 'r') as f:
    for i in f.readline():
        if i != "\n":
            polja.append(int(i))
    igralec = int(f.readline())
    katera_figura = int(f.readline())
    katero_polje = int(f.readline())

def Reset():
    global igralec
    global katera_figura
    global katero_polje
    global poteza
    global polja
    global mores_vzeti
    global drugic_vzames
    global drugic
    global mores
    igralec = 0
    poteza = 0
    katera_figura = 0
    katero_polje = 0
    mores_vzeti = 0
    drugic_vzames = 0
    drugic = []
    mores = {}
    polja = [
    0, 2, 0, 2, 0, 2, 0, 2,
    2, 0, 2, 0, 2, 0, 2, 0,
    0, 2, 0, 2, 0, 2, 0, 2,
    1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    3, 0, 3, 0, 3, 0, 3, 0,
    0, 3, 0, 3, 0, 3, 0, 3,
    3, 0, 3, 0, 3, 0, 3, 0,
    9, 9, 9, 9, 9, 9, 9, 9]
    Narisi()
    return

svetla ="wheat2"
temna = "saddle brown"

leva_stran = [8, 24, 40, 56, 1, 17, 33, 49]
desna_stran = [7, 23, 39, 55, 14, 30, 46, 62]
gori = [1, 3, 5, 7]
doli = [56, 58, 60, 62]


def Modra():
    global temna
    global svetla
    temna = "steel blue"
    svetla = "white"
    Narisi()
    return

def Green():
    global temna
    global svetla
    temna = "chartreuse4"
    svetla = "mint cream"
    Narisi()
    return

def Brown():
    global temna
    global svetla
    temna = "saddle brown"
    svetla = "wheat2"
    Narisi()
    return

def Black():
    global temna
    global svetla
    temna = "antique white4"
    svetla = "ivory2"
    Narisi()
    return

def Pink():
    global temna
    global svetla
    temna = "orchid3"
    svetla = "lavender blush"
    Narisi()
    return

def checkboard(x = 0):
    global igralec
    global mores
    global mores_vzeti

    for i in range(63):
        if igralec == 0:
            if i in leva_stran:
                if polja[i] == 3:
                    if (polja[i - 7] == 2 or polja[i - 7] == 4) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    x += 1
                elif polja[i] == 5:
                    if (polja[i - 7] == 2 or polja[i - 7] == 4) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    if (polja[i + 9] == 2 or polja[i + 9] == 4) and polja[i + 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 18
                        else:
                            mores[i] = i + 18
                    x += 1
            elif i in desna_stran:
                if polja[i] == 3:
                    if (polja[i - 9] == 2 or polja[i - 9] == 4) and polja[i - 18] == 1:
                        mores[i] = i - 18
                    x += 1
                elif polja[i] == 5:
                    if (polja[i - 9] == 2 or polja[i - 9] == 4) and polja[i - 18] == 1:
                        mores[i] = i - 18
                    if (polja[i + 7] == 2 or polja[i + 7] == 4) and polja[i + 14] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 14
                        else:
                            mores[i] = i + 14
                    x += 1
            else:
                if polja[i] == 3:
                    if (polja[i - 7] == 2 or polja[i - 7] == 4) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    if (polja[i - 9] == 2 or polja[i - 9] == 4) and polja[i - 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i - 18
                        else:
                            mores[i] = i - 18
                    x += 1

                elif polja[i] == 5:
                    if (polja[i - 7] == 2 or polja[i - 7] == 4) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    if (polja[i + 9] == 2 or polja[i + 9] == 4) and polja[i + 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 18
                        else:
                            mores[i] = i + 18
                    if (polja[i - 9] == 2 or polja[i - 9] == 4) and polja[i - 18] == 1:
                        if i in mores.keys() and i + 100 in mores.keys():
                            mores[i + 200] = i - 18
                        elif i in mores.keys():
                            mores[i + 100] = i - 18
                        else:
                            mores[i] = i - 18
                    if (polja[i + 7] == 2 or polja[i + 7] == 4) and polja[i + 14] == 1:
                        if i + 200 in mores.keys() and i + 100 in mores.keys() and i in mores.keys():
                            mores[i + 300] = i + 14
                        elif i + 100 in mores.keys() and i in mores.keys():
                            mores[i + 200] = i + 14
                        elif i in mores.keys():
                            mores[i + 100] = i + 14
                        else:
                            mores[i] = i + 14
                    x += 1

        else:
            if i in leva_stran:
                if polja[i] == 2:
                    if (polja[i + 9] == 3 or polja[i + 9] == 5) and polja[i + 18] == 1:
                        mores[i] = i + 18
                    x += 1

                elif polja[i] == 4:
                    if (polja[i - 7] == 3 or polja[i - 7] == 5) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    if (polja[i + 9] == 3 or polja[i + 9] == 5) and polja[i + 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 18
                        else:
                            mores[i] = i + 18
                    x += 1
            elif i in desna_stran:
                if polja[i] == 2:
                    if (polja[i + 7] == 3 or polja[i + 7] == 5) and polja[i + 14] == 1:
                        mores[i] = i + 14
                    x += 1
                elif polja[i] == 4:
                    if (polja[i - 9] == 3 or polja[i - 9] == 5) and polja[i - 18] == 1:
                        mores[i] = i - 18
                    if (polja[i + 7] == 3 or polja[i + 7] == 5) and polja[i + 14] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 14
                        else:
                            mores[i] = i + 14
                    x += 1

            else:
                if polja[i] == 2:
                    if (polja[i + 7] == 3 or polja[i + 7] == 5) and polja[i + 14] == 1:
                        mores[i] = i + 14
                    if (polja[i + 9] == 3 or polja[i + 9] == 5) and polja[i + 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 18
                        else:
                            mores[i] = i + 18
                    x += 1

                elif polja[i] == 4:
                    if (polja[i - 7] == 3 or polja[i - 7] == 5) and polja[i - 14] == 1:
                        mores[i] = i - 14
                    if (polja[i + 9] == 3 or polja[i + 9] == 5) and polja[i + 18] == 1:
                        if i in mores.keys():
                            mores[i + 100] = i + 18
                        else:
                            mores[i] = i + 18
                    if (polja[i - 9] == 3 or polja[i - 9] == 5) and polja[i - 18] == 1:
                        if i in mores.keys() and i + 100 in mores.keys():
                            mores[i + 200] = i - 18
                        elif i in mores.keys():
                            mores[i + 100] = i - 18
                        else:
                            mores[i] = i - 18
                    if (polja[i + 7] == 3 or polja[i + 7] == 5) and polja[i + 14] == 1:
                        if i + 200 in mores.keys() and i + 100 in mores.keys() and i in mores.keys():
                            mores[i + 300] = i + 14
                        elif i + 100 in mores.keys() and i in mores.keys():
                            mores[i + 200] = i + 14
                        elif i in mores.keys():
                            mores[i + 100] = i + 14
                        else:
                            mores[i] = i + 14
                    x += 1
    if x == 0:
        victory(igralec)
    if mores != {}:
        mores_vzeti = 1
    print(x)
    print(mores)
    return

def drugic_check(polje):
    global drugic
    global drugic_vzames
    global katera_figura
    global katero_polje
    if polje in leva_stran:
        if polja[polje] == 3:
            if (polja[polje - 7] == 2 or polja[polje - 7] == 4) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
        elif polja[polje] == 5:
            if (polja[polje - 7] == 2 or polja[polje - 7] == 4) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
            if (polja[polje + 9] == 2 or polja[polje + 9] == 4) and polja[polje + 18] == 1:
                drugic.append(polje + 18)
        elif polja[polje] == 2:
            if (polja[polje + 9] == 3 or polja[polje + 9] == 5) and polja[polje + 18] == 1:
                drugic.append(polje + 18)
        elif polja[polje] == 4:
            if (polja[polje - 7] == 3 or polja[polje - 7] == 5) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
            if (polja[polje + 9] == 3 or polja[polje + 9] == 5) and polja[polje + 18] == 1:
               drugic.append(polje +18)

    elif polje in desna_stran:
        if polja[polje] == 3:
            if (polja[polje - 9] == 2 or polja[polje - 9] == 4) and polja[polje - 18] == 1:
               drugic.append(polje - 18)
        elif polja[polje] == 5:
            if (polja[polje - 9] == 2 or polja[polje - 9] == 4) and polja[polje - 18] == 1:
                drugic.append(polje - 18)
            if (polja[polje + 7] == 2 or polja[polje + 7] == 4) and polja[polje + 14] == 1:
                drugic.append(polje + 14)
        if polja[polje] == 2:
            if (polja[polje + 7] == 3 or polja[polje + 7] == 5) and polja[polje + 14] == 1:
                drugic.append(polje + 14)
        elif polja[polje] == 4:
            if (polja[polje - 9] == 3 or polja[polje - 9] == 5) and polja[polje - 18] == 1:
               drugic.append(polje - 18)
            if (polja[polje + 7] == 3 or polja[polje + 7] == 5) and polja[polje + 14] == 1:
                drugic.append(polje + 14)

    else:
        if polja[polje] == 2:
            if (polja[polje + 7] == 3 or polja[polje + 7] == 5) and polja[polje + 14] == 1:
                drugic.append(polje + 14)
            if (polja[polje + 9] == 3 or polja[polje + 9] == 5) and polja[polje + 18] == 1:
               drugic.append(polje + 18)

        elif polja[polje] == 4:
            if (polja[polje - 7] == 3 or polja[polje - 7] == 5) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
            if (polja[polje + 9] == 3 or polja[polje + 9] == 5) and polja[polje + 18] == 1:
                drugic.append(polje + 18)
            if (polja[polje - 9] == 3 or polja[polje - 9] == 5) and polja[polje - 18] == 1:
                drugic.append(polje - 18)
            if (polja[polje + 7] == 3 or polja[polje + 7] == 5) and polja[polje + 14] == 1:
                drugic.append(polje + 14)

        if polja[polje] == 3:
            if (polja[polje - 7] == 2 or polja[polje - 7] == 4) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
            if (polja[polje - 9] == 2 or polja[polje - 9] == 4) and polja[polje - 18] == 1:
               drugic.append(polje - 18)

        elif polja[polje] == 5:
            if (polja[polje - 7] == 2 or polja[polje - 7] == 4) and polja[polje - 14] == 1:
                drugic.append(polje - 14)
            if (polja[polje + 9] == 2 or polja[polje + 9] == 4) and polja[polje + 18] == 1:
               drugic.append(polje + 18)
            if (polja[polje - 9] == 2 or polja[polje - 9] == 4) and polja[polje - 18] == 1:
                drugic.append(polje - 18)
            if (polja[polje + 7] == 2 or polja[polje + 7] == 4) and polja[polje + 14] == 1:
                drugic.append(polje + 14)
    if len(drugic) != 0:
        drugic_vzames = 1
        katero_polje = polje
        katera_figura = polja[polje]
    return

def shrani():
    with open("save.txt", 'w') as f:
        for i in polja:
            f.write(str(i))
        f.write("\n{}".format(igralec))
        f.write("\n{}".format(katera_figura))
        f.write("\n{}".format(katero_polje))

    root.destroy()

def victory(x):
    Zmaga(x)
    return


from tkinter import *

root = Tk()
root.resizable(0,0)
root.title("Dama")

beli = PhotoImage(file="beli.png")
beli_K = PhotoImage(file="beli_K.png")
crni = PhotoImage(file="crni.png")
crni_K = PhotoImage(file="crni_K.png")


"""menu"""
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Play again", command=Reset)
fileMenu.add_command(label="Exit", command=shrani)

viewMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Blue", command=Modra)
viewMenu.add_command(label="Green", command=Green)
viewMenu.add_command(label="Pink", command=Pink)
viewMenu.add_command(label="Black", command=Black)
viewMenu.add_command(label="Brown", command=Brown)


plosca = Frame(root)
plosca.grid(row=0, column=1)

kazalec = Frame(root)
kazalec.grid(row=0, column=0)

class Zmaga:

    def __init__(self, x):
        self.x = x
        if x == 1:
            niz = "Črni je zmagal"
        else:
            niz = "Rdeči je zmagal"
        self.top = Toplevel(root)
        self.label = Label(self.top, text=niz)
        self.label.pack()
        self.button = Button(self.top, text="Igraj ponovno", command=self.kill)
        self.button.pack()

    def kill(self):
        Reset()
        self.top.destroy()

class Kazalec:

    def __init__(self, row, barva):
        self.row = row
        self.barva = barva
        self.canvas = Canvas(kazalec, bg = barva, height=210, width=50)
        self.canvas.grid(row=row)

class Polje:

    def __init__(self, stevilo):
        self.stevilo = stevilo
        if polja[stevilo] == 0:
            self.barva = svetla
        else:
            self.barva = temna
        self.canvas = Canvas(plosca, bg=self.barva, width=50, height=50)
        self.canvas.grid(row=self.stevilo // 8, column=self.stevilo % 8)
        self.canvas.bind("<Button-1>", self.premik)

        if polja[stevilo] == 2:
            self.canvas.create_image(27, 27, image=beli)
        elif polja[stevilo] == 4:
            self.canvas.create_image(27, 27, image=beli_K)
        elif polja[stevilo] == 3:
            self.canvas.create_image(27, 27, image=crni)
        elif polja[stevilo] == 5:
            self.canvas.create_image(27, 27, image=crni_K)

    def premik(self, stevilo):
        global igralec
        global mores_vzeti
        global drugic_vzames
        if drugic_vzames == 1:
            return self.drugic_premik()
        elif mores_vzeti == 1:
            return self.mores_premik()
        elif igralec == 0:
            return self.crni_premik()
        else:
            return self.beli_premik()

    def drugic_premik(self):
        global igralec
        global katera_figura
        global katero_polje
        global drugic
        global drugic_vzames
        if self.stevilo in drugic:
            polja[katero_polje] = 1
            polja[int((katero_polje + self.stevilo) / 2)] = 1
            if self.stevilo in gori:
                if katera_figura == 3:
                    polja[self.stevilo] = 5
                else:
                    polja[self.stevilo] = katera_figura
            elif self.stevilo in doli:
                if katera_figura == 2:
                    polja[self.stevilo] = 4
                else:
                    polja[self.stevilo] = katera_figura
            else:
                polja[self.stevilo] = katera_figura
            drugic = []
            drugic_vzames = 0
            drugic_check(self.stevilo)
            if drugic_vzames == 0:
                if igralec == 1:
                    igralec = 0
                else:
                    igralec = 1
                checkboard()
            Narisi()

        return

    def mores_premik(self):
        global poteza
        global igralec
        global katera_figura 
        global katero_polje
        global mores
        global mores_vzeti

        
        if self.stevilo in mores.keys():
            katera_figura = polja[self.stevilo]
            katero_polje = self.stevilo
            poteza = True
        
        elif poteza and (self.stevilo == mores.get(katero_polje) or self.stevilo == mores.get(katero_polje + 100) or self.stevilo == mores.get(katero_polje + 200) or self.stevilo == mores.get(katero_polje + 300)):
            polja[katero_polje] = 1
            polja[int((katero_polje + self.stevilo) / 2)] = 1
            if self.stevilo in gori:
                if katera_figura == 3:
                    polja[self.stevilo] = 5
                else:
                    polja[self.stevilo] = katera_figura
            elif self.stevilo in doli:
                if katera_figura == 2:
                    polja[self.stevilo] = 4
                else:
                    polja[self.stevilo] = katera_figura
            else:
                polja[self.stevilo] = katera_figura
            poteza = False
            mores = {}
            mores_vzeti = 0
            drugic_check(self.stevilo)
            if drugic_vzames == 0:
                if igralec == 1:
                    igralec = 0
                else:
                    igralec = 1
                checkboard()
            Narisi()

        return

    def crni_premik(self):
        global poteza
        global igralec

        if polja[self.stevilo] == 3 or polja[self.stevilo] == 5:
            global katera_figura #prvic stisnes
            global katero_polje
            katera_figura = polja[self.stevilo]
            katero_polje = self.stevilo
            poteza = True

        elif poteza and polja[self.stevilo] == 1:
            if katero_polje in leva_stran and self.stevilo in desna_stran:
                return None

            elif katero_polje in desna_stran and self.stevilo in leva_stran:
                return None
            if katera_figura == 3:
                if (katero_polje - 7 == self.stevilo) or( katero_polje - 9 == self.stevilo):
                    if self.stevilo in gori:
                        polja[self.stevilo] = 5
                    else:
                        polja[self.stevilo] = 3
                    polja[katero_polje] = 1
                    poteza = False
                    igralec = 1
                    Narisi()
                    checkboard()

            elif katera_figura == 5:
                if (katero_polje - 7 == self.stevilo) or (katero_polje - 9 == self.stevilo) or  (katero_polje + 7 == self.stevilo) or (katero_polje + 9 == self.stevilo):
                    polja[self.stevilo] = 5
                    polja[katero_polje] = 1
                    poteza = False
                    igralec = 1
                    Narisi()
                    checkboard()

    def beli_premik(self):
        global poteza
        global igralec

        if polja[self.stevilo] == 2 or polja[self.stevilo] == 4:
            global katera_figura #prvic stisnes
            global katero_polje
            katera_figura = polja[self.stevilo]
            katero_polje = self.stevilo
            poteza = True

        if poteza and polja[self.stevilo] == 1:
            if katero_polje in leva_stran and self.stevilo in desna_stran:
                return None

            elif katero_polje in desna_stran and self.stevilo in leva_stran:
                return None
            elif katera_figura == 2:
                if (katero_polje + 7 == self.stevilo) or( katero_polje + 9 == self.stevilo):
                    if self.stevilo in doli:
                        polja[self.stevilo] = 4
                    else:
                        polja[self.stevilo] = 2
                    polja[katero_polje] = 1
                    poteza = False
                    igralec = 0
                    Narisi()
                    checkboard()

            elif katera_figura == 4:
                if (katero_polje - 7 == self.stevilo) or (katero_polje - 9 == self.stevilo) or  (katero_polje + 7 == self.stevilo) or (katero_polje + 9 == self.stevilo):
                    polja[self.stevilo] = 4
                    polja[katero_polje] = 1
                    poteza = False
                    igralec = 0
                    Narisi()
                    checkboard()

def Narisi():
    for i in range(64):
        Polje(i)
    if igralec == 0:
        Kazalec(0, svetla)
        Kazalec(1, "black")
    else:
        Kazalec(1, svetla)
        Kazalec(0, "red4")

Narisi()

checkboard()

root.mainloop()
