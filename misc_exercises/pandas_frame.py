import pandas

student_dict = {
    "student": ['Angela', "James", "Lily"],
    "score": [56, 76, 98]
}

# # looping through dict
# for (key, value) in student_dict.items():
#     print(key, value)

# print as a DataFrame
student_data_frame = pandas.DataFrame(student_dict)
# for key, value in student_data_frame.items():
#     print(value)

for index, row in student_data_frame.iterrows():
    print(f"{row.student}: {row.score}") # every row is a pandas series object. Objects have dot notation