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

def add_fractions(a, b):
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

    # def test_subtract_fractions(self):
       # self.assertEqual((subtract_fractions(Fraction(3, 11), Fraction(5, 7))), Fraction(15, 77)) #no common factor between them
       # self.assertEqual((subtract_fractions(Fraction(6, 5), Fraction(5, 4))), Fraction(3, 2)) #gcd > 1 between first and second fract
       # self.assertEqual((multiply_fractions(Fraction(5, 8), Fraction(10, 6))), Fraction(25, 24)) #gcd > 1 between second and first fract
       # self.assertEqual((multiply_fractions(Fraction(6, 15), Fraction(10, 9))), Fraction(4, 9)) #gcd between all fractions
       #

    def test_add_positive_fractions(self):
        # g == 1
        a = Fraction(1, 2)
        b = Fraction(1, 3)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(1, 6))

        # g == 3, g2 == 1
        a = Fraction(1, 6)
        b = Fraction(1, 9)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(1, 18))

        # g = 4, g2 = 2
        a = Fraction(3, 8)
        b = Fraction(1, 4)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(1, 8))

        # a = 0
        a = Fraction(0, 4)
        b = Fraction(1, 8)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(-1, 8))

        # no common factors
        a = Fraction(3, 11)
        b = Fraction(5, 7)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(-8, 77))

        # result < -1
        a = Fraction(3, 11)
        b = Fraction(9, 7)
        result = subtract_fractions(a, b)
        self.assertEqual(result, Fraction(-90, 77))

        with self.assertRaises(ZeroDivisionError):
            a = Fraction(1, 0)
            b = Fraction(1, 2)
            subtract_fractions(a,b)

        with self.assertRaises(ZeroDivisionError):
            a = Fraction(1, 6)
            b = Fraction(1, 0)
            subtract_fractions(a, b)


    def test_add_positive_fractions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 3)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(5, 6)) # g == 1

        a = Fraction(1, 6)
        b = Fraction(1, 9)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(5, 18)) # g==3, g2 ==1

        a = Fraction(1, 4)
        b = Fraction(1, 8)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(3, 8))         # g = 4, g2 = 2

        a = Fraction(0, 4)
        b = Fraction(1, 8)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(1, 8))  # 0 value for a


        a = Fraction(3, 11)
        b = Fraction(5, 7)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(15, 77))  # no factor


        a = Fraction(3, 11)
        b = Fraction(9, 7)
        result = add_fractions(a, b)
        self.assertEqual(result, Fraction(120, 77))  #final val > 1


        with self.assertRaises(ZeroDivisionError):
            a = Fraction(1, 0)
            b = Fraction(1, 2)
            add_fractions(a,b)




if __name__ == '__main__':
    unittest.main()
