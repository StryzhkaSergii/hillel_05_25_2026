print(isinstance("name", str)) #-> True
print(isinstance("name", int)) #-> False

print(type("name"))
print(type("name") == str) #-> True
print(type("name") == int) #-> False

print(isinstance(False, bool)) # -> True
print(isinstance(False, int)) # -> True
print(isinstance(False, object)) # -> True
print(isinstance("False", object)) # -> True
print(isinstance([1], object)) # -> True
print(isinstance({1:1}, object)) # -> True