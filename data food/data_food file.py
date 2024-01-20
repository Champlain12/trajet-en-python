#Importation de la librerie os
from os import *
class FOOD:
    def __init__(self,sexe=None,age=0,date=None,repas=None,heure=None,ustensine=None,lieux=None,nombre=0):
        self.sexe=sexe
        self.age=age
        self.date=date
        self.repas=repas
        self.heure=heure
        self.ustensine=ustensine
        self.lieux=lieux
        self.nombre=nombre
class Noeud:
    def __init__(self,FOOD=None):
        self.info=FOOD
        self.next=None
class File:
    def __init__(self):
        self.tete=None
#ici c'est la fonction qui permet de de save les informations en fin de liste
    def save_fin(self,t):
        new= Noeud(t)
        if self.tete is None:
            self.tete=new
        else:
            tmp=self.tete
            while(tmp.next):
                tmp=tmp.next
            tmp.next=new
#cette fonction affiche les informations qui sont dans la pile
    def afficher(self):
        tmp=self.tete
        while(tmp is not None):
            print(tmp.info.sexe,tmp.info.age,tmp.info.date,tmp.info.repas,tmp.info.heure,tmp.info.ustensine,tmp.info.lieux,tmp.info.nombre)
            print("                                ")
            tmp=tmp.next
#cette fonction fait la recherche d'un repas dans notre liste
    def recherche(self,repas):
        tmp=self.tete
        while((tmp.next)and(tmp.info.repas!=repas)):
            tmp=tmp.next
        if(tmp.info.repas==repas):
            print("le plat existe dans notre liste")
            print("le sexe est:",tmp.info.sexe)
            print("l'age est:",tmp.info.age)
            print("la date du jour est",tmp.info.date)
            print("le repas est:",tmp.info.repas)
            print("l'heure de prise est:",tmp.info.heure)
            print("l'ustensine est:",tmp.info.ustensine)
            print("le lieu de prise est:",tmp.info.lieux)
            print("le nombre de person est:",tmp.info.nombre)
        else:
            print("le plat n'existe pas dans la liste")

# fonction qui retourne la taille de la liste
    def taille(self):
        tmp=self.tete
        n=0
        while(tmp):
            n+=1
            tmp=tmp.next
        return n
#cette fonction fait le trie de la pile en ceservant de la donnée age
    def sort(self):
        new=File()
        n=self.taille()
        while(n>0):
            tmp=self.tete
            mini=tmp.info.age
            while(tmp.next):
                if(mini>tmp.info.age):
                    mini=tmp.info.age
                tmp=tmp.next  
            new.save_fin(mini)
            n-=1
        return new

#c'est le corp du programme
list=File()
T=FOOD("Masculin",16,"18/03/2022","Riz sauce d'arachide","12h-14h","gamelle","Campus",2)
T1=FOOD("Feminin",20,"28/03/2022","Pain avec la noix","16h-18","Sachet","Maison",4)
T2=FOOD("Feminin",18,"28/03/2022","banane malaxe","16h-18","plat","Maison",2)
list.save_fin(T)
list.save_fin(T1)
list.save_fin(T2)
list.afficher()
print("ici la recherche s'effectue")
list.recherche("Riz sauce d'arachide")
print("la taille de la liste est:",list.taille())
list.sort()
print("la liste trie dans l'ordre croissant est:")
list.afficher()  
        
system("pause")
