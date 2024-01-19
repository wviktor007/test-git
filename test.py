import unittest

def calculate_sum(a, *args):
    sum = a
    for i in args:
        sum += i
    return sum


print(calculate_sum(2, 3, 4, 5))




class UnitTest(unittest.TestCase):
    def test_two_value(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(2, 3, 4, 5, 6)
        true_result = 20
        self.assertEquals(result, true_result)

    def test_two_value2(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(4, 5, 7, 8)
        true_result = 24
        self.assertEquals(result, true_result)

    def test_two_value3(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(10, 10, 20, 30)
        true_result = 70
        self.assertEquals(result, true_result)

    def test_two_value4(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(45, 45, 90)
        self.assertNotEquals(result, 200)

    def test_two_value5(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(10, 10, 20, 30)
        true_result = 70
        self.assertIsInstance(result, int)

    def test_two_value6(self):
        '''
        Проверяем два значения в функции calculate_sum из модуля test
        '''
        result = calculate_sum(10, 10, 20, 30)
        true_result = 70
        self.assertEquals(result, true_result)

    # def test_two_value7(self):
    #     '''
    #     Проверяем два значения в функции calculate_sum из модуля test
    #     '''
    #     with self.assertRaises(ValueError):
    #         calculate_sum([], [1])


if __name__ == '__main__':
    unittest.main()
