import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dic={row.letter:row.code for (index,row) in data.iterrows()}

name=input("Enter your name: ").upper()

out=[nato_phonetic_dic[i] for i in name]
print(out)



