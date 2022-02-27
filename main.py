import Password_generator
import time
from twilio.rest import Client
def logic():
    list1 = Password_generator.password()

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'ACf0169bad626e36d7404199ae55ecd308'
    auth_token = '8d6f6248c77938b1e70b7fa098ed9a03'

    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''

    stringed = "".join(list1)

    messages = stringed

    message = client.messages.create(
        from_='+18593507135',
        body=messages,
        to='+13136526912'
    )



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
        time.sleep(4)
        quit()

    else:
        print("Try again, wrong password")

    logic()

logic()
