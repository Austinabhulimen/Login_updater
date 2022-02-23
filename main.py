import random
import time


def timed_login():

    def password():
        passwords = []
        x = 0
        while x < 25:
            values = ['(', '1', ')', 'r', '3', '4', '%', '&', '6', '*']

            passwords.insert(x, (random.choice(values)))

            x += 1

        list1 = list(passwords[0:4])
        print(list1)
        return(list1)





    def logic():
        list1 = password()
        startTime = time.time()
        response = list(input("Please enter password: "))
        executionTime = (time.time() - startTime)
        print(executionTime)

        if executionTime > 20:
            print(f"Password expired!........{executionTime}")
            time.sleep(5)
            logic()
        elif response == list1:
            print("Welcome")

        else: print("Try again, wrong password")

    logic()


timed_login()
