import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, foods, handle_help


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 499159397
        start(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 499159397
        handle_help(message)

    def test_foods(self):
        message = MagicMock()
        message.chat.id = 499159397
        foods(message)


if __name__ == '__main__':
    unittest.main()
