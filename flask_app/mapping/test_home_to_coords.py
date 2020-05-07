import unittest

from home_to_coords import find_coords
class TestHomeToCoords(unittest.TestCase):

    def test_longitude(self):
        self.assertAlmostEqual(find_coords('Washington, DC')[0], -77.01639, 1)

    def test_latitude(self):
        self.assertAlmostEqual(find_coords('Salt Lake City, UT')[1], 40.749997, 1)

if __name__ == "__main__":
    unittest.main()