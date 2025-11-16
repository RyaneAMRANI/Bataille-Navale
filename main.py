# main.py
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
import random

def placer_bateaux_aleatoires(grille):
    bateaux = [
        PorteAvion(0,0),
        Croiseur(0,0),
        Torpilleur(0,0),
        SousMarin(0,0)
    ]
    
    for bateau in bateaux:
        placed = False
        while not placed:
            ligne = random.randint(0, grille.lignes - 1)
            colonne = random.randint(0, grille.colonnes - 1)
            vertical = random.choice([True, False])
            bateau.ligne = ligne
            bateau.colonne = colonne
            bateau.vertical = vertical
            if grille.ajoute(bateau):
                placed = True
    return bateaux

def jeu():
    g = Grille(8, 10)
    bateaux = placer_bateaux_aleatoires(g)
    
    coups = 0
    while True:
        print(g)

        s = input("Entrez ligne,colonne à tirer (ex: 2,3) ou q pour quitter : ")
        if s.lower() == 'q':
            print("Vous avez quitté le jeu.")
            break

        try:
            ligne, colonne = map(int, s.split(','))
        except:
            print("Format incorrect, recommencez.")
            continue

        coups += 1
        touche = False

        for bateau in bateaux:
            if (ligne, colonne) in bateau.positions:
                g._grille[g.index(ligne, colonne)] = '💣'
                touche = True

                if bateau.coule(g):
                    print(f"Bateau coulé ! {bateau.marque}")
                    g.placer_visuel(bateau)

                break

        if not touche:
            g._grille[g.index(ligne, colonne)] = 'x'

        if all(b.coule(g) for b in bateaux):
            print(g)
            print(f"Bravo ! Vous avez coulé tous les bateaux en {coups} coups.")
            break


if __name__ == "__main__":
    jeu()



