import hashlib


class Site:
    def __init__(self, url, register_users, active_users):
        self.url = url
        self.register_users = register_users
        self.active_users = active_users

    def register(self, user):
        username = user.username
        if username in self.register_users[0]:
            raise Exception('user already registered')
        else:
            self.register_users.append([username, user.password, user.phone_number, user.email])
            return 'register successful'

    def login(self, user):
        password = hashlib.sha256(user['password'].encode('utf-8')).hexdigest()

        if 'username' and 'password' and 'email' in user:
            if password == self.register_users[1] and user['email'] == self.register_users[-1]:
                self.active_users.append(self.register_users[0])
                return 'login successful'
            elif self.register_users[0] in self.active_users:
                return 'user already logged in'
            else:
                return 'invalid login'

        elif 'username' and 'password' in user:
            if password == self.register_users[1]:
                self.active_users.append(self.register_users[0])
                return 'login successful'
            elif self.register_users[0] in self.active_users:
                return 'user already logged in'
            else:
                return 'invalid login'

        elif 'password' and 'email' in user:
            if password == self.register_users[1]:
                self.active_users.append(self.register_users[0])
                return 'login successful'
            elif self.register_users[0] in self.active_users:
                return 'user already logged in'
            else:
                return 'invalid login'

        else:
            return 'invalid login'

    def logout(self, user):
        if user.username in self.active_users:
            self.active_users.remove(user.username)
            return 'logout successful'
        else:
            return 'user is not logged in'
