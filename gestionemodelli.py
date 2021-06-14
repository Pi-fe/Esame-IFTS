#CATALOGAZIONE MODELLI STAMPANTE 3D

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
        print("|- Nome: %s \n|- Descrizione: %s \n"%(self.nome, self.descrizione))


#Creo la classe dipartimento
class Dipartimento():

    def __init__(self, nome):
        self.nome = nome
        self.listaModelli = []


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
    
    
    def stampaModelli(self):
        print("----------Lista Completa Modelli----------")
        for modello in self.listaModelli:
            modello.stampa()




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

