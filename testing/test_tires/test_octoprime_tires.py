import unittest

from tires.octoprime_tires import OctoprimeTires

class OctoprimeTiresTest(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.9, 0.4, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())