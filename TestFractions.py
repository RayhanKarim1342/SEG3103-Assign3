import unittest
import math
from fractions import Fraction

# Our Three Test Functions from Codebase
def multiply_fractions(a, b):
    na, da = a._numerator, a._denominator
    nb, db = b._numerator, b._denominator

    g1 = math.gcd(na, db)     # Branch 1: if g1 > 1
    if g1 > 1:
        na //= g1
        db //= g1

    g2 = math.gcd(nb, da)     # Branch 2: if g2 > 1
    if g2 > 1:
        nb //= g2
        da //= g2

    return Fraction._from_coprime_ints(na * nb, db * da)


def subtract_fractions(a, b):
    na, da = a._numerator, a._denominator
    nb, db = b._numerator, b._denominator
    g = math.gcd(da, db)
    if g == 1:
        return Fraction._from_coprime_ints(na * db - da * nb, da * db)
    s = da // g
    t = na * (db // g) - nb * s
    g2 = math.gcd(t, g)
    if g2 == 1:
        return Fraction._from_coprime_ints(t, s * db)
    return Fraction._from_coprime_ints(t // g2, s * (db // g2))

def add_fractions(f1, f2):
    """a + b"""
    na, da = a._numerator, a._denominator
    nb, db = b._numerator, b._denominator
    g = math.gcd(da, db)
    if g == 1:
        return Fraction._from_coprime_ints(na * db + da * nb, da * db)
    s = da // g
    t = na * (db // g) + nb * s
    g2 = math.gcd(t, g)
    if g2 == 1:
        return Fraction._from_coprime_ints(t, s * db)
    return Fraction._from_coprime_ints(t // g2, s * (db // g2))

# Unit Tests
class TestFractionFunctions(unittest.TestCase):

    def test_multiply_fractions(self):
        self.assertEqual((multiply_fractions(Fraction(3, 11), Fraction(5, 7))), Fraction(15, 77)) #no common factor between them
        self.assertEqual((multiply_fractions(Fraction(6, 5), Fraction(5, 4))), Fraction(3, 2)) #gcd = 1 between first and second fract
        self.assertEqual((multiply_fractions(Fraction(5, 8), Fraction(10, 6))), Fraction(25, 24)) #gcd > 1 between second and first fract
        self.assertEqual((multiply_fractions(Fraction(6, 15), Fraction(10, 9))), Fraction(4, 9)) #gcd between all fractions

    def test_compare_fractions(self):
       self.assertEqual((subtract_fractions(Fraction(3, 11), Fraction(5, 7))), Fraction(15, 77)) #no common factor between them
       self.assertEqual((subtract_fractions(Fraction(6, 5), Fraction(5, 4))), Fraction(3, 2)) #gcd > 1 between first and second fract
       self.assertEqual((multiply_fractions(Fraction(5, 8), Fraction(10, 6))), Fraction(25, 24)) #gcd > 1 between second and first fract
       self.assertEqual((multiply_fractions(Fraction(6, 15), Fraction(10, 9))), Fraction(4, 9)) #gcd between all fractions

    def test_add_positive_fractions(self):
        self.assertEqual(add_fractions(Fraction(1, 2), Fraction(1, 3)), Fraction(5, 6))
        self.assertEqual(add_fractions(Fraction(-1, 2), Fraction(1, 2)), Fraction(0))
        self.assertEqual(add_fractions(Fraction(1, 2), Fraction(0)), Fraction(1,2))

if __name__ == '__main__':
    unittest.main()
