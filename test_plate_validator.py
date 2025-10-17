import unittest
from plate_validator import extract_plate

class TestPlateValidator(unittest.TestCase):

    def test_valid_plates(self):
        plates = ['B 1234 XY', 'D 7890 A']
        expected = ['Even', 'Even']
        self.assertEqual(extract_plate(plates), expected)

    def test_invalid_plates(self):
        plates = ['BHSS 1234 X', 'B 123 XY1', 'd 1234 xy']
        expected = ['Invalid', 'Invalid', 'Invalid']
        self.assertEqual(extract_plate(plates), expected)

    def test_mixed(self):
        plates = ['D 1011 HY', 'BHS 123 S', 'D 423', 'DA 7890 G']
        expected = ['Odd', 'Invalid', 'Invalid', 'Even']
        self.assertEqual(extract_plate(plates), expected)

if __name__ == '__main__':
    unittest.main()
