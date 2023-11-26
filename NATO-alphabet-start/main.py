import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("What is your word?: ").upper()
output_list = word_to_nato = [nato_alphabet[letter] for letter in word]

print(word_to_nato)
