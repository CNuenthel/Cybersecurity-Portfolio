# This script utilizes the Twilio API and a registered trial account to send messages over SMS with
# a verification code to authenticate on username and login, as well as a passcode sent to a
# secondary device.

from twilio.rest import Client
import pyotp
import json

# Load configuration data
with open("config.json", "r") as f:
    config = json.load(f)


def login_start() -> str:
    # Collect email to send 2fa code to
    receiving_phone_number = input("Please input your phone number: ")

    # Sanitize phone number input to collect only numeric information
    num_check_list = [str(num_count) for num_count in range(10)]
    sanitized_phone_number = "".join([num for num in receiving_phone_number if num in num_check_list])

    # Collect a username and password, emulating a normal login process to begin 2fa process
    input("Username: ")
    input("Password: ")

    # Return receiving email address
    return sanitized_phone_number


def send_sms(receiver_phone_number):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = config["twilio_id"]
    auth_token = config["twilio_auth"]
    client = Client(account_sid, auth_token)

    # create a random base 32 key
    # this can be done prior, and the key may be saved in a secure location to be referenced
    key = pyotp.random_base32()

    # Create a time based one-time password
    totp = pyotp.TOTP(key)
    passcode = totp.now()

    # Create message body for 2fa
    message = f"Hello! Your one time passcode is: {passcode}"

    message = client.messages \
        .create(
             body=f'Your one time passcode is {passcode}',
             from_='+18334183417',
             to=f"+1{receiver_phone_number}"
         )
    print(type(totp))
    print(type(message.sid))
    return totp


def verify_2fa(totp):
    # Verify Passcode
    passcode_input = input("Enter one time passcode: ")

    # If user input is correct to email sent in 2fa, totp verification will return true and user is notified
    if totp.verify(passcode_input):
        print("You have successfully logged on with two factor authentication")
        return

    # If user takes too long, or fails to input the correct passcode, user fails to login
    print("You have failed to log in with two factor authentication, buh buh buuuuuuh")


if __name__ == "__main__":
    phone_number = login_start()
    mfa_password_verifier = send_sms(phone_number)
    verify_2fa(mfa_password_verifier)
