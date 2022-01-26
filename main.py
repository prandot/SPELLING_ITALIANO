import pandas

# TODO 1. Create a dictionary in this format:
ita_dict = {row.LETTERA: row.PAROLA for (index, row) in pandas.read_csv("spelling_italiano.csv").iterrows()}
# print(ita_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
tospell = input("Scrivi una parola da fare lo spelling: ").upper().replace(" ", "")
result = [ita_dict[n] for n in tospell]
print(result)
