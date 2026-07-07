# global
# local
# non local
# build in functions

dog_name = "Richi" #global

def doc_actions(name):
    dog_name = name #non local
    def make_sound():
        # dog_name = "Archi"
        global dog_name
        print(dog_name)

    make_sound()
    print(dog_name)

doc_actions("naida")
print(dog_name)

#local -> non-local -> global