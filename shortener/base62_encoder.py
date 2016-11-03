import string


CODES = string.digits + string.ascii_uppercase + string.ascii_lowercase


def encode(id):
    if id <= 0:
        raise ValueError('Negative integer provided.')
    
    hash_digits = []
    dividend = id
    remainder = 0

    while dividend > 0:
        remainder = dividend % 62
        dividend = int(dividend / 62)
        hash_digits.insert(0, remainder)
    
    hash_string = ""

    for digit in hash_digits:
        hash_string += CODES[digit]

    return hash_string


def decode(hash_string):
    decoded = 0

    for idx, char in enumerate(reversed(hash_string)):
        base_num = CODES.index(char)
        pos_sum = base_num * pow(62, idx)
        decoded += pos_sum 

    return decoded
