import os

import Password_generator
import time
from twilio.rest import Client
def logic():
    generated_pass = Password_generator.password_gen.password()

    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    ''' Change the value of 'from' with the number 
    received from Twilio and the value of 'to'
    with the number in which you want to send message.'''

    stringed = "".join(generated_pass)

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
