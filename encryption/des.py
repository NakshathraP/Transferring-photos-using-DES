from key import keyGenerate
from functionF import xor_binary_strings, functionF

def initial_permutation(plainText):
    IPtable = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
 
    if len(plainText) != 64:
        raise ValueError("Input plaintext must be 64 bits long")
    
    permutedText = [plainText[i-1] for i in IPtable]
    permutedText = "".join(permutedText)

    return permutedText

def des(plainText):
    plainTextPermuted = initial_permutation(plainText)

    lpt = plainTextPermuted[:32]
    rpt = plainTextPermuted[32:]

    for i in range(16):
        temp = rpt
        roundKey = keyGenerate(i)
        rpt = functionF(rpt, roundKey)
        rpt = xor_binary_strings(lpt, rpt)
        lpt = temp

    cipherText = lpt+rpt
    #print(len(cipherText))
    return cipherText
