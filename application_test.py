import unittest
from application import Application

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.something = True

    def test_example(self):
        self.assertTrue(self.something)

    def test_application_constructor(self):
        application = Application()

        self.assertEqual(application.hello, 'Hello')


if __name__ == '__main__':
    unittest.main()