# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        # Créez un objet "foo" et une instance de GildedRose
        item = Item("foo", 0, 0)
        gilded_rose = GildedRose([item])
        
        # Mettez à jour la qualité de l'objet
        gilded_rose.update_quality()
        
        # Vérifiez que le nom de l'objet a été mis à jour correctement
        self.assertEqual(item.name, "foo")

if __name__ == '__main__':
    unittest.main()
