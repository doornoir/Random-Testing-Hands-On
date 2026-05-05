import random
import unittest
from credit_card_validator import credit_card_validator


def make_number(prefix, length):
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(length - len(prefix)))


class TestRandomCreditCards(unittest.TestCase):

    def test_random_valid_prefixes_valid_lengths(self):
        for _ in range(15000):
            choice = random.choice(["visa", "mc_old", "mc_new", "amex"])
            if choice == "visa":
                num = make_number("4", 16)
            elif choice == "mc_old":
                num = make_number(str(random.randint(51, 55)), 16)
            elif choice == "mc_new":
                num = make_number(str(random.randint(2221, 2720)), 16)
            else:
                num = make_number(random.choice(["34", "37"]), 15)
            credit_card_validator(num)

    def test_random_valid_prefixes_all_lengths(self):
        for _ in range(15000):
            prefix = random.choice([
                "4", "34", "37",
                str(random.randint(51, 55)),
                str(random.randint(2221, 2720))
            ])
            length = random.randint(10, 19)
            if len(prefix) <= length:
                credit_card_validator(make_number(prefix, length))

    def test_random_mastercard_boundaries(self):
        for _ in range(15000):
            prefix = str(random.choice([50, 51, 52, 54, 55, 56, 2220, 2221, 2222, 2719, 2720, 2721]))
            length = random.choice([15, 16, 17])
            if len(prefix) <= length:
                credit_card_validator(make_number(prefix, length))

    def test_random_amex_boundaries(self):
        for _ in range(15000):
            prefix = random.choice(["33", "34", "35", "36", "37", "38"])
            length = random.choice([14, 15, 16])
            credit_card_validator(make_number(prefix, length))

    def test_random_repeated_and_patterns(self):
        for _ in range(15000):
            length = random.randint(10, 19)
            pattern = random.choice(["same", "alternating", "zeros"])
            if pattern == "same":
                num = str(random.randint(0, 9)) * length
            elif pattern == "alternating":
                a = str(random.randint(0, 9))
                b = str(random.randint(0, 9))
                num = (a + b) * 10
                num = num[:length]
            else:
                prefix = random.choice(["0", "00", "000", "0000"])
                num = make_number(prefix, length)
            credit_card_validator(num)

    def test_random_everything(self):
        for _ in range(15000):
            length = random.randint(10, 19)
            num = "".join(str(random.randint(0, 9)) for _ in range(length))
            credit_card_validator(num)

    def test_more_bug5(self):
        prefixes = ["37", "26", "25"]
        for _ in range(20000):
            prefix = random.choice(prefixes)
            length = random.choice([15, 16])
            num = make_number(prefix, length)
            credit_card_validator(num)

    def test_more_bug6(self):
        prefixes = ["26", "34", "47"]
        endings = ["258", "1258"]
        for _ in range(20000):
            prefix = random.choice(prefixes)
            ending = random.choice(endings)
            length = random.choice([15, 16])
            middle_len = length - len(prefix) - len(ending)

            if middle_len > 0:
                middle = "".join(str(random.randint(0, 9)) for _ in range(middle_len))
                num = prefix + middle + ending
                credit_card_validator(num)


if __name__ == "__main__":
    unittest.main()
