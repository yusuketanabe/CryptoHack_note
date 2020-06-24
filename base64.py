def base64(crypto, num):
    '''
    > chmod 755 base.py
    .. from base64 import base64
    .. print(base64('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'))
    -> crypto/Base+64+Encoding+is+Web+Safe/

    A. 入力: "72bca9b68" 16進数に対して
    -> 10進数に変換: 7,2,11,12,10,9,11,6,8
    -> 2進数に変換: 0111, 0010, 1011, 1100, 1010, 1001, 1011, 0110, 1000
    -> 6ビットずつに分割(6ビットに満たない場合0を追加する e. 111 -> 111000): 011100, 101011, 110010, 101001, 101101, 101000
    -> Base64辞書から対応するものを引き出す: c, r, y, p, t, o
    -> 連結する: crypto
    '''

    # Base64の辞書
    conversion_table = {
        '000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E',
        '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I', '001001': 'J',
        '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O',
        '001111': 'P', '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T',
        '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y',
        '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd',
        '011110': 'e', '011111': 'f', '100000': 'g', '100001': 'h', '100010': 'i',
        '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n',
        '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's',
        '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w', '110001': 'x',
        '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2',
        '110111': '3', '111000': '4', '111001': '5', '111010': '6', '111011': '7',
        '111100': '8', '111101': '9', '111110': '+', '111111': '/',
    }

    # 16進数の辞書
    hex_table = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    if num == 16:
        # 2進数として保管するリスト
        binary_list = []

        for s in crypto:
            dec = 0
            if s in hex_table:
                dec = hex_table[s]
                binary_list.append(format(dec, 'b').zfill(4))

        binary_number = ''.join(binary_list)
        n = 0
        six_bit_list = []

        while n < len(binary_number):
            if 6 < len(binary_number) - n:
                six_bit_list.append(binary_number[n:n+6])
            else:
                six_bit_list.append(binary_number[n:] + ('0' * (6 - len(binary_number) + n)))
            n += 6

        convert_text = ''
        convert_list = []
        count = 1
        for part in six_bit_list:
            convert_text += conversion_table[part]
            if count % 6 == 0:
                convert_list.append(convert_text)
                convert_text = ''
            elif count == len(six_bit_list):
                convert_list.append(convert_text + ('=' * (6 - count % 6)))
                convert_text = ''
            count += 1

        return ''.join(convert_list)

    if num == 64:
        six_bit_list = []
        for part in crypto:
            if part == '=':
                break
            for key, value in conversion_table.items():
                if part == value:
                    six_bit_list.append(key)
        
        join_list = ''.join(six_bit_list)
        four_bit_list = []
        n = 0
        while n <= len(join_list) - 4:
            four_bit_list.append(join_list[n:n+4])
            n += 4

        ascii_list = []
        base2 = ''
        count = 0
        for part in four_bit_list:
            count += 1
            base2 += part
            if count == 2:
                ascii_list.append(int(base2, 2))
                count = 0
                base2 = ''
            
        message = []
        for part in ascii_list:
            message.append(part.to_bytes(1, 'big').decode('utf-8'))

        return ''.join(message)