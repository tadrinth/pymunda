from unittest import TestCase

import pymunda

class TestHit(TestCase):
    def test_hit_two_plus(self):
        p = pymunda.hit(2)
        self.assertEqual(5 / 6, p)

    def test_hit_five_plus(self):
        p = pymunda.hit(5)
        self.assertEqual(2 / 6, p)	

    def test_hit_one_plus(self):
        p = pymunda.hit(1)
        self.assertEqual(5 / 6, p)

class TestToxin(TestCase):
    def test_toxin_toughness_four(self):
        p = pymunda.toxin(3)
        self.assertEqual(5/8, p)	

    def test_toxin_toughness_twelve(self):
        p = pymunda.toxin(12)
        self.assertEqual(0, p)	

    def test_toxin_relative(self):
        p1 = pymunda.toxin(3)
        p2 = pymunda.toxin(4)
        p3 = pymunda.toxin(5)
        self.assertTrue(p1 > p2)
        self.assertTrue(p2 > p3)

class TestGas(TestCase):
    def test_gas_toughness_three(self):
        p = pymunda.gas(3)
        self.assertEqual(4 / 6, p)	

    def test_gas_toughness_four(self):
        p = pymunda.gas(4)
        self.assertEqual(3 / 6, p)	

    def test_gas_toughness_six(self):
        p = pymunda.gas(6)
        self.assertEqual(1 / 6, p)

    def test_gas_toughness_seven(self):
        p = pymunda.gas(7)
        self.assertEqual(1 / 6, p)

