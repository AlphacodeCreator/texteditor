#-*-coding:iso-8859-1-*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import math as mh
from tkinter import filedialog
tk1=Tk()
file=filedialog.askopenfilename(initialdir = "/",title = "choose file")
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
Scrollery.pack(side=LEFT,fill=Y)
texted.insert(INSERT,fitext)
Scrollery.config(command=texted.yview)
texted.place(x=20,y=1)
Label(master,text="Man beendet den Texteditor, indem man F4 drückt, während man ihn mit \"esc\" in normalgröße macht.").place(x=350,y=730)
master.attributes("-fullscreen", True)
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
    bild=PhotoImage(file="shutdown.png")
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
    bild=PhotoImage(file="shutdown.png")
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
msg=Message(master,text="Abkürzungen")
msg.config(bg="red",fg="green",font=("Arial",13),width=100)
msg.place(x=1210,y=240)
abkur=Entry(master)
abkur.place(x=1203,y=270)
bedeut=Label(master,text="Bedeutung:")
def such():
    abkutte=str(abkur.get())
    if abkutte=="afrikan.":
        bedeut.configure(text="afrikanisch")
    elif abkutte=="Abg.":
        bedeut.configure(text="Abgeordnete(r)")
    elif abkutte=="Abh.":
        bedeut.configure(text="Abhandlung")
    elif abkutte=="":
        bedeut.configure(text="")
    elif abkutte=="":
        bedeut.configure(text="")
    elif abkutte=="":
        bedeut.configure(text="")
    elif abkutte=="":
        bedeut.configure(text="")
    elif abkutte=="Abb.":
        bedeut.configure(text="Abbildung")
    elif abkutte=="Abf.":
        bedeut.configure(text="Abfahrt")
    elif abkutte=="abds.":
        bedeut.configure(text="abends")
    elif abkutte=="Abl." or abkutte=="abl.":
        bedeut.configure(text="Ablativ (Lateinischer Fall)")
    elif abkutte=="äqypt.":
        bedeut.configure(text="ägyptisch")
    elif abkutte=="Akk.":
        bedeut.configure(text="Akkusativ (Fall)")
    elif abkutte=="altgriech.":
        bedeut.configure(text="altgriechisch")
    elif abkutte=="altnord.":
        bedeut.configure(text="altnordisch")
    elif abkutte=="americ.":
        bedeut.configure(text="amerikanisch")
    elif abkutte=="aram.":
        bedeut.configure(text="aramäisch")
    elif abkutte=="angelsächs.":
        bedeut.configure(text="angelsächsisch")
    elif abkutte=="arab.":
        bedeut.configure(text="arabisch")
    elif abkutte=="Art.":
        bedeut.configure(text="Artikel\n(Vorwort)")
    elif abkutte=="austral.":
        bedeut.configure(text="australisch")
    elif abkutte=="aztex.":
        bedeut.configure(text="aztekich")
    elif abkutte=="nom." or abkutte=="Nom.":
        bedeut.configure(text="Nominativ (Fall)")
    elif abkutte=="bes.":
        bedeut.configure(text="besonders")
    elif abkutte=="Best.":
        bedeut.configure(text="Bestimmung")
    elif abkutte=="Bez.":
        bedeut.configure(text="Bezeichnung")
    elif abkutte=="bildl.":
        bedeut.configure(text="bildlich")
    elif abkutte=="Bio.":
        bedeut.configure(text="Biologie")
    elif abkutte=="Bot.":
        bedeut.configure(text="Botanik")
    elif abkutte=="breton.":
        bedeut.configure(text="bretonisch")
    elif abkutte=="Bruchz.":
        bedeut.configure(text="Bruchzahl")
    elif abkutte=="Bw.":
        bedeut.configure(text="Bewohner")
    elif abkutte=="bzw.":
        bedeut.configure(text="beziehungsweise")
    elif abkutte=="bsp.":
        bedeut.configure(text="beispielsweise/\nBeispiel")
    elif abkutte=="chines.":
        bedeut.configure(text="chinisisch")
    elif abkutte=="dän.":
        bedeut.configure(text="dänisch")
    elif abkutte=="Dat.":
        bedeut.configure(text="Dativ (Fall)")
    elif abkutte=="demonstr.":
        bedeut.configure(text="demonstrativ\n(hinweisend)")
    elif abkutte=="d.h.":
        bedeut.configure(text="das heißt")
    elif abkutte=="dt." or abkutte=="deu.":
        bedeut.configure(text="deutsch")
    elif abkutte=="engl." or abkutte=="eng.":
        bedeut.configure(text="englisch")
    elif abkutte=="etc.":
        bedeut.configure(text="et cetera (usw.)")
    elif abkutte=="Ew.":
        bedeut.configure(text="Einwohner")
    elif abkutte=="f.":
        bedeut.configure(text="für")
    elif abkutte=="fachspr.":
        bedeut.configure(text="fachsprachlich")
    elif abkutte=="finn.":
        bedeut.configure(text="finnisch")
    elif abkutte=="franz.":
        bedeut.configure(text="französisch")
    elif abkutte=="Gastr.":
        bedeut.configure(text="Gastronomie")
    elif abkutte=="Gen." or abkutte=="gen.":
        bedeut.configure(text="Genitiv (Fall)")
    elif abkutte=="Geol.":
        bedeut.configure(text="Geologie")
    elif abkutte=="german.":
        bedeut.configure(text="germanisch")
    elif abkutte=="Ggs.":
        bedeut.configure(text="Gegensatz")
    elif abkutte=="gramm.":
        bedeut.configure(text="grammatikalisch")
    elif abkutte=="griech.":
        bedeut.configure(text="griechisch")
    elif abkutte=="ggf." or abkutte=="Ggf.":
        bedeut.configure(text="gegebenenfalls")
    elif abkutte=="hebr.":
        bedeut.configure(text="hebräisch")
    elif abkutte=="hist.":
        bedeut.configure(text="historisch")
    elif abkutte=="i. Ggs." or abkutte=="i.Ggs.":
        bedeut.configure(text="im Gegensatz")
    elif abkutte=="ind.":
        bedeut.configure(text="indisch")
    elif abkutte=="ind.":
        bedeut.configure(text="indefinitiv \n(unbestimmt)")
    elif abkutte=="indian.":
        bedeut.configure(text="indianisch")
    elif abkutte=="interj.":
        bedeut.configure(text="Interjektion (Ausruf)")
    elif abkutte=="interrog.":
        bedeut.configure(text="interrogativ (fragend)")
    elif abkutte=="ir.":
        bedeut.configure(text="irisch")
    elif abkutte=="iran.":
        bedeut.configure(text="iranisch")
    elif abkutte=="isländ.":
        bedeut.configure(text="isländisch")
    elif abkutte=="ital.":
        bedeut.configure(text="italienisch")
    elif abkutte=="jap.":
        bedeut.configure(text="japanisch")
    elif abkutte=="Jh.":
        bedeut.configure(text="Jahrhundert")
    elif abkutte=="jidd.":
        bedeut.configure(text="jiddisch")
    elif abkutte=="jmd.":
        bedeut.configure(text="jemand")
    elif abkutte=="jmdm.":
        bedeut.configure(text="jemandem")
    elif abkutte=="karib.":
        bedeut.configure(text="karibisch")
    elif abkutte=="kath.":
        bedeut.configure(text="katholisch")
    elif abkutte=="kaus.":
        bedeut.configure(text="kausal (Adverbiale\nBestimmung des Grundes)")
    elif abkutte=="kelt.":
        bedeut.configure(text="keltisch")
    elif abkutte=="kirgis.":
        bedeut.configure(text="kirgisisch")
    elif abkutte=="Konj.":
        bedeut.configure(text="Konjunktion (Bindewort)")
    elif abkutte=="kreol.":
        bedeut.configure(text="kreolisch")
    elif abkutte=="Kunstw.":
        bedeut.configure(text="Kunstwort")
    elif abkutte=="Kurzw.":
        bedeut.configure(text="Kurzwort")
    elif abkutte=="lat.":
        bedeut.configure(text="lateinisch")
    elif abkutte=="lok.":
        bedeut.configure(text="lokal (Adverbiale \nBestimmung des Ortes)")
    elif abkutte=="MA":
        bedeut.configure(text="Mittelalter")
    elif abkutte=="malai.":
        bedeut.configure(text="malaiisch")
    elif abkutte=="Math.":
        bedeut.configure(text="Mathematik")
    elif abkutte=="Med.":
        bedeut.configure(text="Medizin")
    elif abkutte=="mhd.":
        bedeut.configure(text="mittelhochdeutsch")
    elif abkutte=="mod.":
        bedeut.configure(text="modal (Adverbiale Best.\nder Art und Weise)")
    elif abkutte=="mong.":
        bedeut.configure(text="mongolisch")
    elif abkutte=="neugriech.":
        bedeut.configure(text="neugriechisch")
    elif abkutte=="niederdt.":
        bedeut.configure(text="niederdeutsch")
    elif abkutte=="niederl.":
        bedeut.configure(text="niederländisch")
    elif abkutte=="nlat.":
        bedeut.configure(text="neulateinisch")
    elif abkutte=="nordd.":
        bedeut.configure(text="norddeutsch")
    elif abkutte=="norw.":
        bedeut.configure(text="norwegisch")
    elif abkutte=="österr.":
        bedeut.configure(text="österreichisch")
    elif abkutte=="pers.":
        bedeut.configure(text="persisch")
    elif abkutte=="person.":
        bedeut.configure(text="personal (persönlich)")
    elif abkutte=="Philos.":
        bedeut.configure(text="Philosophie")
    elif abkutte=="Phys.":
        bedeut.configure(text="Physik")
    elif abkutte=="Pl." or abkutte=="Plur.":
        bedeut.configure(text="Plural")
    elif abkutte=="Pluralw.":
        bedeut.configure(text="Pluralwort")
    elif abkutte=="poln.":
        bedeut.configure(text="polnisch")
    elif abkutte=="polyn.":
        bedeut.configure(text="polynesisch")
    elif abkutte=="portugies.":
        bedeut.configure(text="portugiesisch")
    elif abkutte=="possess.":
        bedeut.configure(text="possessiv\n(besitzanzeigend)")
    elif abkutte=="Präp.":
        bedeut.configure(text="Präposition\n(Verhältniswort)")
    elif abkutte=="Pron.":
        bedeut.configure(text="Pronomen")
    elif abkutte=="Psychol.":
        bedeut.configure(text="Psychologie")
    elif abkutte=="Rechtsw.":
        bedeut.configure(text="Rechtswissenschaft")
    elif abkutte=="refl.":
        bedeut.configure(text="reflexiv (rückbezüglich)")
    elif abkutte=="relat.":
        bedeut.configure(text="relativ")
    elif abkutte=="roman.":
        bedeut.configure(text="romanisch")
    elif abkutte=="rumän.":
        bedeut.configure(text="rumänisch")
    elif abkutte=="russ.":
        bedeut.configure(text="russisch")
    elif abkutte=="s.":
        bedeut.configure(text="Siehe (oder) Seite")
    elif abkutte=="sanskr.":
        bedeut.configure(text="sanskritisch")
    elif abkutte=="schwed.":
        bedeut.configure(text="schwedisch")
    elif abkutte=="Sing.":
        bedeut.configure(text="Singular")
    elif abkutte=="span.":
        bedeut.configure(text="spanisch")
    elif abkutte=="südd.":
        bedeut.configure(text="süddeutsch")
    elif abkutte=="T.":
        bedeut.configure(text="Trennung")
    elif abkutte=="temp.":
        bedeut.configure(text="temporal")
    elif abkutte=="u.a.":
        bedeut.configure(text="unter andere/\nunter anderem")
    elif abkutte=="ugs.":
        bedeut.configure(text="umgangssprachlich")
    elif abkutte=="V.":
        bedeut.configure(text="Verb")
    elif abkutte=="Vors.":
        bedeut.configure(text="Vorsilbe")
    elif abkutte=="Wz.":
        bedeut.configure(text="Wahrenzeichen")
    elif abkutte=="zahlw.":
        bedeut.configure(text="Zahlwort")
    elif abkutte=="zw.":
        bedeut.configure(text="zwischen")
    elif abkutte=="Nr.":
        bedeut.configure(text="Nummer")
    else:
        bedeut.configure(text="(nicht vorhanden)")
bedeut.place(x=1213,y=290)
suchb=Button(master,text="Nach Abkürzung suchen",command=such).place(x=1200,y=330)
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
reda=open("exask.txt","r").readline()
z=int()
if reda=="an":
    z=1
elif reda=="aus":
    z=0
def specialfunk():
    spectk=Tk()
    spectk.title("Special-Fuktions")
    spectk.geometry("500x350")
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
                except:
                    return
                sinus=mh.sin(oneattr)
                oneaus.configure(text=sinus)
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
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
            gammabut=Button(rechner_hinzu_Tk,text="gamma",command=GAMMA).place(x=60,y=150)
            def ROOT():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                except:
                    return
                try:
                    root=mh.sqrt(oneattr)
                    oneaus.configure(text=root)
                except:
                    oneaus.configure(text="Nicht Reelle Zahl (i)")
                    pass
            rootbut=Button(rechner_hinzu_Tk,text="Quadratwurzel",command=ROOT).place(x=113,y=150)
            def COS():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                    cosi=mh.cos(oneattr)
                    oneaus.configure(text=cosi)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
                
            coibut=Button(rechner_hinzu_Tk,text="Cosinus",command=COS).place(x=20,y=176)
            def TAN():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
                tang=mh.tan(oneattr)
                oneaus.configure(text=tang)
            tanbu=Button(rechner_hinzu_Tk,text="Tangens",command=TAN).place(x=74,y=176)
            def ASIN():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                    asinus=mh.asin(oneattr)
                    oneaus.configure(text=asinus)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
                
            arcussinusbut=Button(rechner_hinzu_Tk,text="Arcussinus",command=ASIN).place(x=20,y=202)
            def ACOS():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                    acosinus=mh.acos(oneattr)
                    oneaus.configure(text=acosinus)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
            arcussinusbut=Button(rechner_hinzu_Tk,text="Arcuscosinus",command=ACOS).place(x=88,y=202)
            def ATAN():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
                atang=mh.atan(oneattr)
                oneaus.configure(text=atang)
            arcustangens=Button(rechner_hinzu_Tk,text="Arcustangens",command=ATAN).place(x=20,y=228)
            def RAND():
                oneattr=onattrfunk.get()
                try:
                    oneattr=float(oneattr)
                except:
                    error=Tk()
                    error.title("Fehler")
                    error.geometry("300x120")
                    Label(error,text="konnte nicht berechnet werden.",fg="red").pack()
                atang=mh.atan(oneattr)
                oneaus.configure(text=atang)
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
    rechn_add=Button(spectk,text="Ausfürlicher Rechner",command=rechner_attribut_hinzufügung).place(x=2,y=2)
    def exitask():
        oo=open("exask.txt","r").readline()
        if oo=="an":
            a=1
            z=a
        elif oo=="aus":
            a=0
            z=a
        tki=Tk()
        tki.title("Ausgangsfrage")
        tki.geometry("300x150")
        Label(tki,text="Wollen sie gefragt werden,\nob das Programm geschlossen wird?").pack()
        def an():
            a=1
            oow=open("C:\\Users\\Privat\\Desktop\\exask.txt","w")
            oow.write("an")
            oow.close()
            global z
            z=a
            lab.configure(text="an")
        def aus():
            a=0
            oow=open("C:\\Users\\Privat\\Desktop\\exask.txt","w")
            oow.write("aus")
            lab.configure(text="aus")
            global z
            z=a
            oow.close()
        onB=Button(tki,text="An",command=an,width=5).pack(anchor=W)
        offB=Button(tki,text="Aus",command=aus,width=5).pack(anchor=W)
        lab=Label(tki)
        lab.configure(text=oo)
        lab.pack(side=BOTTOM)
        z=a
    exas=Button(spectk,text="Ausgangsfrage",command=exitask).place(x=2,y=29)
Label(master,text="Beim Rechner könnte es \npassieren, dass die Zahl so \nhoch wird, dass sie nicht \nangezeigt werden kann.",justify=LEFT).place(x=1160,y=615)
speciB=Button(master,text="SPECIAL",command=specialfunk).place(x=1311,y=660)
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
        master.attributes("-fullscreen",False)
        master.deiconify()
master.protocol("WM_DELETE_WINDOW",closeask)
master.bind("<Escape>",closeaske)
mainloop()
