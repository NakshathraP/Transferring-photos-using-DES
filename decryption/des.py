from functionF import functionF, xor_binary_strings
from key import keyGenerate

def initial_permutation(plainText):
    IP_inverse_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
 
    if len(plainText) != 64:
        raise ValueError("Input plaintext must be 64 bits long")
    
    permutedText = [plainText[i-1] for i in IP_inverse_table]
    permutedText = "".join(permutedText)

    return permutedText

def des_decryption(cipher_text):
    plaintext = ""

    lpt = cipher_text[:32]
    rpt = cipher_text[32:]

    for i in range(16):
        roundKey = keyGenerate(15-i)
        fValue = functionF(lpt, roundKey)
        temp = lpt
        lpt = xor_binary_strings(fValue, rpt)
        rpt = temp

    plaintext = lpt+rpt

    plaintext = initial_permutation(plaintext)

    return plaintext