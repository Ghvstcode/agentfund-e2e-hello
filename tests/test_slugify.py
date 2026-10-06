import unittest

from src.textutil import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify("!!!"), "untitled")


if __name__ == "__main__":
    unittest.main()
