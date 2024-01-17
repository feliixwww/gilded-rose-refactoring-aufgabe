import unittest

from gilded_rose_besser import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_vest(self):
        items = [Item("+5 Dexterity Vest", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_elixir(self):
        items = [Item("Elixir of the Mongoose", -2, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

    def test_selfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(42, items[0].quality)

    def test_backstage3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(43, items[0].quality)

    def test_backstage_50max(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_konzert_vorbei(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -2, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_mana_cake(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_mana_cake2(self):
        items = [Item("Conjured Mana Cake", -2, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == '__main__':
    unittest.main()
