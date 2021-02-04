# Jeu du petit bac

from random import *
from tkinter import *
import tkinter as tk

##############
## FONCTION ##
##############

def jouerUnePartie():
    '''
        function: Début de partie soit écran d'accueil qui retourne un bool en fonction de l'input.
        entrée: none
        sortie : bool
    '''
    quitterOuJouer = "."
    while quitterOuJouer != "":
        quitterOuJouer = input("Souhaitez-vous Jouer (écrivez 'jouer') ou Quitter (écrivez 'quitter') ? ").lower()
        if quitterOuJouer == "jouer":
            entrerDansLeJeuBool = 1
            return True
        elif quitterOuJouer == "quitter":
            return False

def generationLettre():
    '''
        function: On choisi une lettre au hasard dans la liste.
        entrée: none
        sortie : string
    '''
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    listAlphabet = alphabet.split(" ")
    lettreAleatoire = choice(listAlphabet)
    return lettreAleatoire


def generationOrdreDuJeu():
    '''
        function: On mélange au hasard une liste.
        entrée: none
        sortie : liste
    '''
    listDesFichierMelange = ["animaux.txt", "pays.txt","prenomm.txt","prenomf.txt"]
    shuffle(listDesFichierMelange)
    return listDesFichierMelange


def generationCategorie(melange, categorie):
    '''
        function: On mélange au hasard une liste.
        entrée: liste, int
        sortie : fichier texte
    '''
    fichiercategorie = open(melange[categorie], "r")
    return fichiercategorie


def verifivationPremiereLettre(lettreArgument):
    '''
        function: On vérifie la syntaxe.
        entrée: string
        sortie : string
    '''
    global entrezUneValeur
    premiereLettre = lettreArgument

    while True:
        entrezUneValeur = input().upper()
        if not entrezUneValeur.upper().startswith(premiereLettre, 0, 1):
            print("Entrez la bonne première lettre")
        elif len(entrezUneValeur) <= 2:
            print("Veuillez saisir plus de deux lettre lettre.")
        else:
            return entrezUneValeur


def siInputEstDansText(fichierCategorie):
    '''
        function: On vérifie si l'input est dans le texte
        entrée: fichier texte
        sortie : bool
    '''
    listeDeLongueur = []
    for ligne in fichierCategorie:
        if entrezUneValeur in ligne:
            listeDeLongueur.append(ligne)

    for i in range(len(listeDeLongueur)):
        if len(listeDeLongueur[i]) - 1 == len(entrezUneValeur):
            return True

def generationOrdreDuJeuSansTXT(liste): #Antoine m'a demandé de faire cette fonction pour l'aider sur tkinter.
    '''
        function: On crée une liste de l'ordre du jeu sans l'extension .txt
        entrée: liste
        sortie : list
    '''
    categories = liste
    categoriesSansTXT = []
    for i in range(4):
        if categories[i] == "animaux.txt":
            categoriesSansTXT.append("Animaux")
        elif categories[i] == "pays.txt":
            categoriesSansTXT.append("Pays")
        elif categories[i] == "prenomm.txt":
            categoriesSansTXT.append("Prenom Masculin")
        elif categories[i] == "animaux.txt":
            categoriesSansTXT.append("animaux")
        elif categories[i] == "prenomf.txt":
            categoriesSansTXT.append("Prenom Feminin")
    return categoriesSansTXT


#########################
## INTERFACE GRAPHIQUE ##
#########################

# En attente du programme tkinter

########################
# PROGRAMME PRINCIPALE #
########################

def programmePrincipale():
    while jouerUnePartie():
        lettreAleatoire = generationLettre()
        ordreDuJeu = generationOrdreDuJeu()
        compteurDeFaute = 0
        print("La première lettre du jeu est : ", lettreAleatoire)
        for i in range(len(ordreDuJeu)):
            fichier = generationCategorie(ordreDuJeu, i)
            fichierSansTXT = generationOrdreDuJeuSansTXT(ordreDuJeu)
            print("La catégorie est : ", fichierSansTXT[i])
            if verifivationPremiereLettre(lettreAleatoire):
                print("La première lettre est juste !")
                if siInputEstDansText(fichier):
                    print("Et la réponse est correcte")
                else:
                    print("Oh non ! La réponse est incorrect...")
                    compteurDeFaute = compteurDeFaute + 1
                    print("Tu as ", compteurDeFaute," faute(s).")

            if compteurDeFaute == 2:
                break
        if compteurDeFaute == 0:
            print("Vous avez fait un sans faute INCROYABLE !")
            continue
        else:
            print("vous avez fait ", compteurDeFaute, " faute(s) bien joué !")

if __name__ == "__main__":
    programmePrincipale()
