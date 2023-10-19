def caesar_cipher(message: str, shift: int, mode: str):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    reversealphabet = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
    result = ""
    message = message.lower()
    if mode == "decode":
        shift *= -1
    for c in message:
        if c in alphabet:
            result += alphabet[alphabet.index(c) + shift]
        else:
            result += c
    return result