import unittest
from command import Command


class TestParagraph(unittest.TestCase):
    def setUp(self):
        self.cmd = Command()

    def tearDown(self):
        pass

    def test_process_command(self):
        pass


if __name__ == "__main__":
    unittest.main()