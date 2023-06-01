import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2 ))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    """ 
        Note: the assertion here is the same as the assertion in the test above.
        This is because, as the test name indicates, it is the dummy test data that is different.
        The top_bid_price is always higher than the top_ask_price in the quotes dummy dictionary above.
    """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2 ))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatioWhenPriceAIsZero(self):
    mock_price_a = 0
    """ Random price b as it is not relevant to the test case """
    mock_price_b = 300

    self.assertEqual(getRatio(mock_price_a, mock_price_b), 0)

  def test_getRatio_calculateRatioWhenPricePriceBIsZero(self):
    """ Random price a as it is not relevant to the test case """
    mock_price_a = 500
    mock_price_b = 0

    self.assertEqual(getRatio(mock_price_a, mock_price_b), None)


if __name__ == '__main__':
    unittest.main()
