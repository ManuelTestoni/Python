import ClasseCane

import unittest

class AnimaleTest(unittest.TestCase):
    def test_faiVerso(self):
        GoldenRetriever = ClasseCane.Cane("GoldenRetriever", False, True, 'Canis', 'Panna', 4, True, 10, 'M', "tundra")
        self.assertEqual(GoldenRetriever.faiVerso(), 0)

    def test_due(self):
        GoldenRetriever = ClasseCane.Cane("GoldenRetriever", False, True, 'Canis', 'Panna', 4, True, 10, 'M', "tundra")
        GoldenRetriever.cammina()

if __name__ == "__main__":
    unittest.main()
