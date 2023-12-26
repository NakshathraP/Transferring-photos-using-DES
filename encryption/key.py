import secrets

def keyGenerate(roundNum):
    compressionTable = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
    ]

    shiftTable = [
        1, 1, 2, 2,
        2, 2, 2, 2,
        1, 2, 2, 2,
        2, 2, 2, 1
    ]

    #fullKey = secrets.randbits(64)
    #fullKey = format(fullKey, '064b')
    fullKey = "0111010011011000011010011001111101000111111000110111111100001110"
    #print(len(fullKey))
    randomKey = ""
    for i,char in enumerate(fullKey):
        if (i+1)%8 != 0 :
            randomKey += char
    #print(len(randomKey))
    leftKeyHalf = randomKey[:28]
    rightKeyHalf = randomKey[28:]

    roundKey = []

    for r, shiftNum in enumerate(shiftTable):
        subkey = ""

        leftKeyHalf = leftKeyHalf[shiftNum:] + leftKeyHalf[:shiftNum]
        rightKeyHalf = rightKeyHalf[shiftNum:] + rightKeyHalf[:shiftNum]

        subkey = leftKeyHalf + rightKeyHalf
        compressedKey = [subkey[i-1] for i in compressionTable]
        compressedKey = "".join(compressedKey)
        roundKey.append(compressedKey)
    
    return roundKey[roundNum] 

print(keyGenerate(0))