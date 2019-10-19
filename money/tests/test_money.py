"""
$5 + 10 CHF = $10 (レートが2:1の場合)
[DONE] $5 * 2 = $10
amountをprivateにする
[DONE] Dollarの副作用をどうする？
Moneyの丸め処理どうする？
[DONE] equals()
hashCode()
null との等価性比較
他のオブジェクトとの等価性比較
"""

import unittest
from money import Dollar


class TestMoney(unittest.TestCase):

    def test_maltiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
