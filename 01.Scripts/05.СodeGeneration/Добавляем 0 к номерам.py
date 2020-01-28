def past(num, den):
    sch = min(*map(abs, (num, den)))
    while sch != 0:
        if num % sch == 0 and den % sch == 0:
            num /= sch
            den /= sch
        sch -= 1
    if str(int(num)) != str(int(den)):
        return str(int(num)) + '/' + str(int(den))
    else:
        return str(int(num))


class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        self.numerator *= other.denominator
        other.numerator *= self.denominator
        common_numerator = self.numerator + other.numerator
        return past(common_numerator, common_denominator)

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        self.numerator *= other.denominator
        other.numerator *= self.denominator
        common_numerator = self.numerator - other.numerator
        return past(common_numerator, common_denominator)

    def __mul__(self, other):
        common_denominator = self.denominator * other.denominator
        common_numerator = self.numerator * other.numerator
        return past(common_numerator, common_denominator)

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator


class OperationsOnFraction(Fraction):
    def getint(self):
        return self.__int__()

    def getfloat(self):
        return self.__float__()


lol1 = Fraction(6, 3)
lol2 = Fraction(3, 4)
lol3 = OperationsOnFraction(5, 4)
print(lol3.getint())
print(lol3.getfloat())
print(lol1 + lol2)
