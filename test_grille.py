from grille import Grille

def test_init():
    g = Grille(5, 8)
    assert len(g._grille) == 5*8
    assert all(c == g.vide for c in g._grille)

def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 1)
    idx = g.index(1, 1)
    assert g._grille[idx] == g.touche
