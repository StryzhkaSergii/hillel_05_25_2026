user = [
    {"name": "Alex", "math": 0, "philosophy": 60},
    {"name": "Den", "math": 50, "philosophy": 55},
    {"name": "Ivan", "math": 50, "philosophy": None},
    {"name": "Ivan", "math": 50}
]

def test_count_score(user_list):
    for k in user_list:
        # if k["philosophy"] is None: bad variant
        #     continue
        try:
            assert k["math"] + k["philosophy"] > 0
            print(k["name"], k["math"] + k["philosophy"])
            print("Test passed")
            print("-"*80)
        except TypeError as exception_instance:
            print(f"Can't get correct data for {k}")
            print("Warning! Bad data")
            print(exception_instance)
            print("-" * 80)
        except KeyError as key:
            print(f"No key {key} in file! It's a bug")
            print("Test failed")
            print("-" * 80)
        except Exception as e:
            print("Some unexpected error happened")
            print(e)


test_count_score(user)
assert 1==1 # check True if not True raise AssertionError
# assert False