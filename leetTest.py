import itertools
import re
from datetime import datetime

def leet_conversion(word):
    leet_dict = {'a': '4', 'e': '3', 'g': '6', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    leet_word = ''
    for char in word:
        if char.lower() in leet_dict:
            leet_word += leet_dict[char.lower()]
        else:
            leet_word += char
    return leet_word

def join_words(word1, word2):
    combined_words = [word1 + word2, word2 + word1]
    combined_words = [leet_conversion(word) for word in combined_words]
    return combined_words

def format_date(dt):
    formats = ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%d/%m/%Y']
    date_strings = [dt.strftime(fmt) for fmt in formats]
    return date_strings

def main():
    with open('input.txt', 'r') as file:
        words = [line.strip() for line in file]
        leet_words = [leet_conversion(word) for word in words]

    combined_words = []
    for i in range(len(leet_words)):
        for j in range(i+1, len(leet_words)):
            combined_words.extend(join_words(leet_words[i], leet_words[j]))
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    gods = ['Zeus', 'Jupiter', 'Apollo', 'Venus']
    date_strings = []
    for word in words:
        match = re.match(r'\d{4}-\d{2}-\d{2}', word)
    if match:
        dt = datetime.strptime(word, '%Y-%m-%d')
        date_strings.extend(format_date(dt))

    with open('output.txt', 'w') as file:
        for word in leet_words:
            file.write(word + '\n')
            file.write(word.capitalize() + '\n')
        for word in combined_words:
            file.write(word + '\n')
            file.write(word.capitalize() + '\n')
        for season in seasons:
            for word in leet_words:
                file.write(season + word + '\n')
                file.write(season + word.capitalize() + '\n')
        for god in gods:
            for word in leet_words:
                file.write(god + word + '\n')
                file.write(god + word.capitalize() + '\n')
        for date_string in date_strings:
            file.write(date_string + '\n')

if __name__ == '__main__':
    main()
