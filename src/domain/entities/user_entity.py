class UserEntity:
    def __init__(self, _id, name, email, password):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f'id: {self.id}\nname: {self.name}\nemail: {self.email}'
