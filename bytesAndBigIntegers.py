import Crypto

def to_message(base10):
    to_binary = format(base10, 'b')
    binary_list = []
    inversion_binary = ''.join([_ for _ in to_binary[::-1]])
    n = 0
    while n < len(inversion_binary):
        if 4 < len(inversion_binary) - n:
            binary_list.append(inversion_binary[n:n+4])
        else:
            binary_list.append(inversion_binary[n:] + ('0' * (4 - len(inversion_binary) + n)))
        n += 4

    binary_list = [''.join([_ for _ in _[::-1]]) for _ in binary_list[::-1]]

    # binary_list = ['0110', '0011', '0111', '0010', '0111', '1001', '0111', '0000', '0111', '0100', '0110',
    #           '1111', '0111', '1011', '0011', '0011', '0110', '1110', '0110', '0011', '0011', '0000',
    #           '0110', '0100', '0011', '0001', '0110', '1110', '0011', '0110', '0101', '1111', '0011',
    #           '0100', '0110', '1100', '0110', '1100', '0101', '1111', '0011', '0111', '0110', '1000',
    #           '0011', '0011', '0101', '1111', '0111', '0111', '0011', '0100', '0111', '1001', '0101',
    #           '1111', '0110', '0100', '0011', '0000', '0111', '0111', '0110', '1110', '0111', '1101'] 

    #hex_list = []
    #hex_bytes = ''
    #count = 0
    #for part in binary_list:
    #    count += 1
    #    # int('1111', 2) -> 15(base10) -> str(hex(15)) -> '0xf'(base16 sring) -> replace('0x', '') -> 'f'
    #    hex_bytes += str(hex(int(part, 2))). replace('0x', '')
    #    if count == 2:
    #        hex_list.append(hex_bytes)
    #        count = 0
    #        hex_bytes = ''
    #
    # hex_list = ['63', '72', '79', '70', '74', '6f', '7b', '33', '6e', '63', '30', '64', '31', '6e',
    #             '36', '5f', '34', '6c', '6c', '5f', '37', '68', '33', '5f', '77', '34', '79', '5f',
    #             '64', '30', '77', '6e', '7d']

    ascii_list = []
    base2 = ''
    count = 0
    for part in binary_list:
        count += 1
        base2 += part
        if count == 2:
            ascii_list.append(int(base2, 2))
            count = 0
            base2 = ''

    # ascii_list = [99, 114, 121, 112, 116, 111, 123, 51, 110, 99, 48, 100, 49, 110, 54, 95, 52, 108,
    #               108, 95, 55, 104, 51, 95, 119, 52, 121, 95, 100, 48, 119, 110, 125]

    message = []
    for part in ascii_list:
        # Crypto.Util.number.long_to_bytes part(99).to_bytes(1, 'big') -> bytes(b'c')
        # bytes(b'c') -> bytes.decode('utf-8') -> str('c')
        message.append(part.to_bytes(1, 'big').decode('utf-8'))

    return ''.join(message)
    # >> from bytesAndBigIntegers import to_message
    # >> to_message(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
    # .. 'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'