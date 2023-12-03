import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("What is your word?: ").upper()
    try:
        output_list = word_to_nato = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
        generate_phonetic()


generate_phonetic()
