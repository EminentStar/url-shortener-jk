BASE62_ALPHABET = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z']


def hex_to_int(hexdigest):
    hex_str = '0x' + hexdigest
    return int(hex_str, 16)


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
    
    hash_digits_count = len(hash_digits)
    hash_string = ""
    i = 0

    while hash_digits_count > i:
        hash_string += str(BASE62_ALPHABET[hash_digits[i]])
        i += 1

    return hash_string


def decode(hash_string):
    hash_digits_count = len(hash_string)
    i = hash_digits_count - 1
    multiple_cnt = 0
    decoded = 0    
    
    while i >= 0:
        j = 0
        element = hash_string[i]
        if ord(element) >= ord('0') and ord(element) <= ord('9'):
            idx_num = int(element)
        else:
            idx_num = BASE62_ALPHABET.index(element)

        tmp_sum = idx_num
        
        while j < multiple_cnt:
            tmp_sum *= 62
            j += 1

        decoded +=  tmp_sum

        i -= 1
        multiple_cnt += 1

    return decoded

