import pandas
data = pandas.read_csv('nato_alphabet.csv')



new_dictionary={row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()


nato_list = [new_dictionary[letter] for letter in word]
print(nato_list)