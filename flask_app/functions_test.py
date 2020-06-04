import unittest

import numpy.testing as npt

from functions import latlong_finder, EmergencyLookup


class TestLatLongFinder:
    @staticmethod
    def test_redmond_output():
        return npt.assert_almost_equal(latlong_finder('US', 98052), [47.6740, -122.1215], decimal=2)

class TestEmergencyLookup(unittest.TestCase):

    def test_city_instance(self):
        test_instance = EmergencyLookup('San Francisco')
        self.assertEqual(test_instance.city, 'San Francisco', msg='Class Instantiation is Broken!')

    def test_find_site(self):
        test_instance = EmergencyLookup('San Francisco')
        self.assertTrue(('.gov' in test_instance.find_site()) or ('.org' in test_instance.find_site()))

    def test_scrape_site(self):
        test_instance = EmergencyLookup('San Francisco')
        test_instance.find_site()
        self.assertTrue(isinstance(test_instance.scrape_site(), str))

if __name__ == "__main__":
    TestLatLongFinder.test_redmond_output()
    unittest.main()
