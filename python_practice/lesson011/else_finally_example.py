users = [
    {"name": "Alex", "scores":{"math": 0, "philosophy": 60, "literature": 20}},
    {"name": "Den", "scores":{"math": 0, "philosophy": 60}},
    {"name": "Ivan", "scores":{"math": 0, "philosophy": 60, "literature": None}},
    {"name": "Sofa", "scores":{"math": 0, "philosophy": 0, "literature": 0}},
    {"name": "Viktor", "scores":{}},
    {"name": "Alehandro", "scores":{"math": 0, "philosophy": 60, "literature": 20}}
]

def get_user_score(user):
    scores = user.get("scores")
    sum_ = 0
    for s in scores:
        try:
            sum_ += scores[s]
        except TypeError:
            print(f"Get None for {s}")
    try:
        result = sum_ / len(scores)
    except ZeroDivisionError:
        print(f"No data for user {user['name']}")
        return 0
    else:
        print("We can see this only if no errors appeared")
    finally: #виконується в будь-якому випадку
        print(f"Finally: user has score: {sum_}")
    return result

for user in users:
    print(f"User name is {user['name']}")
    print(f"User score is {get_user_score(user)}")
    print("-" * 80)

# try
# many except
# else
# finally