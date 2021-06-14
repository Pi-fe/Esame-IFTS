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
        print(" MODELLO\nNome: %s \t  Descrizione: %s \n"%(self.nome, self.descrizione))



class Dipartimento():

    def __init__(self, nome):
        self.nome = nome
        self.listaModelli = []


    def inserimento(self, modello):
        self.listaModelli.append(modello)
        print("Il modello è stato inserito con successo!")

    def cancellazione(self, modello):
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





myModello = Modello("Tappo","Tappo di bottiglia in plastica")
myDipartimento = Dipartimento("Dipartimento 1")
myDipartimento.inserimento(myModello)

myDipartimento.stampaModelli()

myModello.modifica()

myModello.stampa()

myDipartimento.cancellazione(myModello)

myDipartimento.stampaModelli()

