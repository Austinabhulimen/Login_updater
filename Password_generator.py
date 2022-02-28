import random
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
