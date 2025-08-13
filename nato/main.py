from pyexpat import native_encoding

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
data = {row.letter:row.code for index, row in df.iterrows()}
print(data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# nato = [data.get(key) for nato in name if key in data]
# nato = [data.get(key, "?") for key in name]

def generate_word():
    name = input("what's your name ??").upper()
    try:
        nato = [data[key] for key in name]
    except KeyError as error:
        print(f"please input letters bitch, you input {error}")
        generate_word()
    else:
        print(nato)

generate_word()