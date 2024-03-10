import random
# from django.core.mail import EmailMessage

# function to generate One-Time-Pins (OTP)
# OTP should be 6 chars long, between 1 and 9

def generateOrgID():
    orgID = 'UBO'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    for i in range(4):
        orgID += letters[random.randint(0, len(letters)-1)]

    for i in range(3):
        orgID += numbers[random.randint(0, len(numbers)-1)]

    return orgID

def generateUserID():
    userID = 'UBU'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    for i in range(4):
        userID += letters[random.randint(0, len(letters)-1)]

    for i in range(3):
        userID += numbers[random.randint(0, len(numbers)-1)]

    return userID


