import unittest
from command import Command


class TestParagraph(unittest.TestCase):
    def setUp(self):
        self.cmd = Command()

    def tearDown(self):
        pass

    def test_process_command(self):
        self.assertEqual(self.cmd.process_command('glob is I'), None)
        self.assertEqual(self.cmd.process_command('prok is V'), None)
        self.assertEqual(self.cmd.process_command('pish is X'), None)
        self.assertEqual(self.cmd.process_command('tegj is L'), None)
        self.assertEqual(
            self.cmd.process_command('glob glob Silver is 34 Credits'), None)
        self.assertEqual(
            self.cmd.process_command('glob prok Gold is 57800 Credits'), None)
        self.assertEqual(
            self.cmd.process_command('pish pish Iron is 3910 Credits'), None)
        self.assertEqual(
            self.cmd.process_command('how much is pish tegj glob glob ?'),
            'pish tegj glob glob is 42')
        self.assertEqual(
            self.cmd.process_command('how many Credits is glob prok Silver ?'),
            'glob prok Silver is 68 Credits')
        self.assertEqual(
            self.cmd.process_command('how many Credits is glob prok Gold ?'),
            'glob prok Gold is 57800 Credits')
        self.assertEqual(
            self.cmd.process_command('how many Credits is glob prok Iron ?'),
            'glob prok Iron is 782 Credits')
        self.assertEqual(
            self.cmd.process_command(
                'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'
            ), 'I have no idea what you are talking about')


if __name__ == "__main__":
    unittest.main()