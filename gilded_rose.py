# -*- coding: utf-8 -*-

class GildedRose:
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
            elif item.name == "Conjured":
                self._update_conjured_items(item)
            else:
                self._update_other_items(item)
    
    def _update_conjured_items(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Conjured".
        """
        # La qualité de l'objet diminue avec le temps
        if item.quality > 0:
            item.quality -= 2
        # Si l'objet a expiré, sa qualité continue de diminuer
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        # La qualité de l'objet ne doit pas être négative
        if item.quality < 0:
            item.quality = 0
        # Mettre à jour la date de vente de l'objet
        item.sell_in -= 1


    def _update_aged_brie(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Aged Brie".
        """
        self._increase_quality(item, 1)
        self._update_sell_in(item, -1)

    def _update_backstage_passes(self, item):
        """
        Met à jour la qualité et l'état d'un objet "Backstage passes".
        """
        if item.sell_in > 10:
            self._increase_quality(item, 1)
        elif item.sell_in > 5:
            self._increase_quality(item, 2)
        elif item.sell_in > 0:
            self._increase_quality(item, 3)
        else:
            # Si l'objet a expiré, sa qualité passe à 0
            item.quality = 0
        self._update_sell_in(item, -1)

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
        self._decrease_quality(item, 1)
        self._update_sell_in(item, -1)
        if item.sell_in < 0:
            self._decrease_quality(item, 1)

    def _increase_quality(self, item, amount):
        """
        Augmente la qualité de l'objet d'une certaine quantité, en s'assurant de ne pas dépasser la limite de 50.
        """
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount):
        """
        Diminue la qualité de l'objet d'une certaine quantité, en s'assurant de ne pas descendre en dessous de 0.
        """
        item.quality = max(0, item.quality - amount)

    def _update_sell_in(self, item, amount):
        """
        Met à jour la date de vente de l'objet d'une certaine quantité.
        """
        item.sell_in += amount

class Item:
    def __init__(self, name, sell_in, quality):
        """
        Initialise un objet avec un nom, une date de vente et une qualité.
        """
        if quality < 0:
            raise ValueError("La qualité ne peut pas être négative.")
        if sell_in < 0:
            raise ValueError("La date de vente ne peut pas être négative.")
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        """
        Retourne une représentation de l'objet sous forme de chaîne de caractères.
        """
        return f"{self.name}, {self.sell_in}, {self.quality}"


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