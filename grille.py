# grille.py
class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self._grille = ['∿'] * (lignes * colonnes)  # on n'affiche JAMAIS les bateaux ici

    def index(self, ligne, colonne):
        return ligne * self.colonnes + colonne

    def ajoute(self, bateau):
        """Ajoute un bateau SANS l'afficher (invisible tant qu'il n'est pas coulé)."""
        for l, c in bateau.positions:
            if l < 0 or l >= self.lignes or c < 0 or c >= self.colonnes:
                return False
            if self._grille[self.index(l, c)] != '∿':  # case déjà occupée
                return False
        return True  # on ne met rien dans la grille → invisible

    def placer_visuel(self, bateau):
        """Affiche visuellement un bateau coulé."""
        for l, c in bateau.positions:
            self._grille[self.index(l, c)] = bateau.marque

    def __str__(self):
        s = ""
        for i in range(self.lignes):
            s += "".join(self._grille[i * self.colonnes:(i + 1) * self.colonnes]) + "\n"
        return s


