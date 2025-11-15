from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

def test_positions():
    b1 = Bateau(2, 3, longueur=3)
    assert b1.positions == [(2,3),(2,4),(2,5)]
    b2 = Bateau(2, 3, longueur=3, vertical=True)
    assert b2.positions == [(2,3),(3,3),(4,3)]

def test_coule():
    g = Grille(5,5)
    b = Bateau(1,1, longueur=2)
    # avant tir
    assert not b.coule(g)
    # tirer sur toutes les positions
    for (l,c) in b.positions:
        g.tirer(l,c)
    assert b.coule(g)

def test_sous_classes():
    pa = PorteAvion(0,0)
    assert pa.longueur == 4 and pa.marque == "🚢"
    c = Croiseur(0,0)
    assert c.longueur == 3 and c.marque == "⛴"
    t = Torpilleur(0,0)
    assert t.longueur == 2 and t.marque == "🚣"
    s = SousMarin(0,0)
    assert s.longueur == 2 and s.marque == "🐟"
