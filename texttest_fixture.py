# -*- coding: utf-8 -*-
from __future__ import print_function

from refacto_python.gilded_rose_2 import Item, GildedRose


def main(days):
    # Créez une liste d'objets
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]

    # Mettez à jour la qualité des objets sur plusieurs jours
    for day in range(days):
        print("-------- jour %s --------" % day)
        print("nom, date de vente, qualité")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()


if __name__ == "__main__":
    # Si un argument est fourni, utilisez-le comme nombre de jours à simuler
    # Sinon, simulez seulement 2 jours
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1])
    else:
        days = 2
    main(days)
