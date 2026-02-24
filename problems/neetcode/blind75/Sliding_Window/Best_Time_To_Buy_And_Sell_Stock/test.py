import unittest
from solution import Solution

class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_best_time_to_buy_and_sell_stock_example1(self):
        prices = [10,1,5,6,7,1]
        expected_result = 6
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)

    def test_best_time_to_buy_and_sell_stock_example2(self):
        prices = [10,8,7,5,2]
        expected_result = 0
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)
    
    def test_best_time_to_buy_and_sell_stock_zeros(self):
        prices = [0, 0, 0, 0]
        expected_result = 0
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)

    def test_best_time_to_buy_and_sell_stock_increasing(self):
        prices = [1, 2, 3, 4]
        expected_result = 3
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)
    
    def test_best_time_to_buy_and_sell_stock_one(self):
        prices = [100000]
        expected_result = 0
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)
    
    def test_best_time_to_buy_and_sell_stock_big(self):
        prices = [30, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected_result = 9
        result = self.solution.maxProfit(prices)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()