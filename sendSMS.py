from slipProcessor import listOfAssignments
from phoneDB import nameToPhone
from twilio.rest import Client
import time

# Account Credentials (use your Twilio credentials)
accountSID = ''
accountToken = ''

# Connecting to Twilio API
client = Client(accountSID, accountToken)

# Sending SMS
for assignment in listOfAssignments:

    # Formatting Purposes
    time.sleep(5)
    print('-' * 50)

    # Constructing Message
    msgBody = (f'Hi {assignment['Name:']}, here is your assignment slip details for your upcoming talk.\n\nAssistant: '
          f'{assignment['Assistant:']}\nDate: {assignment['Date:']}\nPart No: {assignment['Part No:']}\nGiven In: '
          f'{assignment['Given In:']}\n\nThanks!\n')
    
    # Retrieving Phone Number from Name
    try:
        phoneNumber = 'unknown'
        phoneNumber = nameToPhone[assignment['Name:']]
    except KeyError:
        pass

    # # Message Demo (Debugging Purposes)
    # print(f'\nSending to: {phoneNumber}.\n')
    # print(msgBody)
    
    # Sending Out Messages
    message = client.messages.create(
      from_='', # Your Twilio Number
      body=msgBody,
      to=phoneNumber
    )

    # SMS Verbose Information
    if message.sid:
        print(f'\nSending to: {phoneNumber}.\n')
        print(msgBody)
    else:
        print(f'\nError sending message:')
        print(msgBody)
