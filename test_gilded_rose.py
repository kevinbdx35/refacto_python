# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_aged_brie(self):
        # Création d'un objet "Aged Brie" avec une qualité de 20 et une date de vente de 10 jours
        item = Item("Aged Brie", 10, 20)
        # Création d'une instance de GildedRose avec cet objet
        gilded_rose = GildedRose([item])

        # Vérification de l'état de l'objet avant la mise à jour
        self.assertEqual(item.name, "Aged Brie")
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 20)

        # Mise à jour de l'objet
        gilded_rose.update_quality()

        # Vérification de l'état de l'objet après la mise à jour
        self.assertEqual(item.name, "Aged Brie")
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

    def test_update_quality_backstage_passes(self):
        # Création d'un objet "Backstage passes" avec une qualité de 20 et une date de vente de 15 jours
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        # Création d'une instance de GildedRose avec cet objet
        gilded_rose = GildedRose([item])

        # Vérification de l'état de l'objet avant la mise à jour
        self.assertEqual(item.name, "Backstage passes to a TAFKAL80ETC concert")
        self.assertEqual(item.sell_in, 15)
        self.assertEqual(item.quality, 20)

        # Mise à jour de l'objet
        gilded_rose.update_quality()

        # Vérification de l'état de l'objet après la mise à jour
        self.assertEqual(item.name, "Backstage passes to a TAFKAL80ETC concert")
        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_update_quality_sulfuras(self):
        # Création d'un objet "Sulfuras" avec une qualité de 80 et une date de vente de 0 jours
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        # Création d'une instance de GildedRose avec cet objet
        gilded_rose = GildedRose([item])

        # Vérification de l'état de l'objet avant la mise à jour
        self.assertEqual(item.name, "Sulfuras, Hand of Ragnaros")
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

        # Mise à jour de l'objet
        gilded_rose.update_quality()

        # Vérification de l'état de l'objet après la mise à jour
        self.assertEqual(item.name, "Sulfuras, Hand of Ragnaros")
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

    def test_update_quality_other_items(self):
        # Création d'un objet "Normal Item" avec une qualité de 10 et une date de vente de 5 jours
        item = Item("Normal Item", 5, 10)
        # Création d'une instance de GildedRose avec cet objet
        gilded_rose = GildedRose([item])

        # Vérification de l'état de l'objet avant la mise à jour
        self.assertEqual(item.name, "Normal Item")
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 10)

        # Mise à jour de l'objet
        gilded_rose.update_quality()

        # Vérification de l'état de l'objet après la mise à jour
        self.assertEqual(item.name, "Normal Item")
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_update_quality_conjured_items(self):
        # Création d'un objet "Conjured" avec une qualité de 10 et une date de vente de 5 jours
        item = Item("Conjured", 5, 10)
        # Création d'une instance de GildedRose avec cet objet
        gilded_rose = GildedRose([item])

        # Vérification de l'état de l'objet avant la mise à jour
        self.assertEqual(item.name, "Conjured")
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 10)

        # Mise à jour de l'objet
        gilded_rose.update_quality()

        # Vérification de l'état de l'objet après la mise à jour
        self.assertEqual(item.name, "Conjured")
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 8)

if __name__ == '__main__':
    unittest.main()
