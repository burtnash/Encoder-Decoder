##Decoder##

alphabet = [['a', 'b', 'c', 'd', 'e', 'f', 'g'],
         ['h', 'i', 'j', 'k', 'l', 'm', 'n'],
         ['o', 'p', 'q', 'r', 's', 't', 'u'],
         ['v', 'w', 'x', 'y', 'z', '1', '2'],
         ['3', '4', '5', '6', '7', '8', '9']]

def category(character):
    for i in range(len(alphabet)):
        if character in alphabet[i]:
            return i

def place(character, index):
    return alphabet[index].index(character)

def decode_list(code):
    message = ""
    for word in code:
        current_category = category(word[0])
        nums = []
        for i in range(len(word)):
            if category(word[i]) != current_category:
                message += str(chr(sum(nums)))
                current_category = category(word[i])
                nums = []
            nums.append(2 ** place(word[i], category(word[i])))
            if i == len(word) - 1:
                message += str(chr(sum(nums)))
        message += " "
    return message

def decode(code):
    return decode_list(code.split())

def double_decode(code):
    return decode(decode(code))

def triple_decode(code):
    return decode(decode(decode(code)))
    
