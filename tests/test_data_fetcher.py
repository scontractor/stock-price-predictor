import unittest
from src.data_fetcher import fetch_stock_data

class TestDataFetcher(unittest.TestCase):
    def test_fetch_stock_data(self):
        data = fetch_stock_data("AAPL")
        self.assertIn("Time Series (Daily)", data)

if __name__ == "__main__":
    unittest.main()
