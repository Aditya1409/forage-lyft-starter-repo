import unittest

from engine.capulet_engine import CapuletEngine

class CapuletEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 15000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())