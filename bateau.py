# bateau.py
class Bateau:
    def __init__(self, ligne, colonne, vertical, longueur, marque):
        self.ligne = ligne
        self.colonne = colonne
        self.vertical = vertical
        self.longueur = longueur
        self.marque = marque

    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coule(self, grille):
        """Teste si toutes les cases de ce bateau sont en 💣."""
        for l, c in self.positions:
            if grille._grille[grille.index(l, c)] != '💣':
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=True):
        super().__init__(ligne, colonne, vertical, 4, "🚢")


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=True):
        super().__init__(ligne, colonne, vertical, 3, "⛴")


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=True):
        super().__init__(ligne, colonne, vertical, 2, "🚣")


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=True):
        super().__init__(ligne, colonne, vertical, 2, "🐟")

