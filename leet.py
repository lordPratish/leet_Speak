def leet_speak(word):
    word = word.lower()
    word = word.replace("a", "4")
    word = word.replace("e", "3")
    word = word.replace("g", "6")
    word = word.replace("i", "1")
    word = word.replace("o", "0")
    word = word.replace("s", "5")
    word = word.replace("t", "7")
    return word.capitalize()

def word_variations(word):
    variations = [word, word.upper(), word.capitalize()]
    word = word.lower()
    variations.extend([
        word + "123",
        word + "!@#",
        word + "xyz",
        word + "2019"
    ])
    return variations

def add_seasons(word):
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    variations = [word + season for season in seasons]
    return variations

def add_gods(word):
    gods = ["Zeus", "Jupiter", "Apollo", "Venus"]
    variations = [word + god for god in gods]
    return variations

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    with open(input_file, "r") as f:
        words = f.readlines()
    words = [word.strip() for word in words]
    leet_words = [leet_speak(word) for word in words]
    combined_words = []
    for i in range(len(leet_words)):
        for j in range(i+1, len(leet_words)):
            combined_words.extend(join_words(leet_words[i], leet_words[j]))
    single_word_variations = []
    for word in leet_words:
        single_word_variations.extend(word_variations(word))
        single_word_variations.extend(add_seasons(word))
        single_word_variations.extend(add_gods(word))
    all_variations = combined_words + single_word_variations
    with open(output_file, "w") as f:
        f.write("\n".join(all_variations))

if __name__ == "__main__":
    main()
