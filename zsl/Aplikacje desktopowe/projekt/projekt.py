# Piotr Gierba i Jacek Jędra 3PT

import tkinter as tk

root = tk.Tk()

root.geometry("250x150")
root.config(bg="#0e8267")
root.resizable(height=None, width=None)

label = tk.Label(master=root, text="Wybierz program", fg="white", bg="#0e8267", font="Bold")

def Figury():
    "@brief Liczenie pola i obwodu wybranej figury"
    root.destroy()

    def newWindow(a):
        # 1 - prostokąt | 2 - trójkąt | 3 - trapez | 4 - równoległobok | 5 - koło | 6 - deltoid
        newWin = tk.Tk()
        newWin.geometry("565x350")
        newWin.config(bg="#0e8267")
        newWin.resizable(height=None, width=None)
        window.destroy()
        entrya = tk.Entry(master=newWin, validate="all")
        entryb = tk.Entry(master=newWin, validate="all")
        entryc = tk.Entry(master=newWin, validate="all")
        entryd = tk.Entry(master=newWin, validate="all")
        entryh = tk.Entry(master=newWin, validate="all")

        labela = tk.Label(master=newWin, text="Podaj pierwszy bok", bg="#0e8267", fg="white")
        labelb = tk.Label(master=newWin, text="Podaj drugi bok", bg="#0e8267", fg="white")
        labelc = tk.Label(master=newWin, text="Podaj trzeci bok", bg="#0e8267", fg="white")
        labeld = tk.Label(master=newWin, text="Podaj czwarty bok", bg="#0e8267", fg="white")
        labelh = tk.Label(master=newWin, text="Podaj wysokość", bg="#0e8267", fg="white")
        labelr = tk.Label(master=newWin, text="Podaj promień", bg="#0e8267", fg="white")
        labele = tk.Label(master=newWin, text="Podaj pierwszą przekątną", bg="#0e8267", fg="white")
        labelf = tk.Label(master=newWin, text="Podaj drugą przekątną", bg="#0e8267", fg="white")
        sep1 = tk.Frame(master=newWin, height=20, bg="#0e8267")
        sep2 = tk.Frame(master=newWin, width=50, bg="#0e8267")
        sep3 = tk.Frame(master=newWin, height=30, bg="#0e8267")
        sep4 = tk.Frame(master=newWin, height=20, bg="#0e8267")

        imgrect = tk.PhotoImage(master=newWin, file="prostokat.png")
        imgtri = tk.PhotoImage(master=newWin, file="trojkat.gif")
        imgtra = tk.PhotoImage(master=newWin, file="trapez1.gif")
        imgpara = tk.PhotoImage(master=newWin, file="rwnolegobok.gif")
        imgcir = tk.PhotoImage(master=newWin, file="kolo.gif")
        imgdelto = tk.PhotoImage(master=newWin, file="delto.png")

        rectlabel = tk.Label(master=newWin, image=imgrect)
        trilabel = tk.Label(master=newWin, image=imgtri)
        tralabel = tk.Label(master=newWin, image=imgtra)
        paralabel = tk.Label(master=newWin, image=imgpara)
        cirlabel = tk.Label(master=newWin, image=imgcir)
        deltolabel = tk.Label(master=newWin, image=imgdelto)

        result = tk.Label(master=newWin, bg="#0bd4a5")
        result2 = tk.Label(master=newWin, bg="#0bd4a5")

        def rect():
            "@brief Pole prostokąta"
            a = entrya.get()
            b = entryb.get()
            if a:
                if b:
                    res = float(a) * float(b)
                    result.config(text=res)

        def rectcir():
            "@brief Obwód prostokąta"
            a = entrya.get()
            b = entryb.get()
            if a:
                if b:
                    res = float(a) * 2 + float(b) * 2
                    result2.config(text=res)

        def tri():
            "@brief Pole trójkąta"
            a = entrya.get()
            h = entryh.get()
            if a:
                if h:
                    res = float(a) * float(h) / 2
                    result.config(text=res)

        def tricir():
            "@brief Obwód trójkąta"
            a = entrya.get()
            b = entryb.get()
            c = entryc.get()
            if a:
                if b:
                    if c:
                        res = float(a) + float(b) + float(c)
                        result2.config(text=res)

        def tra():
            "@brief Pole trapezu"
            a = entrya.get()
            b = entryb.get()
            h = entryh.get()
            if a:
                if b:
                    if h:
                        res = (float(a) + float(b)) * float(h) / 2
                        result.config(text=res)

        def tracir():
            "@brief Obwód trapezu"
            a = entrya.get()
            b = entryb.get()
            c = entryc.get()
            d = entryd.get()
            if a:
                if b:
                    if c:
                        if d:
                            res = float(a) + float(b) + float(c) + float(d)
                            result2.config(text=res)

        def para():
            "@brief Pole równoległoboku"
            a = entrya.get()
            h = entryh.get()
            if a:
                if h:
                    res = float(a) * float(h)
                    result.config(text=res)

        def paracir():
            "@brief Obwód równoległoboku"
            a = entrya.get()
            b = entryb.get()
            if a:
                if b:
                    res = float(a) * 2 + float(b) * 2
                    result2.config(text=res)

        def cir():
            "@brief Pole koła"
            r = entrya.get()
            if r:
                r2 = float(r) * float(r)
                res = str(r2) + "π"
                result.config(text=res)

        def circir():
            "@brief Obwód koła"
            r = entrya.get()
            if r:
                r2 = 2 * float(r)
                res = str(r2) + "π"
                result2.config(text=res)

        def delto():
            "@brief Pole deltoidu"
            e = entrya.get()
            f = entryb.get()
            if e:
                if f:
                    res = float(e) * float(f) / 2
                    result.config(text=res)

        def deltocir():
            "@brief Obwód deltoidu"
            a = entryc.get()
            b = entryd.get()
            if a:
                if b:
                    res = 2 * float(a) + 2 * float(b)
                    result2.config(text=res)

        if a == 1:
            newWin.title("Prostokąt")
            sep1.grid(row=0, column=0)
            labela.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep2.grid(row=1, column=2)
            labelb.grid(row=1, column=3)
            entryb.grid(row=1, column=4)
            sep3.grid(row=2, column=0)

            btnrect = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: rect()
            )

            btnrectcir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: rectcir()
            )

            sep4.grid(row=4, column=0)
            btnrect.grid(row=3, column=1)
            result.grid(row=5, column=1)
            btnrectcir.grid(row=3, column=3)
            result2.grid(row=5, column=3)
            rectlabel.grid(row=6, column=2)


        elif a == 2:
            newWin.title("Trójkąt")
            sep1.grid(row=0, column=0)
            labela.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep2.grid(row=1, column=2)
            labelb.grid(row=1, column=3)
            entryb.grid(row=1, column=4)
            labelc.grid(row=2, column=0)
            entryc.grid(row=2, column=1)
            sep2.grid(row=2, column=2)
            labelh.grid(row=2, column=3)
            entryh.grid(row=2, column=4)
            sep3.grid(row=3, column=0)

            btntri = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: tri()
            )

            btntricir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: tricir()
            )

            sep4.grid(row=5, column=0)
            btntri.grid(row=4, column=1)
            result.grid(row=6, column=1)
            btntricir.grid(row=4, column=3)
            result2.grid(row=6, column=3)
            trilabel.grid(row=7, column=1, columnspan=3)

        elif a == 3:
            newWin.title("Trapez")
            sep1.grid(row=0, column=0)
            labela.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep2.grid(row=1, column=2)
            labelb.grid(row=1, column=3)
            entryb.grid(row=1, column=4)
            labelc.grid(row=2, column=0)
            entryc.grid(row=2, column=1)
            sep2.grid(row=2, column=2)
            labeld.grid(row=2, column=3)
            entryd.grid(row=2, column=4)
            labelh.grid(row=3, column=0)
            entryh.grid(row=3, column=1)
            sep3.grid(row=4, column=0)

            btntra = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: tra()
            )

            btntracir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: tracir()
            )
            sep4.grid(row=6, column=0)
            btntra.grid(row=5, column=1)
            result.grid(row=7, column=1)
            btntracir.grid(row=5, column=3)
            result2.grid(row=7, column=3)
            tralabel.grid(row=8, column=1, columnspan=3)

        elif a == 4:
            newWin.title("Równelogłobok")
            sep1.grid(row=0, column=0)
            labela.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep2.grid(row=1, column=2)
            labelb.grid(row=1, column=3)
            entryb.grid(row=1, column=4)
            labelh.grid(row=2, column=0)
            entryh.grid(row=2, column=1)
            sep3.grid(row=3, column=0)

            btnpara = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: para()
            )

            btnparacir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: paracir()
            )

            sep4.grid(row=5, column=0)
            btnpara.grid(row=4, column=1)
            result.grid(row=6, column=1)
            btnparacir.grid(row=4, column=3)
            result2.grid(row=6, column=3)
            paralabel.grid(row=7, column=1, columnspan=3)

        elif a == 5:
            newWin.title("Koło")
            newWin.geometry("225x275")
            sep1.grid(row=0, column=0)
            labelr.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep3.grid(row=2, column=0)

            btncir = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: cir()
            )

            btncircir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: circir()
            )

            sep4.grid(row=4, column=0)
            btncir.grid(row=3, column=0)
            result.grid(row=5, column=0)
            btncircir.grid(row=3, column=1)
            result2.grid(row=5, column=1)
            cirlabel.grid(row=6, column=0, columnspan=2)
        else:
            newWin.title("deltoid")
            newWin.geometry("600x340")
            sep1.grid(row=0, column=0)
            labele.grid(row=1, column=0)
            entrya.grid(row=1, column=1)
            sep2.grid(row=1, column=2)
            labelf.grid(row=1, column=3)
            entryb.grid(row=1, column=4)
            labela.grid(row=2, column=0)
            entryc.grid(row=2, column=1)
            sep2.grid(row=2, column=2)
            labelb.grid(row=2, column=3)
            entryd.grid(row=2, column=4)
            sep3.grid(row=3, column=0)

            btndelto = tk.Button(
                master=newWin,
                text="Oblicz Pole",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: delto()
            )

            btndeltocir = tk.Button(
                master=newWin,
                text="Oblicz Obwód",
                bg="greenyellow",
                height=2,
                width=10,
                font="arial 11",
                command=lambda: deltocir()
            )

            sep4.grid(row=5, column=0)
            btndelto.grid(row=4, column=1)
            result.grid(row=6, column=1)
            btndeltocir.grid(row=4, column=3)
            result2.grid(row=6, column=3)
            deltolabel.grid(row=7, column=1, columnspan=3)
        newWin.mainloop()

    window = tk.Tk()
    window.title("Figury")
    window.geometry("300x200")
    window.config(bg="#0e8267")

    btn1 = tk.Button(
        master=window,
        text="Prostokąt",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(1)
    )
    btn2 = tk.Button(
        master=window,
        text="Trójkąt",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(2)
    )
    btn3 = tk.Button(
        master=window,
        text="Trapez",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(3)
    )
    btn4 = tk.Button(
        master=window,
        text="Równoległobok",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(4)
    )
    btn5 = tk.Button(
        master=window,
        text="Koło",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(5)
    )
    btn6 = tk.Button(
        master=window,
        text="Deltoid",
        bg="greenyellow",
        width=15,
        height=2,
        command=lambda: newWindow(6)
    )

    btn1.grid(row=2, column=0, columnspan=2, padx=20, pady=12)
    btn2.grid(row=2, column=2, columnspan=2, padx=20, pady=12)
    btn3.grid(row=3, column=0, columnspan=2, padx=20, pady=12)
    btn4.grid(row=3, column=2, columnspan=2, padx=20, pady=12)
    btn5.grid(row=4, column=0, columnspan=2, padx=20, pady=12)
    btn6.grid(row=4, column=2, columnspan=2, padx=20, pady=12)

    window.mainloop()

def Jednostki():
    "@brief Przeliczanie wybranych jednostek"
    root.destroy()

    window = tk.Tk()
    window.title("Przeliczanie jednostek")
    window.configure(bg="#0e8267")
    window.resizable(width=False, height=False)
    window.geometry("390x220")

    frm_screen = tk.Frame(master=window, width=50)
    naglowek1 = tk.Label(master=frm_screen, width=30, height=5, text="Witamy w przeliczniku jednostek",
                         font=('Helvetica 15 bold'), bg="#0e8267", fg="white")
    naglowek1.grid(row=0, column=0, columnspan=4)
    frm_screen.grid(row=0, column=0, columnspan=4, pady=10)

    def dlugosc():
        window.destroy()
        window1 = tk.Tk()
        window1.title("Przeliczanie jednostek - dlugość")
        window1.configure(bg="#0e8267")
        window1.resizable(width=False, height=False)

        frm_screen1 = tk.Frame(master=window1, width=50, bg="#0e8267")
        naglowek2 = tk.Label(master=frm_screen1, width=121, height=2, text="Jednostki długości",
                             font=('Helvetica 15 bold'), bg="#0e8267", fg="white")
        t1 = tk.Label(master=frm_screen1, width=45, height=2, text="Milimetry na centymetry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t2 = tk.Label(master=frm_screen1, width=45, height=2, text="Milimetry na decymetry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t3 = tk.Label(master=frm_screen1, width=45, height=2, text="Milimetry na metry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t4 = tk.Label(master=frm_screen1, width=45, height=2, text="Milimetry na kilometry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t5 = tk.Label(master=frm_screen1, width=45, height=2, text="Centymetry na milimetry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t6 = tk.Label(master=frm_screen1, width=45, height=2, text="Centymetry na decymetry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t7 = tk.Label(master=frm_screen1, width=45, height=2, text="Centymetry na metry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t8 = tk.Label(master=frm_screen1, width=45, height=2, text="Centymetry na kilometry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t9 = tk.Label(master=frm_screen1, width=45, height=2, text="Decymetry na milimetry", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t10 = tk.Label(master=frm_screen1, width=45, height=2, text="Decymetry na centymetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t11 = tk.Label(master=frm_screen1, width=45, height=2, text="Decymetry na metry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t12 = tk.Label(master=frm_screen1, width=45, height=2, text="Decymetry na kilometry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t13 = tk.Label(master=frm_screen1, width=45, height=2, text="Metry na milimetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t14 = tk.Label(master=frm_screen1, width=45, height=2, text="Metry na centymetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t15 = tk.Label(master=frm_screen1, width=45, height=2, text="Metry na decymetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t16 = tk.Label(master=frm_screen1, width=45, height=2, text="Metry na kilometry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t17 = tk.Label(master=frm_screen1, width=45, height=2, text="Kilometry na milimetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t18 = tk.Label(master=frm_screen1, width=45, height=2, text="Kilometry na centymetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t19 = tk.Label(master=frm_screen1, width=45, height=2, text="Kilometry na decymetry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t20 = tk.Label(master=frm_screen1, width=45, height=2, text="Kilometry na metry", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        e1 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e2 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e3 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e4 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e5 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e6 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e7 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e8 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e9 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e10 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e11 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e12 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e13 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e14 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e15 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e16 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e17 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e18 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e19 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        e20 = tk.Entry(master=frm_screen1, width=25, font=('Helvetica 10 bold'))
        wynik = tk.Entry(master=frm_screen1, width=40, font=('Helvetica 30'), bg="#0bd4a5")

        def oblicz1():
            wynik.delete(0, tk.END)
            if len(e1.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e1.get())
                wyn = wart * 0.1
                wynik.insert(0, wyn)

        def oblicz2():
            wynik.delete(0, tk.END)
            if len(e2.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e2.get())
                wyn = wart * 0.01
                wynik.insert(0, wyn)

        def oblicz3():
            wynik.delete(0, tk.END)
            if len(e3.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e3.get())
                wyn = wart * 0.001
                wynik.insert(0, wyn)

        def oblicz4():
            wynik.delete(0, tk.END)
            if len(e4.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e4.get())
                wyn = wart * 0.000001
                wynik.insert(0, wyn)

        def oblicz5():
            wynik.delete(0, tk.END)
            if len(e5.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e5.get())
                wyn = wart * 10
                wynik.insert(0, wyn)

        def oblicz6():
            wynik.delete(0, tk.END)
            if len(e6.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e6.get())
                wyn = wart * 0.1
                wynik.insert(0, wyn)

        def oblicz7():
            wynik.delete(0, tk.END)
            if len(e7.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e7.get())
                wyn = wart * 0.01
                wynik.insert(0, wyn)

        def oblicz8():
            wynik.delete(0, tk.END)
            if len(e8.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e8.get())
                wyn = wart * 0.00001
                wynik.insert(0, wyn)

        def oblicz9():
            wynik.delete(0, tk.END)
            if len(e9.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e9.get())
                wyn = wart * 100
                wynik.insert(0, wyn)

        def oblicz10():
            wynik.delete(0, tk.END)
            if len(e10.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e10.get())
                wyn = wart * 10
                wynik.insert(0, wyn)

        def oblicz11():
            wynik.delete(0, tk.END)
            if len(e11.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e11.get())
                wyn = wart * 0.1
                wynik.insert(0, wyn)

        def oblicz12():
            wynik.delete(0, tk.END)
            if len(e12.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e12.get())
                wyn = wart * 0.0001
                wynik.insert(0, wyn)

        def oblicz13():
            wynik.delete(0, tk.END)
            if len(e13.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e13.get())
                wyn = wart * 1000
                wynik.insert(0, wyn)

        def oblicz14():
            wynik.delete(0, tk.END)
            if len(e14.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e14.get())
                wyn = wart * 100
                wynik.insert(0, wyn)

        def oblicz15():
            wynik.delete(0, tk.END)
            if len(e15.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e15.get())
                wyn = wart * 10
                wynik.insert(0, wyn)

        def oblicz16():
            wynik.delete(0, tk.END)
            if len(e16.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e16.get())
                wyn = wart * 0.001
                wynik.insert(0, wyn)

        def oblicz17():
            wynik.delete(0, tk.END)
            if len(e17.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e17.get())
                wyn = wart * 1000000
                wynik.insert(0, wyn)

        def oblicz18():
            wynik.delete(0, tk.END)
            if len(e18.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e18.get())
                wyn = wart * 100000
                wynik.insert(0, wyn)

        def oblicz19():
            wynik.delete(0, tk.END)
            if len(e19.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e19.get())
                wyn = wart * 10000
                wynik.insert(0, wyn)

        def oblicz20():
            wynik.delete(0, tk.END)
            if len(e20.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e20.get())
                wyn = wart * 1000
                wynik.insert(0, wyn)

        btn_mmcm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz1()
        )

        btn_mmdm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz2()
        )

        btn_mmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz3()
        )

        btn_mmkm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz4()
        )

        btn_cmmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz5()
        )

        btn_cmdm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz6()
        )

        btn_cmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz7()
        )

        btn_cmkm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz8()
        )

        btn_dmmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz9()
        )

        btn_dmcm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz10()
        )

        btn_dmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz11()
        )

        btn_dmkm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz12()
        )

        btn_m_mm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz13()
        )

        btn_mcm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz14()
        )

        btn_mdm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz15()
        )

        btn_mkm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz16()
        )

        btn_kmmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz17()
        )

        btn_kmcm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz18()
        )

        btn_kmdm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz19()
        )

        btn_kmm = tk.Button(
            master=frm_screen1,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz20()
        )

        naglowek2.grid(row=0, column=0, columnspan=10)
        frm_screen1.grid(row=0, column=0)
        t1.grid(row=1, column=0)
        e1.grid(row=2, column=0, pady=6)
        btn_mmcm.grid(row=3, column=0)
        t2.grid(row=1, column=1)
        e2.grid(row=2, column=1, pady=6)
        btn_mmdm.grid(row=3, column=1)
        t3.grid(row=1, column=2)
        e3.grid(row=2, column=2, pady=6)
        btn_mmm.grid(row=3, column=2)
        t4.grid(row=1, column=3)
        e4.grid(row=2, column=3, pady=6)
        btn_mmkm.grid(row=3, column=3)
        t5.grid(row=4, column=0)
        e5.grid(row=5, column=0, pady=6)
        btn_cmmm.grid(row=6, column=0)
        t6.grid(row=4, column=1)
        e6.grid(row=5, column=1, pady=6)
        btn_cmdm.grid(row=6, column=1)
        t7.grid(row=4, column=2)
        e7.grid(row=5, column=2, pady=6)
        btn_cmm.grid(row=6, column=2)
        t8.grid(row=4, column=3)
        e8.grid(row=5, column=3, pady=6)
        btn_cmkm.grid(row=6, column=3)
        t9.grid(row=7, column=0)
        e9.grid(row=8, column=0, pady=6)
        btn_dmmm.grid(row=9, column=0)
        t10.grid(row=7, column=1)
        e10.grid(row=8, column=1, pady=6)
        btn_dmcm.grid(row=9, column=1)
        t11.grid(row=7, column=2)
        e11.grid(row=8, column=2, pady=6)
        btn_dmm.grid(row=9, column=2)
        t12.grid(row=7, column=3)
        e12.grid(row=8, column=3, pady=6)
        btn_dmkm.grid(row=9, column=3)
        t13.grid(row=10, column=0)
        e13.grid(row=11, column=0, pady=6)
        btn_m_mm.grid(row=12, column=0)
        t14.grid(row=10, column=1)
        e14.grid(row=11, column=1, pady=6)
        btn_mcm.grid(row=12, column=1)
        t15.grid(row=10, column=2)
        e15.grid(row=11, column=2, pady=6)
        btn_mdm.grid(row=12, column=2)
        t16.grid(row=10, column=3)
        e16.grid(row=11, column=3, pady=6)
        btn_mkm.grid(row=12, column=3)
        t17.grid(row=13, column=0)
        e17.grid(row=14, column=0, pady=6)
        btn_kmmm.grid(row=15, column=0)
        t18.grid(row=13, column=1)
        e18.grid(row=14, column=1, pady=6)
        btn_kmcm.grid(row=15, column=1)
        t19.grid(row=13, column=2)
        e19.grid(row=14, column=2, pady=6)
        btn_kmdm.grid(row=15, column=2)
        t20.grid(row=13, column=3)
        e20.grid(row=14, column=3, pady=6)
        btn_kmm.grid(row=15, column=3)
        wynik.grid(row=16, column=0, columnspan=10, pady=30)

        window1.mainloop()

    def masa():
        window.destroy()
        window2 = tk.Tk()
        window2.title("Przeliczanie jednostek - masa")
        window2.configure(bg="#0e8267")
        window2.resizable(width=False, height=False)

        frm_screen2 = tk.Frame(master=window2, width=50, bg="#0e8267")
        naglowek3 = tk.Label(master=frm_screen2, width=121, height=2, text="Jednostki masy", font=('Helvetica 15 bold'),
                             bg="#0e8267", fg="white")
        t1 = tk.Label(master=frm_screen2, width=45, height=2, text="Miligramy na gramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t2 = tk.Label(master=frm_screen2, width=45, height=2, text="Miligramy na dekagramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t3 = tk.Label(master=frm_screen2, width=45, height=2, text="Miligramy na kilogramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t4 = tk.Label(master=frm_screen2, width=45, height=2, text="Miligramy na tony", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t5 = tk.Label(master=frm_screen2, width=45, height=2, text="Gramy na miligramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t6 = tk.Label(master=frm_screen2, width=45, height=2, text="Gramy na dekagramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t7 = tk.Label(master=frm_screen2, width=45, height=2, text="Gramy na kilogramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t8 = tk.Label(master=frm_screen2, width=45, height=2, text="Gramy na tony", font=('Helvetica 10'), bg="#0e8267", fg="white")
        t9 = tk.Label(master=frm_screen2, width=45, height=2, text="Dekagramy na miligramy", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t10 = tk.Label(master=frm_screen2, width=45, height=2, text="Dekagramy na gramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t11 = tk.Label(master=frm_screen2, width=45, height=2, text="Dekagramy na kilogramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t12 = tk.Label(master=frm_screen2, width=45, height=2, text="Dekagramy na tony", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t13 = tk.Label(master=frm_screen2, width=45, height=2, text="Kilogramy na miligramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t14 = tk.Label(master=frm_screen2, width=45, height=2, text="Kilogramy na gramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t15 = tk.Label(master=frm_screen2, width=45, height=2, text="Kilogramy na dekagramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t16 = tk.Label(master=frm_screen2, width=45, height=2, text="Kilogramy na tony", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t17 = tk.Label(master=frm_screen2, width=45, height=2, text="Tony na miligramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t18 = tk.Label(master=frm_screen2, width=45, height=2, text="Tony na gramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t19 = tk.Label(master=frm_screen2, width=45, height=2, text="Tony na dekagramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        t20 = tk.Label(master=frm_screen2, width=45, height=2, text="Tony na kilogramy", font=('Helvetica 10'),
                       bg="#0e8267", fg="white")
        e1 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e2 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e3 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e4 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e5 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e6 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e7 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e8 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e9 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e10 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e11 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e12 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e13 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e14 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e15 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e16 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e17 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e18 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e19 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        e20 = tk.Entry(master=frm_screen2, width=25, font=('Helvetica 10 bold'))
        wynik = tk.Entry(master=frm_screen2, width=40, font=('Helvetica 30'), bg="#0bd4a5")

        def oblicz1():
            wynik.delete(0, tk.END)
            if len(e1.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e1.get())
                wyn = wart * 0.001
                wynik.insert(0, wyn)

        def oblicz2():
            wynik.delete(0, tk.END)
            if len(e2.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e2.get())
                wyn = wart * 0.00001
                wynik.insert(0, wyn)

        def oblicz3():
            wynik.delete(0, tk.END)
            if len(e3.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e3.get())
                wyn = wart * 0.000001
                wynik.insert(0, wyn)

        def oblicz4():
            wynik.delete(0, tk.END)
            if len(e4.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e4.get())
                wyn = wart * 0.000000001
                wynik.insert(0, wyn)

        def oblicz5():
            wynik.delete(0, tk.END)
            if len(e5.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e5.get())
                wyn = wart * 1000
                wynik.insert(0, wyn)

        def oblicz6():
            wynik.delete(0, tk.END)
            if len(e6.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e6.get())
                wyn = wart * 0.1
                wynik.insert(0, wyn)

        def oblicz7():
            wynik.delete(0, tk.END)
            if len(e7.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e7.get())
                wyn = wart * 0.001
                wynik.insert(0, wyn)

        def oblicz8():
            wynik.delete(0, tk.END)
            if len(e8.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e8.get())
                wyn = wart * 0.000001
                wynik.insert(0, wyn)

        def oblicz9():
            wynik.delete(0, tk.END)
            if len(e9.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e9.get())
                wyn = wart * 10000
                wynik.insert(0, wyn)

        def oblicz10():
            wynik.delete(0, tk.END)
            if len(e10.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e10.get())
                wyn = wart * 10
                wynik.insert(0, wyn)

        def oblicz11():
            wynik.delete(0, tk.END)
            if len(e11.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e11.get())
                wyn = wart * 0.01
                wynik.insert(0, wyn)

        def oblicz12():
            wynik.delete(0, tk.END)
            if len(e12.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e12.get())
                wyn = wart * 0.00001
                wynik.insert(0, wyn)

        def oblicz13():
            wynik.delete(0, tk.END)
            if len(e13.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e13.get())
                wyn = wart * 1000000
                wynik.insert(0, wyn)

        def oblicz14():
            wynik.delete(0, tk.END)
            if len(e14.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e14.get())
                wyn = wart * 1000
                wynik.insert(0, wyn)

        def oblicz15():
            wynik.delete(0, tk.END)
            if len(e15.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e15.get())
                wyn = wart * 100
                wynik.insert(0, wyn)

        def oblicz16():
            wynik.delete(0, tk.END)
            if len(e16.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e16.get())
                wyn = wart * 0.001
                wynik.insert(0, wyn)

        def oblicz17():
            wynik.delete(0, tk.END)
            if len(e17.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e17.get())
                wyn = wart * 1000000000
                wynik.insert(0, wyn)

        def oblicz18():
            wynik.delete(0, tk.END)
            if len(e18.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e18.get())
                wyn = wart * 1000000
                wynik.insert(0, wyn)

        def oblicz19():
            wynik.delete(0, tk.END)
            if len(e19.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e19.get())
                wyn = wart * 100000
                wynik.insert(0, wyn)

        def oblicz20():
            wynik.delete(0, tk.END)
            if len(e20.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e20.get())
                wyn = wart * 1000
                wynik.insert(0, wyn)

        btn_mggr = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz1()
        )

        btn_mgdg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz2()
        )

        btn_mgki = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz3()
        )

        btn_mgto = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz4()
        )

        btn_grmg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz5()
        )

        btn_grdg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz6()
        )

        btn_grki = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz7()
        )

        btn_grto = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz8()
        )

        btn_dgmg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz9()
        )

        btn_dggr = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz10()
        )

        btn_dgki = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz11()
        )

        btn_dgto = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz12()
        )

        btn_kimg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz13()
        )

        btn_kigr = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz14()
        )

        btn_kidg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz15()
        )

        btn_kito = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz16()
        )

        btn_tomg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz17()
        )

        btn_togr = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz18()
        )

        btn_todg = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz19()
        )

        btn_toki = tk.Button(
            master=frm_screen2,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz20()
        )

        naglowek3.grid(row=0, column=0, columnspan=10)
        frm_screen2.grid(row=0, column=0)
        t1.grid(row=1, column=0)
        e1.grid(row=2, column=0, pady=6)
        btn_mggr.grid(row=3, column=0)
        t2.grid(row=1, column=1)
        e2.grid(row=2, column=1, pady=6)
        btn_mgdg.grid(row=3, column=1)
        t3.grid(row=1, column=2)
        e3.grid(row=2, column=2, pady=6)
        btn_mgki.grid(row=3, column=2)
        t4.grid(row=1, column=3)
        e4.grid(row=2, column=3, pady=6)
        btn_mgto.grid(row=3, column=3)
        t5.grid(row=4, column=0)
        e5.grid(row=5, column=0, pady=6)
        btn_grmg.grid(row=6, column=0)
        t6.grid(row=4, column=1)
        e6.grid(row=5, column=1, pady=6)
        btn_grdg.grid(row=6, column=1)
        t7.grid(row=4, column=2)
        e7.grid(row=5, column=2, pady=6)
        btn_grki.grid(row=6, column=2)
        t8.grid(row=4, column=3)
        e8.grid(row=5, column=3, pady=6)
        btn_grto.grid(row=6, column=3)
        t9.grid(row=7, column=0)
        e9.grid(row=8, column=0, pady=6)
        btn_dgmg.grid(row=9, column=0)
        t10.grid(row=7, column=1)
        e10.grid(row=8, column=1, pady=6)
        btn_dggr.grid(row=9, column=1)
        t11.grid(row=7, column=2)
        e11.grid(row=8, column=2, pady=6)
        btn_dgki.grid(row=9, column=2)
        t12.grid(row=7, column=3)
        e12.grid(row=8, column=3, pady=6)
        btn_dgto.grid(row=9, column=3)
        t13.grid(row=10, column=0)
        e13.grid(row=11, column=0, pady=6)
        btn_kimg.grid(row=12, column=0)
        t14.grid(row=10, column=1)
        e14.grid(row=11, column=1, pady=6)
        btn_kigr.grid(row=12, column=1)
        t15.grid(row=10, column=2)
        e15.grid(row=11, column=2, pady=6)
        btn_kidg.grid(row=12, column=2)
        t16.grid(row=10, column=3)
        e16.grid(row=11, column=3, pady=6)
        btn_kito.grid(row=12, column=3)
        t17.grid(row=13, column=0)
        e17.grid(row=14, column=0, pady=6)
        btn_tomg.grid(row=15, column=0)
        t18.grid(row=13, column=1)
        e18.grid(row=14, column=1, pady=6)
        btn_togr.grid(row=15, column=1)
        t19.grid(row=13, column=2)
        e19.grid(row=14, column=2, pady=6)
        btn_todg.grid(row=15, column=2)
        t20.grid(row=13, column=3)
        e20.grid(row=14, column=3, pady=6)
        btn_toki.grid(row=15, column=3)
        wynik.grid(row=16, column=0, columnspan=10, pady=40)

        window2.mainloop()

    def temperatura():
        window.destroy()
        window3 = tk.Tk()
        window3.title("Przeliczanie jednostek - temperatura")
        window3.configure(bg="#0e8267")
        window3.resizable(width=False, height=False)

        frm_screen3 = tk.Frame(master=window3, width=50, bg="#0e8267")
        naglowek4 = tk.Label(master=frm_screen3, width=60, height=5, text="Jednostki temperatury",
                             font=('Helvetica 15 bold'), bg="#0e8267", fg="white")
        t1 = tk.Label(master=frm_screen3, width=45, height=5, text="Celsjusze na Farenheity", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t2 = tk.Label(master=frm_screen3, width=45, height=5, text="Celsjusze na Kelwiny", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t3 = tk.Label(master=frm_screen3, width=45, height=5, text="Farenheity na Celsjusze", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t4 = tk.Label(master=frm_screen3, width=45, height=5, text="Farenheity na Kelwiny", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t5 = tk.Label(master=frm_screen3, width=45, height=5, text="Kelwiny na Farenheity", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        t6 = tk.Label(master=frm_screen3, width=45, height=5, text="Kelwiny na Celsjusze", font=('Helvetica 10'),
                      bg="#0e8267", fg="white")
        e1 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        e2 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        e3 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        e4 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        e5 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        e6 = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 10 bold'))
        wynik = tk.Entry(master=frm_screen3, width=25, font=('Helvetica 30'), bg="#0bd4a5")

        def oblicz1():
            wynik.delete(0, tk.END)
            if len(e1.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e1.get())
                wyn = round(wart * (9 / 5) + 32, 2)
                wynik.insert(0, wyn)

        def oblicz2():
            wynik.delete(0, tk.END)
            if len(e2.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e2.get())
                wyn = round(wart + 273.15, 2)
                wynik.insert(0, wyn)

        def oblicz3():
            wynik.delete(0, tk.END)
            if len(e3.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e3.get())
                wyn = round((wart - 32) * (5 / 9), 2)
                wynik.insert(0, wyn)

        def oblicz4():
            wynik.delete(0, tk.END)
            if len(e4.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e4.get())
                wyn = round((wart - 32) / 1.8000 + 273.15, 2)
                wynik.insert(0, wyn)

        def oblicz5():
            wynik.delete(0, tk.END)
            if len(e5.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e5.get())
                wyn = round((wart - 273.15) * 1.8000 + 32, 2)
                wynik.insert(0, wyn)

        def oblicz6():
            wynik.delete(0, tk.END)
            if len(e6.get()) == 0:
                wynik.insert(0, 0)
            else:
                wart = float(e6.get())
                wyn = round(wart - 273.15, 2)
                wynik.insert(0, wyn)

        btn_CF = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz1()
        )

        btn_CK = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz2()
        )

        btn_FC = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz3()
        )

        btn_FK = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz4()
        )

        btn_KF = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz5()
        )

        btn_KC = tk.Button(
            master=frm_screen3,
            text="Oblicz",
            bg="greenyellow",
            height=2,
            width=10,
            font="arial 11",
            command=lambda: oblicz6()
        )

        naglowek4.grid(row=0, column=0, columnspan=10)
        frm_screen3.grid(row=0, column=0)
        t1.grid(row=1, column=0)
        e1.grid(row=2, column=0, pady=6)
        btn_CF.grid(row=3, column=0)
        t2.grid(row=1, column=1)
        e2.grid(row=2, column=1, pady=6)
        btn_CK.grid(row=3, column=1)
        t3.grid(row=4, column=0)
        e3.grid(row=5, column=0, pady=6)
        btn_FC.grid(row=6, column=0)
        t4.grid(row=4, column=1)
        e4.grid(row=5, column=1, pady=6)
        btn_FK.grid(row=6, column=1)
        t5.grid(row=7, column=0)
        e5.grid(row=8, column=0, pady=6)
        btn_KF.grid(row=9, column=0)
        t6.grid(row=7, column=1)
        e6.grid(row=8, column=1, pady=6)
        btn_KC.grid(row=9, column=1)
        wynik.grid(row=10, column=0, columnspan=10, pady=40)

        window3.mainloop()

    btn_dlugosc = tk.Button(
        master=window,
        text="Długość",
        bg="greenyellow",
        height=2,
        width=10,
        font="arial 11",
        command=lambda: dlugosc()
    )

    btn_masa = tk.Button(
        master=window,
        text="Masa",
        bg="greenyellow",
        height=2,
        width=10,
        font="arial 11",
        command=lambda: masa()
    )

    btn_temperatura = tk.Button(
        master=window,
        text="Temperatura",
        bg="greenyellow",
        height=2,
        width=10,
        font="arial 11",
        command=lambda: temperatura()
    )

    btn_dlugosc.grid(row=1, column=0, pady=3, padx=15)
    btn_masa.grid(row=1, column=1, pady=3, padx=15)
    btn_temperatura.grid(row=1, column=2, pady=3, padx=15)

    window.mainloop()


btn1 = tk.Button(
    master=root,
    text="Figury",
    bg="greenyellow",
    height=2,
    width=10,
    font="arial 11",
    command=lambda: Figury()
)

btn2 = tk.Button(
    master=root,
    text="Jednostki",
    bg="greenyellow",
    height=2,
    width=10,
    font="arial 11",
    command=lambda: Jednostki()
)

label.grid(row=0, column=0, columnspan=3, pady=10)
btn1.grid(row=1, column=0, pady=30, padx=12)
btn2.grid(row=1, column=2, pady=30, padx=12)

root.mainloop()