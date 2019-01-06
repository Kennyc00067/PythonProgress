import boto3


client = boto3.client('sns', 'us-east-1')

client.set_sms_attributes(
    attributes={
        "DefaultSenderID": "KrypticStudio",
    }
)

pnList = ['12543943274']
 
message = 'U wnt sum fuk?'

for phoneNumber in pnList:
    try:
        client.publish(PhoneNumber = phoneNumber, Message = message)
        print('Message Sent!\n Phone Number: {}'.format(phoneNumber))
    except:
        print("\nMessage Failed.\n Phone Number: {}".format(phoneNumber))