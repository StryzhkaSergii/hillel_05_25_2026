# sent = "Alex My name is Alex"
#
# print(sent.find("Alex"))
# print(sent.find("Oleg"))
#
# if sent.find("Alex") >=0:
#     print(True)
#
# if "Alex" in sent:
#     print("Alex in the sentence")
#
# is_index = sent.find("is")
# result_sent = sent[:is_index]
# print(result_sent)

# sent = "Alex My name is Alex"
# search_word = "Alex"
#
# search_word_index = sent.find(search_word)
# len_of_search_word = len(search_word)
# end_index = search_word_index + len_of_search_word
# result_sent = sent[end_index:]
# print(result_sent)


sent = 'Would you tell me, please, which way I ought to go from here?'

list_of_words = sent.split()
print(list_of_words)

join_string = "+".join(list_of_words) # працює тільки з стрінгами
print(join_string)
join_string = "+".join(sent)
print(join_string)
join_string = " ".join(sent)
print(join_string)