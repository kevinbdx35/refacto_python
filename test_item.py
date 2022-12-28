import unittest

from gilded_rose import Item

class ItemTest(unittest.TestCase):
    def test_init(self):
        # Test de création d'un objet avec des valeurs valides
        item = Item("Aged Brie", 10, 20)
        self.assertEqual(item.name, "Aged Brie")
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 20)

    def test_init_invalid_quality(self):
        # Test de création d'un objet avec une qualité négative
        with self.assertRaises(ValueError):
            item = Item("Aged Brie", 10, -1)

    def test_init_invalid_sell_in(self):
        # Test de création d'un objet avec une date de vente négative
        with self.assertRaises(ValueError):
            item = Item("Aged Brie", -1, 20)

    def test_repr(self):
        # Test de la représentation de l'objet sous forme de chaîne de caractères
        item = Item("Aged Brie", 10, 20)
        self.assertEqual(repr(item), "Aged Brie, 10, 20")

if __name__ == '__main__':
    unittest.main()
