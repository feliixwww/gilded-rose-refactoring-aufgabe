import unittest

from gilded_rose_besser import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_vest(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)


    def test_elixir(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)




    def test_ttt(self):
        items = [Item(items[variable_item], 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)




















if __name__ == '__main__':
    unittest.main()
