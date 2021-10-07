import unittest


class HelloWorldTests(unittest.TestCase):
    def test_example(self):
        assert True

    def test_a_dumb_test(self):
        assert False


if __name__ == "__main__":
    unittest.main()
