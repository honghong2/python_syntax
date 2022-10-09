def print_upper_words(words):
    for word in words:
        print(word.upper())

print_upper_words(["dfds", "DeDCrer"])

def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())



def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break



print_upper_words3(["egh", "abc","thj"], {"h", "a", "t"})

