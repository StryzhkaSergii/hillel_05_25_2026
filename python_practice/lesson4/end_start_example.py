sent = 'Would you tell me, please, which way I ought to go from here?'

print(sent.startswith("Would"))
print(sent.startswith("Could"))
print(sent.endswith("here?"))
print(sent.endswith("here!"))

for word in sent.split():
    word_lower = word.lower()
    print(f"word {word} starts with \'w\': {word.startswith("w")}")