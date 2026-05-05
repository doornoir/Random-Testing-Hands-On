import random 
import credit_card_validator
from credit_card_validator

def make_number(prefix, length):
  """Creates a random credit card-like number with a chosen prefix and length.""""
  remaining = length - len(prefix)
  suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining))
  return prefix +suffix

def test_random_visa():
  for _ in range(3000) :
    num = make_number("4", 16)
    credit_card_validator(num)

def test_random_mastercard_old_prefixes():
    for _ in range(3000):
        prefix = str(random.randint(51, 55))
        num = make_number(prefix, 16)
        credit_card_validator(num)

def test_random_mastercard_new_prefixes():
    for _ in range(3000):
        prefix = str(random.randint(2221, 2720))
        num = make_number(prefix, 16)
        credit_card_validator(num)

def test_random_amex_34():
    for _ in range(2000):
        num = make_number("34", 15)
        credit_card_validator(num)

def test_random_amex_37():
    for _ in range(2000):
        num = make_number("37", 15)
        credit_card_validator(num)

def test_random_invalid_lengths():
    for _ in range(3000):
        prefix = random.choice(["4", "34", "37", str(random.randint(51, 55)), str(random.randint(2221, 2720))])
        length = random.choice([10, 11, 12, 13, 14, 17, 18, 19])
        if len(prefix) < length:
            num = make_number(prefix, length)
            credit_card_validator(num)

def test_random_invalid_prefixes():
    for _ in range(3000):
        length = random.choice([15, 16])
        prefix = str(random.randint(10, 99))
        while prefix.startswith("4") or prefix in ["34", "37"] or 51 <= int(prefix) <= 55:
            prefix = str(random.randint(10, 99))
        num = make_number(prefix, length)
        credit_card_validator(num)

def test_random_weird_edge_numbers():
    for _ in range(2000):
        length = random.randint(10, 19)
        num = "".join(str(random.randint(0, 9)) for _ in range(length))
        credit_card_validator(num)
