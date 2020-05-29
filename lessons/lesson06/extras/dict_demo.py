"""dictionary demo"""
my_dict = {"Name": "Andy", "Job": "Tutor"}

dict_to_list = []

for key, value in my_dict.items():
    dict_to_list.append((key, value))

assert dict_to_list == [("Name", "Andy"), ("Job", "Tutor")]

# transpose keys and values
my_new_dict = {}
for key, value in my_dict.items():
    my_new_dict[value] = key

dict_to_list = []
for key, value in my_dict.items():
    dict_to_list.append((value, key))

assert dict_to_list == [("Andy", "Name"), ("Tutor", "Job")]


people = [
    {"Name": "Andy", "Job": "Tutor"},
    {"Name": "Fred", "Job": "Analyst"},
    {"Name": "Pam", "Job": "Nurse"},
]

assert people[1]["Name"] == "Fred"


# dictionary keys must be unique; show what happens when they are not
my_dict = {
    "Name": "Andy",
    "Job": "Tutor",
    "Job": "Analyst",
    "Preferred_name": "Andy",
}

assert my_dict == {"Name": "Andy", "Job": "Analyst", "Preferred_name": "Andy"}

# transpose keys and values
my_new_dict = {}
for key, value in my_dict.items():
    my_new_dict[value] = key

assert my_new_dict == {"Andy": "Preferred_name", "Analyst": "Job"}
