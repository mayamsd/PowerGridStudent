
import unittest
import os
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        f = open("terrain_test.txt", "w")
        f.write("~~C\nE X\n")
        f.close()
        t = Terrain()
        t.charger("terrain_test.txt")
        self.assertEqual(t.largeur, 3)
        self.assertEqual(t.hauteur, 2)
        self.assertEqual(t[0][2], Case.CLIENT)
        self.assertEqual(t[1][0], Case.ENTREE)
        self.assertEqual(t[1][1], Case.OBSTACLE)
        os.remove("terrain_test.txt")

    def test_get_entree(self):
        t = Terrain()
        t.cases = [
                [Case.VIDE, Case.VIDE, Case.ENTREE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        entree = t.get_entree()
        self.assertIsNotNone(entree)
        self.assertEqual(entree[0], 0)
        self.assertEqual(entree[1], 2)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

