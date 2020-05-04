import numpy.testing as npt
from functions import latlong_finder


class TestLatLongFinder:
    @staticmethod
    def test_redmond_output():
        return npt.assert_almost_equal(latlong_finder('US', 98052), [47.6740, -122.1215], decimal=2)


if __name__ == "__main__":
    TestLatLongFinder.test_redmond_output()
