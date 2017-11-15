import unittest


class CustomInt(int):
    def __call__(self, n):
        return CustomInt(self + n)


def add(n):
    return CustomInt(n)


class TestFunc(unittest.TestCase):
    def test_call(self):
        self.assertEqual(add(1), 1)
        self.assertEqual(add(1)(2), 3)
        self.assertEqual(add(1)(2)(5), 8)


if __name__ == '__main__':
    unittest.main()
