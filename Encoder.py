##Encoder##
import random, math

alphabet = [['a', 'b', 'c', 'd', 'e', 'f', 'g'],
         ['h', 'i', 'j', 'k', 'l', 'm', 'n'],
         ['o', 'p', 'q', 'r', 's', 't', 'u'],
         ['v', 'w', 'x', 'y', 'z', '1', '2'],
         ['3', '4', '5', '6', '7', '8', '9']]

def int_to_bin_list(num):
    product = num
    result = []
    for i in range(math.floor(math.log(num, 2)), -1, -1):
        if (2 ** i <= product):
            product -= 2 ** i
            result.append(i)
    return result
            
def encode_char(character, index):
    ret = ""
    for num in int_to_bin_list(ord(character)):
        ret += alphabet[index][num]
    return ret

def encode_list(message):
    code = ""
    value = random.randint(0, 4)
    prev_value = value
    for word in message:
        for char in word:
            code += encode_char(char, value)
            while True:
                value = random.randint(0, 4)
                if (value != prev_value):
                    break
            prev_value = value
        code += " "
    return code

def encode(message):
    return encode_list(message.split())

def double_encode(message):
    return encode(encode(message))

def triple_encode(message):
    return encode(encode(encode(message)))


