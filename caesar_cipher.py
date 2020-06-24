def caesar(text, num, vec):
    """
    |A|B|C|D|E| Cipher
     | |_____
     |_____  |
           | |
    |A|B|C|D|E| Plain
    
    > from caesar_cipher import caesar
    > print(caesar('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD', 3))
    THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

    組み込み関数もあるよ
    import codecs
    codecs.decode('TEXT', 'rot13')
    """
    list = text.lower().split()
    convert = []
    if vec == 'right':
        for part in list:
            word = ''
            for w in part:
                if ord(w) + num > ord('z'):
                    word += chr((ord('a') - 1) + (num - (ord('z') - ord(w))))
                else:
                    word += chr(ord(w) + num)
            convert.append(word.upper())

    elif vec == 'left':
        for part in list:
            word = ''
            for w in part:
                if ord(w) - num < ord('a'):
                    word += chr((ord('z') + 1) - (num - (ord(w) - ord('a'))))
                else:
                    word += chr(ord(w) - num)
            convert.append(word.upper())

    return ' '.join(convert)
