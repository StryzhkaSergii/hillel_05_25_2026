# pare key = value

# ключі унікальні і хешабельні

my_dict = {"name": "Alex", "age": 29, "has_job": True}
print(my_dict)

my_dict["new_key"] = "new_value"
print(my_dict)

my_dict["new_key"] = "new_value_updated"
print(my_dict)

new_dict_update = {"key1": "value1"}
my_dict.update(new_dict_update)

my_dict["new_dict_key"] = new_dict_update
print(my_dict)

# get

print(my_dict["age"])

# error

# print(my_dict["age1"])

print(my_dict.get("key1"))
print(my_dict.get("new_dict_key", "Alex default").get("key1"))
