# This script utilizes the Python smtp library to authenticate user login using 2fa by sending a one time passcode
# to a user email address following login.

import pyotp
import smtplib
import ssl
import json

from email.message import EmailMessage
from pyotp import TOTP

# Load configuration data
with open("config.json", "r") as f:
    config = json.load(f)


def login_start() -> str:
    # Collect email to send 2fa code to
    receiving_email_address = input("Please input your email address: ")

    # Collect a username and password, emulating a normal login process to begin 2fa process
    dummy_login = input("Username: ")
    dummy_pass = input("Password: ")

    # Return receiving email address
    return receiving_email_address


def send_verification_code(receiving_email: str) -> TOTP:
    email_sender = "nuentheldev@gmail.com"

    # Passcode for app is obtained through google account settings, two factor auth turned on
    email_password = config["ndevGooglePass"]
    email_receiver = receiving_email

    # create a random base 32 key
    # this can be done prior, and the key may be saved in a secure location to be referenced
    key = pyotp.random_base32()

    # Create a time based one-time password
    totp = pyotp.TOTP(key)
    passcode = totp.now()

    # Create message body for 2fa
    message = f"Hello! Your one time passcode is: {passcode}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = message
    em.set_content(message)

    # Create context for TLS
    context = ssl.create_default_context()

    # With smtplib SSL as server we make a connection with gmails smtp server to initiate TLS encrypted connection
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())

    return totp


def verify_2fa(totp):
    # Verify Passcode
    passcode_input = input("Enter one time passcode: ")
    print(totp.verify(passcode_input))

    # If user input is correct to email sent in 2fa, totp verification will return true and user is notified
    if passcode_input:
        print("You have successfully logged on with two factor authentication")
        return

    # If user takes too long, or fails to input the correct passcode, user fails to login
    print("You have failed to log in with two factor authentication, buh buh buuuuuuh")


if __name__ == '__main__':
    user_email = login_start()
    mfa_password = send_verification_code(user_email)
    verify_2fa(mfa_password)