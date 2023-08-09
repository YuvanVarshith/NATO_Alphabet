import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def nato():
    word = input("Enter you name: ").upper()
    try:
        output = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry!, only letters in the alphabet please.")
        nato()
    else:
        print(output)
nato()