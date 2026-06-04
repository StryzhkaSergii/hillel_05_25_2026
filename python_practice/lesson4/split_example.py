sent = '"Would you tell me, please, which way I ought to go from here?"'

my_phrase = sent.split(",")
print(my_phrase)
print(type(my_phrase))
print(f"first phrase = {my_phrase[0]}")
print(f"second phrase = {my_phrase[1]}")

print(sent.split(" "))

copy_sent = '"Would you       tell me,     please,     which way I ought       to go from here?"'

space_split = copy_sent.split(" ")
default_split = copy_sent.split()

# for element in default_split:
#     new_element = f"this element is {element}"
#     print(new_element)

sentence_to_check = default_split

correct_sentence = True
for element in sentence_to_check:
    if element == "":
        correct_sentence = False

print(f"Sentence correct: {correct_sentence}")

# print(space_split)
# print(default_split)