alphabet = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encryptChar( char ):

    return keyDictionary(char)


def decryptValue( value ):
    for i in range(0, 60):
        if ((i*500) - 100) < value < ((i*500) + 100):

            return alphabet[i]
    return ' '

def keyDictionary(x):
    return {
        '0': 0,
        '1': 500,
        '2': 1000,
        '3': 1500,
        '4': 2000,
        '5': 2500,
        '6': 3000,
        '7': 3500,
        '8': 4000,
        '9': 4500,
        'a': 5000,
        'b': 5500,
        'c': 6000,
        'd': 6500,
        'e': 7000,
        'f': 7500,
        'g': 8000,
        'h': 8500,
        'i': 9000,
        'j': 9500,
        'k': 10000,
        'l': 10500,
        'm': 11000,
        'n': 11500,
        'o': 12000,
        'p': 12500,
        'q': 13000,
        'r': 13500,
        's': 14000,
        't': 14500,
        'u': 15000,
        'v': 15500,
        'w': 16000,
        'x': 16500,
        'y': 17000,
        'z': 17500,
        ' ': 18000,
    }[x]


def toString(list):
    phrase = ""
    for component in list:
        temp = str(phrase) + str(component)
        phrase = temp
        temp = ""
    return phrase
