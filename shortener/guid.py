import time
import random


TIMESTAMP_BIT_LEN = 31
RANDVAL_BIT_LEN = 31

last_timestamp = 0


def generate():
    # generate timestamp
    timestamp = int(time.time())
    # timestamp rand_val를 각 제한 비트 만큼 비트스트링화 한다.
    timestamp_bit_str = construct_element_bit_string(timestamp, TIMESTAMP_BIT_LEN)
    randval_bit_str = "{0:031b}".format(random.getrandbits(RANDVAL_BIT_LEN)) 
    # 모든 요소 문자열을 concatenate하고, int화 하여 guid에 초기화한다.   
    guid_str = timestamp_bit_str + randval_bit_str
    guid = int(guid_str, 2)

    # return guid
    return guid


def construct_element_bit_string(element, element_len):
    # element를 비트로 바꾸고 이를 문자열로 바꾼다.
    element_bit_str = str(bin(element))
    # 비트 문자열의 앞 두문자 '0b'를 제거한다.
    element_bit_str = element_bit_str[2:]
    len_gap = abs(element_len - len(element_bit_str))
    
    if len(element_bit_str) < element_len:
        # 제거한 문자열이 element_len보다 작다면 그 차이만큼 앞에 '0'을 붙여준다.
        element_bit_str = '0'*len_gap + element_bit_str
    else:
        # element_len보다 길이가 길다면 그 차이만큼 앞자리를 자른다.
        element_bit_str = element_bit_str[len_gap:]

    # 정리된 문자열을 리턴한다.
    return element_bit_str

