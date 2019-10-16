from twilio.rest import Client

#testaccountSid = 'AC493a8129f20a252cf14bd490948c0b00'
#testAuthToken = '50a36dbec29da8d7ac44ab1cf9700b7d'
#client = Client(testaccountSid, testAuthToken)

accountSid = 'ACd40fb677edaf206f6ac8f70cda89de08'
authToken = '4426a8b9a4b1c2819611669ddcc5c80c'
client = Client(accountSid, authToken)

print("Sending message...")
myMessage = client.messages.create(body="$2", from_='+12624574265', to='+254717270977')
#myMessage = client.messages.create(body="$2", from_='+15005550006', to='+254717270977')
print("Sent message")
