from twilio.rest import Client
from sys import argv
script, name = argv

sid = 'xxx'
token = 'yyy'
phone_num = '+12012989453'
phone_dict = {'Andrey': '+7...'}

client = Client(sid, token)

print("Sending SMS to %s..." % name)
message = client.messages.create(
    body = "Hello %s!" % name,
    from_ = phone_num,
    to = phone_dict[name]
)

print("Done")
