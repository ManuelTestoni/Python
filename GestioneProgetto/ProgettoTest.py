import unittest
import Progetto

class ProgettoTest(Progetto, unittest.TestCase):

    def __init__(self):
        super.__init__(self)

    def test_progetto(self):
        self.assertEqual(self.getNome(), "ProgettoTest")
        self.assertEqual(self.getIniz(), "2025-10-20")
        self.assertEqual(self.getExp(), "2025-10-21")
