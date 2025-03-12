# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {data.letter: data.code for (index, data) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        word = input("Enter your word: ").upper()
        #characters = list(word) #TIL: split chars of a word
        output_list = [phonetic_dict[char] for char in word]
        print(output_list)
        break
    except KeyError:
        print("error: enter valid word containing alphabets.")
        continue
