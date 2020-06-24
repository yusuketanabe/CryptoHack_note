import Crypto

def from_utf(ascii_list):
    message = []
    for part in ascii_list:
        message.append(part.to_bytes(1, 'big').decode('utf-8'))

    print(''.join(message))