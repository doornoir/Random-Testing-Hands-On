from credit_card_validator import credit_card_validator
import random


def make_number(prefix, length):
    remaining = length - len(prefix)
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(remaining))


def test_bug1():
    for _ in range(2000):
        num = make_number("4", 16)
        credit_card_validator(num)


def test_bug2():
    for _ in range(2000):
        prefix = str(random.randint(51, 55))
        num = make_number(prefix, 16)
        credit_card_validator(num)


def test_bug3():
    for _ in range(2000):
        prefix = str(random.randint(2221, 2720))
        num = make_number(prefix, 16)
        credit_card_validator(num)


def test_bug4():
    for _ in range(2000):
        num = make_number("34", 15)
        credit_card_validator(num)


def test_bug5():
    for _ in range(2000):
        num = make_number("37", 15)
        credit_card_validator(num)


def test_bug6():
    for _ in range(2000):
        num = "".join(str(random.randint(0, 9)) for _ in range(random.randint(10, 19)))
        credit_card_validator(num)


def test_bug7():
    for _ in range(2000):
        prefix = str(random.randint(10, 99))
        num = make_number(prefix, 16)
        credit_card_validator(num)


def test_bug8():
    for _ in range(2000):
        prefix = random.choice(["4", "34", "37"])
        length = random.choice([14, 15, 16, 17])
        if len(prefix) < length:
            num = make_number(prefix, length)
            credit_card_validator(num)
