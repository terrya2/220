def encode(message, key):
    word = ""
    for i in message:
        a = (ord(i) + key)
        word += chr(a)
    return word