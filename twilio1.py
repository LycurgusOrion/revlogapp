from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9fadcfd9020ff53c16e57ba255617f5b"
# Your Auth Token from twilio.com/console
auth_token  = "705e042c3ead910baca828645f59e59e"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+919582906389",
    from_="+19497994192",
    url="http://demo.twilio.com/docs/voice.xml")

print(call.sid)