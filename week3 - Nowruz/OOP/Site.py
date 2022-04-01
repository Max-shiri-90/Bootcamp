class Site:
    def __init__(self, url, register_users, active_users):
        self.url = url
        self.register_users = register_users
        self.active_users = active_users

    def register(self, user):
        username = user.username
        if username in self.register_users:
            raise Exception("user already registered")
        else:
            self.register_users.append([username, user.password, user.phone_number, user.email])
            return "register successful"

    def login(self):
        pass

    def logout(self):
        pass
