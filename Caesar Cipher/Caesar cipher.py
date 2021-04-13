ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def caesar(word):
    encoded = ""
    for character in word:
        if character in ALPHABET:
            index = ALPHABET.find(character)
            # we modulo 26 and wrap around if we pass "z".
            # to decode the message, minus the integer instead.
            nextIndex = (index + 3) % 26
            encoded += ALPHABET[nextIndex]
        else:
            encoded += character
    return encoded

text = open("hamlet.txt", 'r')
message = text.read()
text.close
print(caesar(message))
