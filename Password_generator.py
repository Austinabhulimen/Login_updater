import random

class password_gen:
    def __init__(self, values, passwords, list1):
        self.values = values
        self.passwords = passwords
        self.list1 = list1
    def password():
        passwords = []
        x = 0
        while x < 25:
            values = ['(', '1', ')', 'r', '3', '4', '%', '&', '6', '*']
            passwords.insert(x, (random.choice(values)))
            x += 1
        list1 = list(passwords[0:4])
        return(list1)


    password()
