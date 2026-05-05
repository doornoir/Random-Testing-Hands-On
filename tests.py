from credit_card_validator import credit_card_validator
import random


def make_number(prefix, length):
    remaining = length - len(prefix)
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(remaining))


def test_bug1():
    for _ in range(3000):
        # borderline Visa
        num = "4" + "".join(str(random.randint(0, 9)) for _ in range(15))
        credit_card_validator(num)


def test_bug2():
    for _ in range(3000):
        # invalid lengths but valid prefixes
        prefix = random.choice(["4", "34", "37", str(random.randint(51, 55))])
        length = random.choice([10, 11, 12, 13, 14, 17, 18, 19])
        if len(prefix) < length:
            num = prefix + "".join(str(random.randint(0, 9)) for _ in range(length - len(prefix)))
            credit_card_validator(num)


def test_bug3():
    for _ in range(3000):
        prefix = str(random.choice([51, 55, 2221, 2720]))
        num = prefix + "".join(str(random.randint(0, 9)) for _ in range(16 - len(prefix)))
        credit_card_validator(num)


def test_bug4():
    for _ in range(3000):
        # almost valid AmEx (wrong length)
        prefix = random.choice(["34", "37"])
        num = prefix + "".join(str(random.randint(0, 9)) for _ in range(13))  # should be 15, we give 15? NO → break it
        credit_card_validator(num)


def test_bug5():
    for _ in range(3000):
        # completely random
        num = "".join(str(random.randint(0, 9)) for _ in range(random.randint(10, 19)))
        credit_card_validator(num)


def test_bug6():
    for _ in range(3000):
        # repeated digits (can break Luhn)
        digit = str(random.randint(0, 9))
        num = digit * random.choice([15, 16])
        credit_card_validator(num)


def test_bug7():
    for _ in range(3000):
        # leading zeros (common bug)
        num = "0" + "".join(str(random.randint(0, 9)) for _ in range(15))
        credit_card_validator(num)


def test_bug8():
    for _ in range(3000):
        # near-boundary lengths
        prefix = random.choice(["4", "34", "37"])
        length = random.choice([14, 15, 16])
        if len(prefix) < length:
            num = prefix + "".join(str(random.randint(0, 9)) for _ in range(length - len(prefix)))
            credit_card_validator(num)
