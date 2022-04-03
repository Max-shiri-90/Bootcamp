import re

pattern = r'(^[a-zA-Z]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{3,320}\.[a-zA-Z]{2,3}$)'


def regex_mail(email):
    if re.fullmatch(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")


regex_mail(email='max.shiri90@gmail.com')

