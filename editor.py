#-*-coding:iso-8859-1-*-
from tkinter import *
from random import randint
from tkinter import ttk,messagebox,filedialog
import sys,math as mh
tk1=Tk()
tk1.minsize(width=300,height=140)
tk1.maxsize(width=300,height=140)
file=filedialog.askopenfilename(initialdir = "/",title = "choose file")
if file=="":
    sys.exit()
tk1.destroy()
if file==None:
    sys.exit()
try:
    rtexte=open(file,"r").readlines()
except:
    sys.exit()
fitext=''
for fit in rtexte:
    fitext=fitext+fit
master=Tk()
master.title("Editor")
xkor=1366
ykor=766
wgr=xkor,"x",ykor,"+0+0"
grö=""
for grrr in wgr:
    grö=grö+str(grrr)
master.geometry(grö)
höhe=ykor-721
breit=xkor-1226
Scrollery=Scrollbar(master,bg="green",activebackground="lightgreen",bd=5)
texted=Text(master,width=breit,height=höhe,yscrollcommand=Scrollery.set,bd=1)
Scrollery.grid(padx=1,pady=1,sticky='NS',ipady=336,rowspan=4,column=4)
texted.insert(INSERT,fitext)
Scrollery.config(command=texted.yview)
texted.place(x=20,y=1)
F4andESC=Label(master,text="Man beendet den Texteditor, indem man F4 drückt, während man ihn mit \"esc\" in Normalgröße macht.")
master.attributes("-fullscreen", True)
def exitask():
    reda=open("exask.txt","r").readline()
    tki=Tk()
    tki.title("Ausgangsfrage")
    tki.geometry("300x150")
    Label(tki,text="Wollen sie gefragt werden,\nob das Programm geschlossen wird?").pack()
    def an():
        global z
        oow=open("exask.txt","w")
        oow.write("an")
        oow.close()
        lab.configure(text="an")
        z=1
    def aus():
        global z
        oow=open("exask.txt","w")
        oow.write("aus")
        lab.configure(text="aus")
        z=0
        oow.close()
    lab=Label(tki)
    lab.configure(text=reda)
    lab.pack(side=BOTTOM)
    onB=Button(tki,text="An",command=an,width=5).pack(anchor=W)
    offB=Button(tki,text="Aus",command=aus,width=5).pack(anchor=W)
def mathErrorShow():
    error=Tk()
    error.title("Fehler")
    error.geometry("300x120")
    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
def rechner_attribut_hinzufügung():
    try:
        spectk.destroy()
    except:
        pass
    zutk=Tk()
    zutk.title("Matheinfo")
    zutk.geometry("300x120")
    Label(zutk,text="Bei den 1-Attribut-Funktionen:\nArcussinus und Arcuscosinus\nmuss man eine Zahl zwischen\n1 und 0 eingeben.",justify=LEFT).place(x=1,y=1)
    def ok():
        try:
            zutk.destroy()
        except:
            pass
        rechner_hinzu_Tk=Tk()
        rechner_hinzu_Tk.title("Rechneratribute")
        rechner_hinzu_Tk.geometry("650x350")
        Message(rechner_hinzu_Tk,text="Rechner:",fg="lightblue",bg="Orange",font=("Segoe Print",16),width=200).pack()
        Label(rechner_hinzu_Tk,text="Dies ist ein ausfürlicherer Rechner.").pack(side=BOTTOM)
        Label(rechner_hinzu_Tk,text="1-Attribut-Funktionen: ").place(x=20,y=60)
        Label(rechner_hinzu_Tk,text="2-Attribut-Funktionen: ").place(x=250,y=60)
        onattrfunk=Entry(rechner_hinzu_Tk)
        twattrfunk=Entry(rechner_hinzu_Tk)
        twattrfunk_=Entry(rechner_hinzu_Tk)
        oneaus=Label(rechner_hinzu_Tk,text="Ergebnis: ")
        twoaus=Label(rechner_hinzu_Tk,text="Ergebnis: ")
        specout=Label(rechner_hinzu_Tk,text="Besondere Ausgaben: ")
        def SIN():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                sinus=mh.sin(oneattr)
                oneaus.configure(text=sinus)
            except:
                mathErrorShow()            
        oneaus.place(x=80,y=120)
        sinusbut=Button(rechner_hinzu_Tk,text="Sinus",command=SIN).place(x=20,y=150)
        onattrfunk.place(x=80,y=90)
        def GAMMA():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                gammaz=mh.gamma(oneattr)
                oneaus.configure(text=gammaz)
            except:
                mathErrorShow()
        gammabut=Button(rechner_hinzu_Tk,text="gamma",command=GAMMA).place(x=60,y=150)
        def ROOT():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                try:
                    root=mh.sqrt(oneattr)
                    oneaus.configure(text=root)
                except:
                    oneaus.configure(text="Nicht Reelle Zahl (i)")
                    pass
            except:
                mathErrorShow()
            
        rootbut=Button(rechner_hinzu_Tk,text="Quadratwurzel",command=ROOT).place(x=113,y=150)
        def COS():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                cosi=mh.cos(oneattr)
                oneaus.configure(text=cosi)
            except:
                mathErrorShow()                
        coibut=Button(rechner_hinzu_Tk,text="Cosinus",command=COS).place(x=20,y=176)
        def TAN():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                tang=mh.tan(oneattr)
                oneaus.configure(text=tang)
            except:
                mathErrorShow()
            
        tanbu=Button(rechner_hinzu_Tk,text="Tangens",command=TAN).place(x=74,y=176)
        def ASIN():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                asinus=mh.asin(oneattr)
                oneaus.configure(text=asinus)
            except:
                mathErrorShow()
        arcussinusbut=Button(rechner_hinzu_Tk,text="Arcussinus",command=ASIN).place(x=20,y=202)
        def ACOS():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                acosinus=mh.acos(oneattr)
                oneaus.configure(text=acosinus)
            except:
                mathErrorShow()
        arcussinusbut=Button(rechner_hinzu_Tk,text="Arcuscosinus",command=ACOS).place(x=88,y=202)
        def ATAN():
            oneattr=onattrfunk.get()
            try:
                oneattr=float(oneattr)
                atang=mh.atan(oneattr)
                oneaus.configure(text=atang)
            except:
                mathErrorShow()
        arcustangens=Button(rechner_hinzu_Tk,text="Arcustangens",command=ATAN).place(x=20,y=228)
        def RAND():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                z1_=int(z1)
                z2_=int(z2)
                ran=randint(z1_,z2_)
                twoaus.configure(text=ran)
            except:
                mathErrorShow()
        Zufall=Button(rechner_hinzu_Tk,text="Zufallszahl von-bis",command=RAND).place(x=220,y=228)
        def ADD():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                z1_=float(z1)
                z2_=float(z2)
                erg=float(z1_+z2_)
                twoaus.configure(text=erg)
            except:
                twoaus.configure(text="sie müssen eine Zahl eingeben")
        Addbut=Button(rechner_hinzu_Tk,text="Addition",command=ADD).place(x=220,y=150)
        def SUB():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                erg=float(float(z1)-float(z2))
                twoaus.configure(text=erg)
            except:
                twoaus.configure(text="sie müssen eine Zahl eingeben")
        def MULT():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                erg=float(float(z1)*float(z2))
                twoaus.configure(text=erg)
            except:
                twoaus.configure(text="sie müssen eine Zahl eingeben")
        Multbut=Button(rechner_hinzu_Tk,text="Multiplikation",command=MULT).place(x=220,y=177)
        Subbut=Button(rechner_hinzu_Tk,text="Subtraktion",command=SUB).place(x=278,y=150)
        def DIV():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                erg=float(float(z1)/float(z2))
                twoaus.configure(text=erg)
            except ZeroDivisionError:
                twoaus.configure(text="sie dürfen nicht durch 0 teilen")
            except:
                twoaus.configure(text="sie müssen eine Zahl eingeben")
        divbut=Button(rechner_hinzu_Tk,text="Division",command=DIV).place(x=306,y=177)
        def EXP():
            z1=twattrfunk.get()
            z2=twattrfunk_.get()
            try:
                erg=float(float(z1)**float(z2))
                twoaus.configure(text=erg)
            except:
                twoaus.configure(text="sie müssen eine Zahl eingeben")
        expbut=Button(rechner_hinzu_Tk,text="Exponentialrechnung",command=EXP).place(x=220,y=203)
        def pi():
            specout.configure(text="3.141592653589793238464338328")
        pibut=Button(rechner_hinzu_Tk,text="PI",command=pi).place(x=420,y=150)
        def eul():
            specout.configure(text=mh.e)

        pibut=Button(rechner_hinzu_Tk,text="Eulersche-Zahl",command=eul).place(x=441,y=150)
        specout.place(x=400,y=120)
        twattrfunk.place(x=220,y=90)
        twattrfunk_.place(x=220,y=113)
        twoaus.place(x=220,y=132)
    okbut=Button(zutk,text="OK",command=ok,width=10).place(x=115,y=95)
def specialfunk():
    spectk=Tk()
    spectk.title("Special-Fuktions")
    spectk.geometry("500x350")
    exas=Button(spectk,text="Ausführlicher Rechner",command=rechner_attribut_hinzufügung).place(x=2,y=3)
    exas=Button(spectk,text="Ausgangsfrage",command=exitask).place(x=2,y=29)
Label(master,text="Beim Rechner könnte es \npassieren, dass die Zahl so \nhoch wird, dass sie nicht \nangezeigt werden kann.",justify=LEFT).place(x=1160,y=615)
speciB=Button(master,text="SPECIAL",command=specialfunk).place(x=1311,y=660)

def About():
    info=Tk()
    info.title("Info")
    info.geometry("700x400+0+0")
    def abkurinfo():
        abki=Tk()
        abki.title("Wie verwendet man das Abkürzungs Verzeichnis?")
        abki.geometry("500x450+0+0")
        Label(abki,text="Sie müssen einen Punkt an das Ende der Abkürzung setzen,\ndas Wort beispielsweise wird zu \"bsp.\" während \"u.a.\" zu unter anderem wird, ...",justify=LEFT).place(x=1,y=1)
    Label(info,text="Wo liegt das Problem?").pack()
    abkurinf=Button(info,text="Abürzungsverzeichnis",command=abkurinfo).place(x=1,y=50)
def sear():
    searth=Tk()
    searth.title("Suchen nach")
    searth.geometry("700x450")
    Message(searth,text="Suchen nach:",fg="lightblue",bg="Orange",font=("Segoe Print",16),width=200).pack()
    suw=Entry(searth)
    eing=Entry(searth)
    def delet():
        try:
            rete=texted.get("1.0","end-1c")
            reatext=rete
            suchw=suw.get()
            suwsp=reatext.split(suchw)
            clsstr=""
            for tzui in suwsp:
                clsstr=clsstr+tzui
            texted.delete("1.0",END)
            texted.insert(INSERT,clsstr)
        except:
            mistake=Tk()
            mistake.title("Fehlermeldung")
            mistake.geometry("300x120")
            suwh=suw.get()
            Label(mistake,text="%s Konnte nicht gelöscht werden."%suwh,fg="red").pack()
    def ersetz():
        try:
            rete=texted.get("1.0",END)
            reatext=rete
            suchw=suw.get()
            suwsp=reatext.split(suchw)
            clsstr=""
            rang=0
            for tzuio in suwsp:
                rang=rang+1
                egab=eing.get()
                clsstr=clsstr+tzuio+egab
            clsli=[]
            for tzu in egab:
                clsli.append(tzu)
            inte=0
            for i in clsli:
                inte=inte+1
            clslen=inte
            mincllen=-clslen
            texted.delete("1.0",END)
            texted.insert(INSERT,clsstr[:mincllen])
        except:
            mistake=Tk()
            mistake.title("Fehlermeldung")
            mistake.geometry("300x120")
            suwh=suw.get()
            Label(mistake,text="%s Konnte nicht ersetzt werden."%suwh,fg="red").pack()
    rete=texted.get("1.0","end-1c")
    reatext=rete
    but=Button(searth,text="Löschen",command=delet).place(x=45,y=120)
    ersbut=Button(searth,text="Ersetzen",command=ersetz).place(x=315,y=120)
    suw.place(x=20,y=90)
    Label(searth,text="(",font=("Times New Roman",16)).place(x=270,y=117-30)
    Label(searth,text=")",font=("Times New Roman",16)).place(x=408,y=117-30)
    eing.place(x=283,y=122-29)
    Label(searth,text="Suchzeichen: ",font=("Times New Roman",18)).place(x=20,y=60)
    Label(searth,text="Mögliches ersetzen durch: ",font=("Times New Roman",14)).place(x=240,y=65)
def sav():
    savask=Tk()
    savask.title("")
    savask.geometry("170x80+500+380")
    lab=Label(savask,text="???",fg="red",bg="lightgreen",font=("Times New Roman",16))
    lab.place(x=130,y=5)
    Label(savask,text="soll wirklich\ngespeichert werden?",justify=LEFT).place(x=5,y=2)
    def ja():
        u=open(file,"w")
        inV=texted.get("1.0","end-1c")
        u.write(inV)
        u.close()
        savask.destroy()
    def nein():
        savask.destroy()
        return
    Bja=Button(savask,text="Ja",command=ja,width=7).place(x=15,y=40)
    Bnein=Button(savask,text="Nein",command=nein,width=9).place(x=82,y=40)

def savdown(event):
    savask=Tk()
    savask.title("")
    savask.geometry("170x80+500+380")
    lab=Label(savask,text="???",fg="red",bg="lightgreen",font=("Times New Roman",16))
    lab.place(x=130,y=5)
    Label(savask,text="soll wirklich\ngespeichert werden?",justify=LEFT).place(x=5,y=2)
    def ja():
        u=open(file,"w")
        inV=texted.get("1.0","end-1c")
        u.write(inV)
        u.close()
        savask.destroy()
    def nein():
        savask.destroy()
        return
    Bja=Button(savask,text="Ja",command=ja,width=7).place(x=15,y=40)
    Bnein=Button(savask,text="Nein",command=nein,width=9).place(x=82,y=40)

master.bind("<Control-s>",savdown)
def seardown(event):
    searth=Tk()
    searth.title("Suchen nach")
    searth.geometry("700x450")
    Message(searth,text="Suchen nach:",fg="lightblue",bg="Orange",font=("Segoe Print",16),width=200).pack()
    suw=Entry(searth)
    eing=Entry(searth)
    def delet():
        try:
            rete=texted.get("1.0","end-1c")
            reatext=rete
            suchw=suw.get()
            suwsp=reatext.split(suchw)
            clsstr=""
            for tzui in suwsp:
                clsstr=clsstr+tzui
            texted.delete("1.0",END)
            texted.insert(INSERT,clsstr)
        except:
            mistake=Tk()
            mistake.title("Fehlermeldung")
            mistake.geometry("300x120")
            suwh=suw.get()
            Label(mistake,text="%s Konnte nicht gelöscht werden."%suwh,fg="red").pack()
    def ersetz():
        try:
            rete=texted.get("1.0",END)
            reatext=rete
            suchw=suw.get()
            suwsp=reatext.split(suchw)
            clsstr=""
            rang=0
            for tzuio in suwsp:
                rang=rang+1
                egab=eing.get()
                clsstr=clsstr+tzuio+egab
            clsli=[]
            for tzu in egab:
                clsli.append(tzu)
            inte=0
            for i in clsli:
                inte=inte+1
            clslen=inte
            mincllen=-clslen
            texted.delete("1.0",END)
            texted.insert(INSERT,clsstr[:mincllen])
        except:
            mistake=Tk()
            mistake.title("Fehlermeldung")
            mistake.geometry("300x120")
            suwh=suw.get()
            Label(mistake,text="%s Konnte nicht ersetzt werden."%suwh,fg="red").pack()
    rete=texted.get("1.0","end-1c")
    reatext=rete
    but=Button(searth,text="Löschen",command=delet).place(x=45,y=120)
    ersbut=Button(searth,text="Ersetzen",command=ersetz).place(x=315,y=120)
    suw.place(x=20,y=90)
    Label(searth,text="(",font=("Times New Roman",16)).place(x=270,y=117-30)
    Label(searth,text=")",font=("Times New Roman",16)).place(x=408,y=117-30)
    eing.place(x=283,y=122-29)
    Label(searth,text="Suchzeichen: ",font=("Times New Roman",18)).place(x=20,y=60)
    Label(searth,text="Mögliches ersetzen durch: ",font=("Times New Roman",14)).place(x=240,y=65)

master.bind("<Control-Tab>",seardown)
def hfunk():
    maintk=Tk()
    maintk.title("Textinfo")
    maintk.geometry("683x483+0+0")
    Label(maintk,text="""Wenn sie wissen wollen, wie man das soeben geschriebene speichert,\ndann gehen sie ins Menü auf das \"file\" Attribut.
Wenn sie darauf klicken, kommt eine Auswahl, bei welcher sie\nauf SAVE klicken müssen. Wenn sie das getahen haben, dann haben sie den Inhalt der Textdatei\nnachhaltig auf das gesetzt, was sie grade geschrieben haben.""",justify=LEFT).place(x=1,y=1)
def zeiläng():
    gettext=texted.get("1.0",END)
    zumal=Tk()
    zumal.title("Wie viele Zeichen hat mein Text")
    zumal.geometry("500x300")
    Message(zumal,text="Zeichen:",fg="orange",bg="green",font=("Arial",18),width=100).pack()
    Label(zumal,text="Wörter: ").place(x=5,y=48)
    Label(zumal,text="Alle: ").place(x=100,y=48)
    showwortlen=Label(zumal,text="")
    splgettext=gettext.split(" ")
    lenzu=0
    for zeichlen in gettext:
        lenzu+=1
    zeichlen=lenzu
    showlen=Label(zumal,text="")
    rang=0
    while not rang==zeichlen-1:
        rang=rang+1
    lenz=rang
    showlen.configure(text=lenz)
    showlen.place(x=140,y=48)
    rang=0
    while not rang==len(splgettext):
        if splgettext==None:
            continue
        rang=rang+1
    lenworttext=rang
    if lenz==0:
        lenworttext=0
    showwortlen.configure(text=lenworttext)
    showwortlen.place(x=50,y=48)
    
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="SAVE  (STRG-S)", command=sav)
filemenu.add_command(label="SEARCH (STRG-TAB)", command=sear)
specialmenu=Menu(menu)
menu.add_cascade(label="Special", menu=specialmenu)
specialmenu.add_command(label="Rechner",command=rechner_attribut_hinzufügung)
specialmenu.add_command(label="Exitask",command=exitask)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Hauptfunktion",command=hfunk)
helpmenu.add_command(label="Nebenfunktion",command=About)
infomenu=Menu(menu)
menu.add_cascade(label="Info", menu=infomenu)
infomenu.add_command(label="Zeichen", command=zeiläng)
Label(master,text="Zahl1:  ",fg="red",font=("Arial",10)).place(x=1190,y=10)
Label(master,text="Zahl2:  ",fg="red",font=("Arial",10)).place(x=1190,y=40)
Label(master,text="Sie müssen \".\"\nan Stelle von \",\"\nschreiben.",fg="blue",justify=LEFT).place(x=1160,y=120)
z1=Entry(master)
z1.place(x=1233,y=11)
z2=Entry(master)
z2.place(x=1233,y=41)
zerg=Label(master,text="Ergebnis: ",justify=LEFT)
zerg.place(x=1203,y=65)
def add():
    try:
        zah1=float(z1.get())
        zah2=float(z2.get())
        erg=zah1+zah2
        zerg.configure(text=erg)
    except:
        zerg.configure(text="Sie müssen eine\n Zahl eingeben.")
but1=Button(master,text="+Plus",command=add).place(x=1253,y=100)
def sub():
    try:
        zah1=float(z1.get())
        zah2=float(z2.get())
        erg=zah1-zah2
        zerg.configure(text=erg)
    except:
        zerg.configure(text="Sie müssen eine\n Zahl eingeben.")
but1=Button(master,text="-Minus",command=sub).place(x=1293,y=100)
def mult():
    try:
        zah1=float(z1.get())
        zah2=float(z2.get())
        erg=zah1*zah2
        zerg.configure(text=erg)
    except:
        zerg.configure(text="Sie müssen eine\n Zahl eingeben.")
but1=Button(master,text="*Mal",command=mult).place(x=1253,y=127)
def div():
    try:
        zah1=float(z1.get())
        zah2=float(z2.get())
        erg=zah1/zah2
        zerg.configure(text=erg)
    except ZeroDivisionError:
        zerg.configure(text="Sie dürfen keine Null eingeben.")
    except:
        zerg.configure(text="Sie müssen eine\n Zahl eingeben.")
but1=Button(master,text="/Geteilt",command=div).place(x=1292,y=127)
def ho():
    try:
        zah1=float(z1.get())
        zah2=float(z2.get())
        erg=zah1**zah2
        zerg.configure(text=erg)
    except:
        zerg.configure(text="Sie müssen eine\n Zahl eingeben.")
but1=Button(master,text="^Hoch",command=ho).place(x=1273,y=154)
wörtby=open("wort.txt","r").readlines()
tzuhg=""
for tzuhgp in wörtby:
    tzuhg=tzuhg+tzuhgp
opwör=tzuhg
clearler=opwör.split(" ")
wör=clearler
Wörtbuch=Message(master,text="Wörterbuch")
Wörtbuch.config(bg="red",fg="green",font=("Arial",13),width=100)
Wörtbuch.place(x=1213,y=370)
wörtwort=Entry(master,justify=LEFT)
wörtvorh=Label(master,text="-------------")
def wörtsuch():
    wörterw=wörtwort.get()
    if wörterw=="":
        wörtvorh.configure(text="")
    elif wörterw in wör:
        wörtvorh.configure(text="vorhanden")
    elif not wörterw in wör:
        wörtvorh.configure(text="nicht vorhanden")
wörtvorh.place(x=1185,y=430)
wörtwort.place(x=1203,y=400)
wörtsuchb=Button(master,text="Suchen",command=wörtsuch).place(x=1280,y=430)
Label(master,text="Pfad: ").place(x=1160,y=490)
pfad=Label(master,bd=3,bg="black",fg="white",justify=LEFT,underline=0)
filelen=len(file)
enter=0
for lendefi in range(1,filelen+1):
    zahllen=lendefi%5
    if zahllen==0:
        enter+=1
pfte=str("")
zumte=[]
for i in range(1,filelen+1):
    zui=i%36
    for t in file:
        zumte.append(t)
    if not zui==0:
        buchst=zumte[i]
        pfte=pfte+buchst
    elif zui==0:
        buchst="\n"+zumte[i]
        pfte=pfte+buchst
none=[]
for lol in pfte:
    none.append(lol)
none.insert(0,pfte[-1])
del(none[-1])
txtc="".join(none)
pfad.configure(text=txtc)
pfad.place(x=1152,y=520)
z=int(1)
oo=open("exask.txt","r").readline()
if oo=="an":
    z=1
else:
    z=0
def closeask():
    if z==1:
        r=messagebox.askyesno("Beenden","Soll das Programm\nwirklich geschlossen werden?",icon="warning")
        if r==True:
            master.destroy()
            sys.exit()
        elif r==False:
            pass
    elif z==0:
        master.destroy()
        sys.exit()
def closeaske(event):
    if master.attributes("-fullscreen")==True:
        master.attributes("-fullscreen",False)
        F4andESC.config(text="Man beendet den Texteditor, indem man F4 drückt, während man ihn mit \"esc\" zu Vollbild macht.")
        master.deiconify()
    elif master.attributes("-fullscreen")==False:
        master.attributes("-fullscreen",True)
        F4andESC.config(text="Man beendet den Texteditor, indem man F4 drückt, während man ihn mit \"esc\" in Normalgröße macht.")
        master.deiconify()
master.protocol("WM_DELETE_WINDOW",closeask)
master.bind("<Escape>",closeaske)
F4andESC.place(x=350,y=730)
mainloop()
