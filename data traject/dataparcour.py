#Importation de la librerie os
from os import *
class Parcour:
    def __init__(self,date=None,sexe=None,age=0,depart=None,arriver=None,cout=0,etatroute=None):
         self.date=date
         self.sexe=sexe
         self.age=age
         self.depart=depart
         self.arriver=arriver
         self.cout=cout
         self.etatroute=etatroute
class Noeud:
    def __init__(self,parcour=None):
        self.info=parcour
        self.next=None
class Pile:
    def __init__(self):
        self.tete=None
        self.next=None
    def savetete(self,t):
        new=Noeud(t)
        new.next=self.tete
        self.tete=new
    def affiche(self):
        tmp=self.tete
        while(tmp is not None):
            print(tmp.info.date,tmp.info.sexe,tmp.info.age,tmp.info.depart,tmp.info.arriver,tmp.info.cout,tmp.info.etatroute)
            print("                                ")
            tmp=tmp.next
#cette fonction fait la recherche d'un trajet en utilisant le depart et l'arriver d'un individu
    def recherche(self,depart,arriver):
        tmp=self.tete
        while((tmp)and(tmp.info.depart!=depart)and(tmp.info.arriver!=arriver)):
            tmp=tmp.next
        if((tmp.info.depart==depart)and(tmp.info.arriver==arriver)):
            print("le trajet a été retrouver")
            print("la date est:",tmp.info.date)
            print("le sexe est :",tmp.info.sexe)
            print("l'age est",tmp.info.age)
            print("le lieu de depart:",tmp.info.depart)
            print("le lieu d'arriver est:",tmp.info.arriver)
            print("le cout est:",tmp.info.cout)
            print("l'etat de la route est:",tmp.info.etatroute)
            print("                                ")
        else:
            print("le trajet n'existe pas dans la liste")
    def taille(self):
        n=0
        tmp=self.tete
        while(tmp):
            n+=1
            tmp=tmp.next
        return n
#fonction de trie des information avec le cout
    def sort(self):
        new=Pile()
        n=self.taille()
        while(n>0):
            tmp=self.tete
            mini=tmp.info.cout
            while(tmp is not None):
                if(mini>tmp.info.cout):
                    mini=tmp.info.cout
                tmp=tmp.next  
            new.savetete(mini)
            n-=1
        return new

#c'est le corp du programme      
list=Pile()
T=Parcour("21/03/2022","masculin",19,"carrefour-meec","polytechnique",150,"bonne")
T1=Parcour("21/03/2022","masculin",18,"beatitude","chateau",400,"mauvais")
T2=Parcour("21/03/2022","feminin",20,"mveng","chateau",300,"assez bien")
T3=Parcour("21/03/2022","feminin",17,"maison rose damasse","cite U",200,"passable")
list.savetete(T)
list.savetete(T1)
list.savetete(T2)
list.savetete(T3)
list.affiche()
list.recherche('carrefour-meec','polytechnique')
print("la taille de la pile est:",list.taille())
list.sort()
list=list.affiche()

system("pause")
