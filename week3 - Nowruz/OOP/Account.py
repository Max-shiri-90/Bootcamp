import re
import hashlib


class Account:
    def __init__(self, username, password, phone_number, email):

        if re.match('^[a-zA-Z]+_[a-zA-Z]+$', username):
            self.username = username
        else:
            raise Exception("invalid username")

        if re.match('^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)){8,40}$', password):
            self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        else:
            raise Exception("invalid password")

        if re.match('^09\d{9}$', phone_number):
            self.phone_number = phone_number
        elif re.match('^\+989\d{9}$', phone_number):
            self.phone_number = phone_number
        else:
            raise Exception("invalid phone number")

        if re.match('^([\w\.\-]+)@([\w\.\-]+)((\.([a-zA-Z]){2,5})+)$', email):
            self.email = email
        else:
            raise Exception("invalid email")


acc1 = Account('Masoud_Shiri', 'Aa123123', '09118873087', 'max.shiri.90@gmail.com')

print(acc1.username)
