def caesarCipher(string, key):
    charArray = []
    asciiConstant = 97 
    for char in string:
        asciiCode = ord(char)
        caesarCode = asciiCode - asciiConstant
        shiftedCode = (caesarCode + key) % 26 
        newAsciiCode = shiftedCode + asciiConstant
        shiftedInteger = chr(newAsciiCode)
        charArray.append(shiftedInteger)
    return ''.join(charArray)


if __name__ == '__main__':
    print(caesarCipher('xyz', 2))