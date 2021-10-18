from string import ascii_lowercase

def is_pangram(sentence):
    alphabet = ascii_lowercase
    for letter in sentence.lower():
        alphabet = alphabet.replace(letter, "")
    return len(alphabet) == 0