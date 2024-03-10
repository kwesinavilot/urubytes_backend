import random
from django.core.mail import EmailMessage

# function to generate One-Time-Pins (OTP)
# OTP should be 6 chars long, between 1 and 9
def generateOTP():
    otp = ""

    for i in range(6):
        otp = otp + str(random.randint(0, 9))

    return otp
