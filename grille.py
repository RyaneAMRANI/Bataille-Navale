from typing import List, Optional

class Grille:
    def __init__(self, lignes: int, colonnes: int):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = '∿'
        self.touche = 'x'
        self._grille: List[str] = [self.vide] * (lignes * colonnes)

    def index(self, ligne: int, colonne: int) -> int:
        return ligne * self.colonnes + colonne

    def tirer(self, ligne: int, colonne: int, touche: Optional[str] = None) -> None:
        if touche is None:
            touche = self.touche
        self._grille[self.index(ligne, colonne)] = touche

    def __str__(self) -> str:
        result = ''
        for i in range(self.lignes):
            start = i * self.colonnes
            end = start + self.colonnes
            result += ''.join(self._grille[start:end]) + '\n'
        return result
