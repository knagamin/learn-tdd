"""
$5 + 10 CHF = $10 (レートが2:1の場合)
[DONE] $5 * 2 = $10
amountをprivateにする
Dollarの副作用をどうする？
Moneyの丸め処理どうする？
"""

import unittest
from money import Dollar


class TestMoney(unittest.TestCase):

    def test_maltiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)
