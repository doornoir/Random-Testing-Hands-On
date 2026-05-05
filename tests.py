import random
import unittest
from credit_card_validator import credit_card_validator


def make_number(prefix, length):
    remaining = length - len(prefix)
    suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining))
    return prefix + suffix


class TestRandomCreditCards(unittest.TestCase):

    def test_bug1(self):
        for _ in range(5000):
            num = make_number("4", 16)
            credit_card_validator(num)

    def test_bug2(self):
        for _ in range(5000):
            prefix = random.choice(["4", "34", "37", str(random.randint(51, 55))])
            length = random.choice([10, 11, 12, 13, 14, 17, 18, 19])
            if len(prefix) < length:
                num = make_number(prefix, length)
                credit_card_validator(num)

    def test_bug3(self):
        for _ in range(5000):
            prefix = str(random.choice([51, 55, 2221, 2720]))
            num = make_number(prefix, 16)
            credit_card_validator(num)

    def test_bug4(self):
        for _ in range(5000):
            prefix = random.choice(["34", "37"])
            num = make_number(prefix, 15)
            credit_card_validator(num)

    def test_bug5(self):
        for _ in range(5000):
            length = random.randint(10, 19)
            num = "".join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(num)

    def test_bug6(self):
        for _ in range(5000):
            digit = str(random.randint(0, 9))
            num = digit * random.choice([15, 16])
            credit_card_validator(num)

    def test_bug7(self):
        for _ in range(5000):
            num = make_number("0", 16)
            credit_card_validator(num)

    def test_bug8(self):
        for _ in range(5000):
            prefix = random.choice(["4", "34", "37", "51", "55", "2221", "2720"])
            length = random.choice([14, 15, 16, 17])
            if len(prefix) < length:
                num = make_number(prefix, length)
                credit_card_validator(num)


if __name__ == "__main__":
    unittest.main()
