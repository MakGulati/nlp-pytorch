import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
import sys

sys.path.append("../")
from demo import add, multiply_by_10


class TestDemo(unittest.TestCase):
    def test_1_should_equal_1(self):
        self.assertEquals(1, 1)

    def test_add_1_and_1_should_equal_2(self):
        self.assertEquals(2, add(1, 1))

    def test_multiply_10_should_return_dataframe_val_multiplied_by_10(self):

        # arrange
        df = pd.DataFrame({"column1": [1, 2, 3]})

        expected = pd.DataFrame({"column1": [10, 20, 30]})

        # act
        actual = multiply_by_10(df)

        # assert
        assert_frame_equal(expected, actual)
