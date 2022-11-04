from pyswip import Prolog
import numpy as np

prolog = Prolog()
prolog.consult("../ICON/Dataset/potability.pl")


def addAssert(prolog, str):
    prolog.assertz(str)


def deleteAssert(prolog, str):
    prolog.retract(str)


def query(prolog, str):
    qr = (str + ".")
    return list(prolog.query(qr))

def alto():
    print("Acqua con alto residuo fisso (>1500 mg/L) \n")
    prez=3500
    prez = float(prez)
    interval = np.arange(1500,prez, 1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-residuo(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-residuo(Marca,\"" + i + "\")"))
    print(my_list)
    

def oligominerale():
    print("Acqua Oligominerale (50-500 mg/L) \n")
    prez=500
    prez = float(prez)
    interval = np.arange(50, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-residuo(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-residuo(Marca,\"" + i + "\")"))
    print(my_list)

        
def mediominerale():
    print("Acqua mediominerale (500-1500 mg/L) \n")
    prez=1500
    prez = float(prez)
    interval = np.arange(500, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-residuo(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-residuo(Marca,\"" + i + "\")"))
    print(my_list)

def leggera():
    print("Acqua Leggera (<50 mg/L) \n")
    prez=50
    prez = float(prez)
    interval = np.arange(1, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-residuo(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-residuo(Marca,\"" + i + "\")"))
    print(my_list)
    
def mediomineralebicarbonate():
    print("Mediominerale-bicarbonate \n")
    print("Residuo: 500-1500 mg/L \n"
          "Bicarbonato: >600 mg/L")
    prez=1500
    tip=2300
    prez = float(prez)
    tip = float(tip)
    interval = np.arange(500, prez,1)
    interval1 = np.arange(600.0, tip, 1)
    my_list = []
    for i in interval:
        i = i.astype(str) 
        for p in interval1:
            p = p.astype(str)
            if (query(prolog, "marca-residuo-bicarbonati(Marca,\"" + i + "\",\"" + p + "\")")!= []):
                my_list.append(query(prolog, "marca-residuo-bicarbonati(Marca,\"" + i + "\",\"" + p + "\")"))
    print(my_list)
        
        
def mediomineralecalciche():
    print("Mediominerale-calciche \n")
    print("Residuo: 500-1500 mg/L \n"
         "Calcio: >150 mg/L")
    prez=1500
    tip=720
    prez = float(prez)
    tip = float(tip)
    interval = np.arange(500, prez,1)
    interval1 = np.arange(150.0, tip, 1)
    my_list = []
    for i in interval:
        i = i.astype(str) 
        for p in interval1:
            p = p.astype(str)
            if (query(prolog, "marca-residuo-calcio(Marca,\"" + i + "\",\"" + p + "\")")!= []):
                my_list.append(query(prolog, "marca-residuo-calcio(Marca,\"" + i + "\",\"" + p + "\")"))
    print(my_list)
    
def mediomineralemagnesiache():
    print("Mediominerale-magnesiache \n")
    print("Residuo: 500-1500 mg/L \n"
          "Magnesio: >50 mg/L")
    prez=1500
    tip=175
    prez = float(prez)
    tip = float(tip)
    interval = np.arange(500, prez,1)
    interval1 = np.arange(50.0, tip, 1)
    my_list = []
    for i in interval:
        i = i.astype(str) 
        for p in interval1:
            p = p.astype(str)
            if (query(prolog, "marca-residuo-magnesio(Marca,\"" + i + "\",\"" + p + "\")")!= []):
                my_list.append(query(prolog, "marca-residuo-magnesio(Marca,\"" + i + "\",\"" + p + "\")"))
    print(my_list)
    
def mediomineralefluorate():
    print("mediominerale-fluorate \n")
    print("Residuo: 500-1500 mg/L \n"
          "Fluoruro: >4 mg/L")
    prez=1500
    tip=10
    prez = float(prez)
    tip = float(tip)
    interval = np.arange(500, prez,1)
    interval1 = np.arange(4, tip, 1)
    my_list = []
    for i in interval:
        i = i.astype(str) 
        for p in interval1:
            p = p.astype(str)
            if (query(prolog, "marca-residuo-fluoruro(Marca,\"" + i + "\",\"" + p + "\")")!= []):
                my_list.append(query(prolog, "marca-residuo-fluoruro(Marca,\"" + i + "\",\"" + p + "\")"))
    print(my_list)
    
def neonati():
    leggera()
    print("\n")

def bambini():
    mediomineralecalciche()
    print("\n")
    mediomineralemagnesiache()
    print("\n")
    mediomineralefluorate()
    print("\n")

def adolescenti():
    mediomineralebicarbonate()
    print("\n")
    mediomineralecalciche()
    print("\n")
    mediomineralemagnesiache()
    print("\n")
    
def adulti():
    mediominerale()
    print("\n")
    oligominerale()
    print("\n")
    
def anziani():
    calciche()
    print("\n")
    solfate()
    print("\n")
    magnesiache()
    print("\n")

def incinta():
    calciche()
    print("\n")
    
def bicarbonate():
    print("Bicarbonate \n")
    print("Bicarbonato >600 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(600, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-bicarbonato(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-bicarbonato(Marca,\"" + i + "\")"))
    print(my_list)
    
def solfate():
    print("Solfate \n")
    print("Solfato >200 mg/L \n")
    prez=1900
    interval = np.arange(200, prez+0.1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-solfato(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-solfato(Marca,\"" + i + "\")"))
    print(my_list)
    
def clorurate():
    print("Clorurate \n")
    print("Cloruro >200 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(200, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-cloruro(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-cloruro(Marca,\"" + i + "\")"))
    print(my_list)
    
def calciche():
    print("Calciche \n")
    print("Calcio >150 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(150, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-calcio(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-calcio(Marca,\"" + i + "\")"))
    print(my_list)
    
def magnesiache():
    print("Magnesiache \n")
    print("Magnesio >5 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(50, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-magnesio(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-magnesio(Marca,\"" + i + "\")"))
    print(my_list)
    
def fluorate():
    print("Fluorate \n")
    print("Fluoruro >4 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(4, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-fluoruro(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-fluoruro(Marca,\"" + i + "\")"))
    print(my_list)
    
def acidule():
    print("Acidule \n")
    print("Massimo ph 7 \n")
    prez=7
    prez = float(prez)
    interval = np.arange(0, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-ph(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-ph(Marca,\"" + i + "\")"))
    print(my_list)
    
def sodiche():
    print("Sodiche \n")
    print("Sodio >200 mg/L \n")
    prez=5000
    prez = float(prez)
    interval = np.arange(200, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-sodio(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-sodio(Marca,\"" + i + "\")"))
    print(my_list)
    
def iposodiche():
    print("Iposodiche \n")
    print("Sodio <20 mg/L \n")
    prez=20
    prez = float(prez)
    interval = np.arange(0, prez+1)
    my_list = []
    for i in interval:
     i = i.astype(str)
     if (query(prolog, "marca-sodio(Marca,\"" + i + "\")")!= []):
        my_list.append(query(prolog, "marca-sodio(Marca,\"" + i + "\")"))
    print(my_list)
    
    
def residuo():
    answer1 = input("Selezionare il tipo di acqua in base al residuo fisso:\n"
               "1) Alto (Uso terapeutico)(>1500 mg/L)\n"
               "2) Oligominerale (50-500 mg/L)\n"
               "3) Medio-minerale (500-1500 mg/L)\n"
               "4) Leggera (<50 mg/L)\n"
               "X) Torna al menu principale \n"
               )
    while answer1[0] != ("x") and answer1[0] != ("X"):
        if answer1[0] == "1":
            alto()
        elif answer1[0] == "2":
            oligominerale()
        elif answer1[0] == "3":
            mediominerale()
        elif answer1[0] == "4":
            leggera()
        else:
            print("RISPOSTA ERRATA!")
        answer1 = input("Selezionare il tipo di acqua in base al residuo fisso:\n"
               "1) Alto (Uso terapeutico)(>1500 mg/L)\n"
               "2) Oligominerale (50-500 mg/L)\n"
               "3) Medio-minerale (500-1500 mg/L)\n"
               "4) Leggera (<50 mg/L)\n"
               "X) Torna al menu principale \n"
               )

def eta():
    answer1 = input("Selezionare il tipo di acqua in base all'eta' del soggetto :\n"
               "1) Neonati \n"
               "2) Bambini \n"
               "3) Adolescenti \n"
               "4) Adulti \n"
               "5) Anziani \n"
               "X) Torna al menu principale \n"
               )
    while answer1[0] != ("x") and answer1[0] != ("X"):
        if answer1[0] == "1":
            neonati()
        elif answer1[0] == "2":
            bambini()
        elif answer1[0] == "3":
            adolescenti()
        elif answer1[0] == "4":
            adulti()
        elif answer1[0] == "5":
            anziani()
        else:
            print("RISPOSTA ERRATA!")
        answer1 = input("Selezionare il tipo di acqua in base all'eta' del soggetto :\n"
               "1) Neonati \n"
               "2) Bambini \n"
               "3) Adolescenti \n"
               "4) Adulti \n"
               "5) Anziani \n"
               "X) Torna al menu principale \n"
               )
        
def sintomi():
    answer1 = input("Selezionare il tipo di acqua in base ai sintomi o alle condizioni fisiche: \n"
               "1) Donna incinta \n"
               "2) Ipersecrezione gastrica/ calcoli renali \n"
               "3) Insufficienze digestive/evacuazione intestinale(effetto lassativo) \n"
               "4) Purgative e svolgono un'azione riequilibrante dell'intestino, delle vie biliari e del fegato \n"
               "5) Prevenzione osteoporosi e ipertensione(agiscono su stomaco e fegato) \n"
               "6) Prevenzione arteriosclerosi/favorimento corretto funzionamento del sistema nervoso/alleviazione stress \n"
               "7) Rinforzamento struttura dei denti/prevenzione di carie/ osteoporosi \n"
               "8) Problemi gastrici \n"
               "9) Reintegrazione di perdite di sali durante l'attività sportiva \n"
               "10) Pulizia delle vie urinarie/ipertensione arteriosa \n"
               "X) Torna al menu principale \n"
               )
    while answer1[0] != ("x") and answer1[0] != ("X"):
        if answer1[0] == "1":
            incinta()
        elif answer1[0] == "2":
            bicarbonate()
        elif answer1[0] == "3":
            solfate()
        elif answer1[0] == "4":
            clorurate()
        elif answer1[0] == "5":
            calciche()
        elif answer1[0] == "6":
            magnesiache()
        elif answer1[0] == "7":
            fluorate()
        elif answer1[0] == "8":
            acidule()
        elif answer1[0] == "9":
            sodiche()
        elif answer1[0] == "10":
            iposodiche()
        else:
            print("RISPOSTA ERRATA!")
        answer1 = input("Selezionare il tipo di acqua in base ai sintomi o alle condizioni fisiche: \n"
               "1) Donna incinta \n"
               "2) Ipersecrezione gastrica/ calcoli renali \n"
               "3) Insufficienze digestive/evacuazione intestinale(effetto lassativo) \n"
               "4) Purgative e svolgono un'azione riequilibrante dell'intestino, delle vie biliari e del fegato \n"
               "5) Prevenzione osteoporosi e ipertensione(agiscono su stomaco e fegato) \n"
               "6) Prevenzione arteriosclerosi/favorimento corretto funzionamento del sistema nervoso/alleviazione stress \n"
               "7) Rinforzamento struttura dei denti/prevenzione di carie/ osteoporosi \n"
               "8) Problemi gastrici \n"
               "9) Reintegrazione di perdite di sali durante l'attività sportiva \n"
               "10) Pulizia delle vie urinarie/ipertensione arteriosa \n"
               "X) Torna al menu principale \n"
               )
def menu():
    print("Benvenuto")
    answer = input("Scegliere parametro per la ricerca dell'acqua: \n"
                   "1) Residuo fisso \n"
                   "2) Eta \n"
                   "3) Sintomi/Condizioni fisiche \n"
                   "X) USCITA \n"
                   "")
    while answer[0] != ("x") and answer[0] != ("X"):
        if answer[0] == "1":
            residuo()
        elif answer[0] == "2":
            eta()
        elif answer[0] == "3":
            sintomi()
        else:
            print("RISPOSTA ERRATA!")
        answer = input("Scegliere parametro per la ricerca dell'acqua: \n"
                       "1) Residuo fisso \n"
                       "2) Eta \n"
                       "3) Sintomi/Condizioni fisiche \n"
                       "X) USCITA \n"
                       "")
menu()