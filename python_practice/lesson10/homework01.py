class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language,
        )
        self.team_size = team_size


team_lead = TeamLead(
    "Іван",
    5000,
    "IT",
    "Python",
    8
)

assert hasattr(team_lead, "name")
assert hasattr(team_lead, "salary")
assert hasattr(team_lead, "department")
assert hasattr(team_lead, "programming_language")
assert hasattr(team_lead, "team_size")

print("Усі тести пройдено!")