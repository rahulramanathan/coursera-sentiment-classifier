punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char,"")
    return word


print(strip_punctuation("R:ah,ul;"))
