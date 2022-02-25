def encode_better():
    message = str(input("enter a message: "))
    key = str(input("enter a key: "))
    ret = ""
    for i in range(len(message)):
        charval = ord(message[i]) - 65
        keyval = ord(key[i % len(key)]) - 65
        cipherval = ((charval + keyval) % 57) + 64
        ciphertext = chr(cipherval)
        ret += ciphertext
        print(ret)