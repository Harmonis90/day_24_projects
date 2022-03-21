
with open("./Input/Names/invited_names.txt", "r") as name_data:
    names_list = name_data.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_prefab = letter.read()

for name in names_list:
    corrected_name = name.strip()
    formatted_letter = letter_prefab.replace("[name]", corrected_name)
    with open(f"./Output/ReadyToSend/letter_for_{corrected_name}.txt", mode="w") as final_letter:
        final_letter.write(formatted_letter)


