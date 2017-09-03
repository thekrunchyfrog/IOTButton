import config
from twilio.rest import TwilioRestClient


def sendMessage():
    account_sid = config.sid
    auth_token = config.token

    client = TwilioRestClient(account_sid, auth_token)

    client.messages.create(to=config.addressBook[1], from_="+18562428907", body="Hello there!")

