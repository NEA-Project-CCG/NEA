import unittest
from Battle_Calculators import Damage_calculator_Unit_Test

class test_Damage_calculator_Unit_Test(unittest.TestCase):
    def test_1(self):
        Test_Data = [500, 100, 0, 100, 150, 100, [], [], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4], Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9], Test_Data[10], Test_Data[11])

        expected = 750
        self.assertEqual(expected, actual)

    def test_2(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [], [], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2250
        self.assertEqual(expected, actual)

    def test_3(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [1], [], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 3375
        self.assertEqual(expected, actual)

    def test_4(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [], [1], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 1500
        self.assertEqual(expected, actual)


    def test_5(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [], [], 100, 0, 500, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 1500
        self.assertEqual(expected, actual)

    def test_6(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [1], [1], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2250
        self.assertEqual(expected, actual)

    def test_7(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [1, 4], [1], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 3375
        self.assertEqual(expected, actual)

    def test_8(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [1, 4], [1, 4], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2250
        self.assertEqual(expected, actual)

    def test_9(self):
        Test_Data = [1500, 100, 500, 100, 150, 100, [], [], 100, 0, 0, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 3375
        self.assertEqual(expected, actual)

    def test_10(self):
        Test_Data = [1500, 100, 500, 100, 150, 100, [], [], 100, 0, 500, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2250
        self.assertEqual(expected, actual)

    def test_11(self):
        Test_Data = [1500, 100, 750, 100, 150, 100, [], [], 100, 0, 500, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2812
        self.assertEqual(expected, actual)

    def test_12(self):
        Test_Data = [1500, 100, 756, 100, 150, 100, [], [], 100, 0, 857, 0]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2044
        self.assertEqual(expected, actual)

    def test_13(self):
        Test_Data = [1500, 100, 0, 100, 150, 100, [], [], 100, 0, 0, 50]

        actual = Damage_calculator_Unit_Test(Test_Data[0], Test_Data[1], Test_Data[2], Test_Data[3], Test_Data[4],
                                   Test_Data[5], Test_Data[6], Test_Data[7], Test_Data[8], Test_Data[9],
                                   Test_Data[10], Test_Data[11])

        expected = 2250
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()