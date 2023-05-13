class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()
        return False


first_user = User("SASHA")
second_user = User("sasha")
print(first_user == second_user)
