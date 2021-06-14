#CATALOGAZIONE MODELLI STAMPANTE 3D
import pickle

#Creo la classe modello 3d
class Modello():    

    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione


    def modifica(self):
        newnome = str(input("Inserisci il nuovo nome (lascia vuoto se non vuoi modificare): "))
        if newnome != "":
            self.nome = newnome
        newdescrizione = str(input("Inserisci la nuova descrizione (lascia vuoto se non vuoi modificare): "))
        if newdescrizione != "":
            self.descrizione = newdescrizione

    def stampa(self):
        print(" MODELLO\nNome: %s \t  Descrizione: %s \n"%(self.nome, self.descrizione))



class Dipartimento():

    def __init__(self, nome):
        self.nome = nome
        self.listaModelli = []
        self.file = nome+".p"

    def inserimento(self, modello):
        self.listaModelli.append(modello)
        print("Il modello è stato inserito con successo!")

    def cancellazione(self, modello):
        if modello in self.listaModelli:
            self.listaModelli.remove(modello)
            print("Il modello è stato cancellato con successo!")

    def ricerca(self, nome):
        for modello in self.listaModelli:
            if modello.nome == nome:
                print("------Modello trovato------")
                modello.stampa()
                return modello      #questo serve per poter modificare quando si caricano i modelli da file
    
    
    def stampaModelli(self):
        print("----------Lista Completa Modelli----------")
        for modello in self.listaModelli:
            modello.stampa()

    #carico i dati dal file nella lista
    def leggi(self):
        with open(self.file, 'rb') as file:
            self.listaModelli = pickle.load(file)
            print("Caricamento effettuato!")

    #salvo i dati della lista nel file
    def salva(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.listaModelli, file)
            print("Salvataggio effettuato!")



#creazione oggetti e salvataggio file
'''
#Creo due modelli
myModello = Modello("Tappo","Tappo di bottiglia in plastica")
myModello2 = Modello("Quadrato","Un semplice quadrato per qualsiasi uso!")


#Creo un dipartimento
myDipartimento = Dipartimento("Dipartimento 1")
#inserisco i modelli nel dipartimento
myDipartimento.inserimento(myModello)
myDipartimento.inserimento(myModello2)

#stampo tutti i modelli
myDipartimento.stampaModelli()


#modifico il modello myModello
myModello.modifica()
#controllo le modifiche
myModello.stampa()


#cancello il modello dalla lista del dipartimento
myDipartimento.cancellazione(myModello)

#controllo la lista per vedere se ha eliminato il modello
myDipartimento.stampaModelli()

myDipartimento.salva()
'''

#creazione oggetto e caricamento da file

myDipartimento = Dipartimento("Dipartimento 1")
myDipartimento.leggi()

myDipartimento.stampaModelli()

myDipartimento.ricerca("Quadrato").modifica()
myDipartimento.stampaModelli()