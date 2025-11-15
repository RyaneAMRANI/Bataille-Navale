from typing import List, Tuple
from grille import Grille

class Bateau:
    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False, marque: str = '⛵'):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque

    @property
    def positions(self) -> List[Tuple[int,int]]:
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille: Grille) -> bool:
        for (l, c) in self.positions:
            if grille._grille[grille.index(l, c)] != grille.touche:
                return False
        return True

# Sous-classes
class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque="🚢")

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque="⛴")

class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🚣")

class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🐟")
