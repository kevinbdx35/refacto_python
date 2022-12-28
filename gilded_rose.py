# -*- coding: utf-8 -*-

class GildedRose(object):
    """
    Classe principale qui gère l'état et la qualité des objets.
    """

    def __init__(self, items):
        """
        Initialise la classe avec une liste d'objets.
        """
        self.items = items

    def update_quality(self):
        """
        Met à jour la qualité et l'état de chaque objet dans la liste.
        """
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self._update_sulfuras(item)
            else:
                self._update_other_items(item)

    def _update_aged_brie(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Aged Brie".
        """
        # La qualité de l'objet augmente avec le temps
        if item.quality < 50:
            item.quality += 1
        # Si l'objet a expiré, sa qualité continue d'augmenter
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def _update_backstage_passes(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Backstage passes".
        """
        # La qualité de l'objet augmente avec le temps
        if item.quality < 50:
            item.quality += 1
            # La qualité augmente plus rapidement à mesure que la date de vente approche
            if item.sell_in < 11:
                item.quality += 1
            if item.sell_in < 6:
                item.quality += 1
        # Si l'objet a expiré, sa qualité passe à zéro
        if item.sell_in < 0:
            item.quality = 0

    def _update_sulfuras(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Sulfuras".
        """
        # L'objet "Sulfuras" ne change pas avec le temps
        pass

    def _update_other_items(self, item):
        """
        Met à jour la qualité et l'état d'un objet qui n'est ni "Aged Brie", ni "Backstage passes", ni "Sulfuras".
        """
        # La qualité de l'objet diminue avec le temps
        if item.quality > 0:
            item.quality -= 1
        # Si l'objet a expiré, sa qualité continue de diminuer
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        """
        Initialise un objet avec un nom, une date de vente et une qualité.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """
        Retourne une représentation de l'objet sous forme de chaîne de caractères.
        """
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == '__main__':

    # Créez une instance de GildedRose et ajoutez-y des objets
    gilded_rose = GildedRose([Item("Aged Brie", 10, 20), Item("Backstage passes", 15, 20), Item("Sulfuras", 0, 80), Item("Normal Item", 5, 10)])

    # Affichez les objets avant la mise à jour
    print("Avant la mise à jour :")
    for item in gilded_rose.items:
        print(item)

    # Mettez à jour les objets
    gilded_rose.update_quality()

    # Affichez les objets après la mise à jour
    print("\nAprès la mise à jour :")
    for item in gilded_rose.items:
        print(item)


