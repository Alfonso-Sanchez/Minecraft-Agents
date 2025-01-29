import unittest
from unittest.mock import MagicMock, Mock
from mcpi.minecraft import Minecraft
from mcAgent.InsultBot import InsultBot
from mcAgent.OracleBot import OracleBot
from mcAgent.TntBot import TntBot
from time import sleep
from Main import mainTest as main
import threading

class StaticTest(unittest.TestCase):
    def setUp(self):
        # Creamos un mock de Minecraft que tiene métodos como .create(), .postToChat(), etc.
        self.mock_mc = MagicMock(spec=Minecraft)
        
        # Simulamos que el método `create` devuelve el mismo mock
        self.mock_mc.create.return_value = self.mock_mc
        
        # Configuramos otros métodos que tu código podría necesitar
        self.mock_mc.events = MagicMock()
        self.mock_mc.events.pollChatPosts.return_value = []  # Esto devolverá una lista vacía por defecto
        self.mock_mc.events.pollBlockHits.return_value = []  # Esto devolverá una lista vacía por defecto
        self.mock_mc.player = MagicMock()
        self.mock_mc.player.getPos.return_value = Mock(x=0, y=0, z=0)
        self.mock_mc.getBlock = MagicMock()
        self.mock_mc.getBlock.return_value = 0

    def test_insultbot_static(self):
        insult_bot = InsultBot(mc=self.mock_mc)  # Inyectamos el mock en lugar del objeto real
        
        insult_bot.start()
        self.assertEqual(insult_bot.insultbotON, 1)
        self.assertTrue(insult_bot.insult_thread.is_alive())  # Usamos assertTrue para verificar que es True
        insult_bot.stop()
        self.assertEqual(insult_bot.insultbotON, 0)
        self.assertFalse(insult_bot.insult_thread.is_alive())  # Usamos assertFalse para verificar que es False

    def test_oraclebot_static(self):
        oracle_bot = OracleBot(mc=self.mock_mc)
        
        oracle_bot.start()
        self.assertEqual(oracle_bot.oraclebotON, 1)
        self.assertTrue(oracle_bot.oracle_thread.is_alive())
        oracle_bot.stop()
        self.assertEqual(oracle_bot.oraclebotON, 0)
        self.assertFalse(oracle_bot.oracle_thread.is_alive())

    def test_tntbot_static(self):
        tnt_bot = TntBot(mc=self.mock_mc)
        
        tnt_bot.start()
        self.assertEqual(tnt_bot.tntbotON, 1)
        self.assertTrue(tnt_bot.tnt_thread.is_alive())
        tnt_bot.stop()
        self.assertEqual(tnt_bot.tntbotON, 0)
        self.assertFalse(tnt_bot.tnt_thread.is_alive())

if __name__ == "__main__":
    unittest.main()