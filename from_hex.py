import Crypto

def from_hex(hex_string):
    hex_list = []
    n = 0
    while n < len(hex_string):
        hex_list.append(hex_string[n:n+2])
        n += 2
    
    ascii_list = []
    for part in hex_list:
        ascii_list.append(int(part, 16))

    message = []
    for part in ascii_list:
        message.append(part.to_bytes(1, 'big').decode('utf-8'))

    print(''.join(message))
