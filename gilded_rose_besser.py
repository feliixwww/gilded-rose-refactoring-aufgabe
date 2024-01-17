def standard_abzug(item):
    if item.quality > 0:
        item.quality = item.quality - 1
        if item.sell_in <= 0:
            item.quality = item.quality - 1


def brie_gut_gealtert(item):
    item.quality = item.quality + 1
    if item.sell_in <= 0 and item.quality < 50:
        item.quality = item.quality + 1


def backstage_anforderung(item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if 11 > item.sell_in >= 0:
            if item.quality < 50:
                item.quality = item.quality + 1
        if 6 > item.sell_in >= 0:
            if item.quality < 50:
                item.quality = item.quality + 1
    if item.sell_in <= 0:
        item.quality = item.quality - item.quality


def conjured_cake_gammel(item):
    if item.quality > 0:
        item.quality = item.quality - 2
        if item.sell_in <= 0:
            item.quality = item.quality - 2


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name !=
                    "Conjured Mana Cake" and item.name != "Sulfuras, Hand of Ragnaros"):
                standard_abzug(item)

            if item.name == "Aged Brie" and item.quality < 50:
                brie_gut_gealtert(item)

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_anforderung(item)

            if item.name == "Conjured Mana Cake":
                conjured_cake_gammel(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
