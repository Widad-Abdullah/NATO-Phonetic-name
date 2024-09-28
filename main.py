import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dic={row.letter:row.code for (index,row) in data.iterrows()}

# printed=False
# while not printed:
#     name = input("Enter your name: ").upper()
#     try:
#         out = [nato_phonetic_dic[i] for i in name]
#     except KeyError:
#         print("Enter Only Alphabets please...")
#     else:
#         print(out)
#         printed=True

def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        out = [nato_phonetic_dic[i] for i in name]
    except KeyError:
        print("Enter Only Alphabets please...")
        generate_phonetic()
    else:
        print(out)

generate_phonetic()
