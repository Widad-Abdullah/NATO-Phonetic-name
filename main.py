# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
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


