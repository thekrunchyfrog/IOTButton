import config
from twilio.rest import TwilioRestClient

account_sid = config.sid
auth_token = config.token

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to=config.addressBook[1], from_="+18563222875", body="Hello there!")
