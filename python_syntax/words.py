""" 1-3"""

def print_upper_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

"""4"""
        
def print_upper_words2(words, must_start_with):

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
