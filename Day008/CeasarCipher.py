alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
reversealphabet = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
def encode(message: str, shift: int):
    encodedmessage = ""
    message = message.lower()
    for c in message :
        if c in alphabet : 
            encodedmessage += alphabet[alphabet.index(c) + shift]
        else:
            encodedmessage += c
    return encodedmessage

def decode(message: str, shift: int) :
    decodedmessage = ""
    message = message.lower()
    for c in message :
        if c in reversealphabet :
            decodedmessage += reversealphabet[reversealphabet.index(c) + shift]
        else:
            decodedmessage += c
    return decodedmessage