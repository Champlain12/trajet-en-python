#Importation de la librerie os
from os import*
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
class File:
    #ici c'est la fonction qui initialiser la tete de la file a null
    def __init__(self):
        self.tete=None
#ici c'est la fonction qui permet de de save les informations en fin de liste
    def  save_fin(self,t):
        new=Noeud(t)
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
        new=File()
        n=self.taille()
        while(n>0):
            tmp=self.tete
            mini=tmp.info.cout
            while(tmp is not None):
                if(mini>tmp.info.cout):
                    mini=tmp.info.cout
                tmp=tmp.next  
            #self.supprimer(mini)
            new.save_fin(mini)
            n-=1
        return new


#ici ce trouve le programme principale du code ci dessus
list=File()
T=Parcour("21/03/2022","masculin",17,"carrefour-meec","polytechnique",150,"bonne")
T1=Parcour("21/03/2022","masculin",18,"beatitude","chateau",400,"mauvais")
T2=Parcour("21/03/2022","feminin",19,"mveng","chateau",300,"assez bien")
T3=Parcour("21/03/2022","feminin",20,"maison rose damasse","cite U",200,"passable")
print("les elements de la file sont:")
list.save_fin(T)
list.save_fin(T1)
list.save_fin(T2)
list.save_fin(T3)
list.afficher()
print("ici on recherche le trajet dont le depart c'est(maison rose damasse) et l'arriver c'est(cite U)")
list.recherche("maison rose damasse","cite U")
print("la taille de la File est:",list.taille())
list.sort()
print("les element classes dans l'ordre croissant sont:")
list.afficher()


            
        

system("pause")
