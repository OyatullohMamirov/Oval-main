import unittest
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .btn_texts import accept_send_btns, accept_withdraw_btns, accept_balance_btns, accepted_btns, denied_btns

class TestButtonFunctions(unittest.TestCase):

    def test_accept_send_btns(self):
        lang = 'ru'
        user_id = '123'
        send_id = '456'
        keyboard = accept_send_btns(lang, user_id, send_id)
        self.assertIsInstance(keyboard, InlineKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(len(keyboard.keyboard[0]), 2)
        self.assertEqual(keyboard.keyboard[0][0].callback_data, f"confirm_send_{user_id}_{send_id}")
        self.assertEqual(keyboard.keyboard[0][1].callback_data, f"deny_send_{user_id}_{send_id}")

    def test_accept_withdraw_btns(self):
        lang = 'ru'
        user_id = '123'
        withdraw_id = '456'
        keyboard = accept_withdraw_btns(lang, user_id, withdraw_id)
        self.assertIsInstance(keyboard, InlineKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(len(keyboard.keyboard[0]), 2)
        self.assertEqual(keyboard.keyboard[0][0].callback_data, f"confirm_withdraw_{user_id}_{withdraw_id}")
        self.assertEqual(keyboard.keyboard[0][1].callback_data, f"deny_withdraw_{user_id}_{withdraw_id}")

    def test_accept_balance_btns(self):
        lang = 'ru'
        user_id = '123'
        balance_id = '456'
        keyboard = accept_balance_btns(lang, user_id, balance_id)
        self.assertIsInstance(keyboard, InlineKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(len(keyboard.keyboard[0]), 2)
        self.assertEqual(keyboard.keyboard[0][0].callback_data, f"confirm_balance_{user_id}_{balance_id}")
        self.assertEqual(keyboard.keyboard[0][1].callback_data, f"deny_balance_{user_id}_{balance_id}")

    def test_accepted_btns(self):
        lang = 'ru'
        keyboard = accepted_btns(lang)
        self.assertIsInstance(keyboard, InlineKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(len(keyboard.keyboard[0]), 1)
        self.assertEqual(keyboard.keyboard[0][0].callback_data, "already_accepted")

    def test_denied_btns(self):
        lang = 'ru'
        keyboard = denied_btns(lang)
        self.assertIsInstance(keyboard, InlineKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(len(keyboard.keyboard[0]), 1)
        self.assertEqual(keyboard.keyboard[0][0].callback_data, "already_denied")

if __name__ == '__main__':
    unittest.main()