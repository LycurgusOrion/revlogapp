from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import chatbot3 as cb
import time

import CreateDB as cd
import random as rd


chat = cb.Chat(cb.pairs, cb.reflections)

# Your Account SID from twilio.com/console
account_sid = "ACdb9304b0c1a9736432c77d3ce495e3f5"
# Your Auth Token from twilio.com/console
auth_token  = "f5db2c220080ad842bd8539b41960049"

f = ""

while True:
    print("hi")
    
    id_ = rd.randint(1, 5000)
    time.sleep(5)

    client = Client(account_sid, auth_token)

    sms = client.messages.list()[0]
    msg = client.messages(sms.sid).fetch()

    print("hi")

    # if (("thankyou" in msg.body.lower()) or ("picture" in msg.body.lower())):
    #     msg.body = msg.body + ". Your Request ID is " + str(id_) + "."

    # if ("search" in msg.body.lower()):
    #     id_s = int(msg.body.split()[1])
    #     st = "SELECT STATUS FROM LOG WHERE REQ_ID == " + str(id_s)
    #     status = str(cd.curr.execute(st).fetchall())
    #     message = client.messages.create(
    #         body = chat.respond("Status is " + status),
    #         from_ = "whatsapp:+14155238886",
    #         to= "whatsapp:+919582906389"
    #     )

        # message = client.messages.create(
        #     body = chat.respond("Status is " + status),
        #     from_ = "+14155238886",
        #     to= "+919582906389"
        # )

    # if len(msg) != f:
    if ("okay" in msg.body.lower()):
        break
    # sms_reply(msg)

    if (len(msg.body) <= 0) or (f == msg.body):
        continue

    message = client.messages.create(
        body = chat.respond(msg.body),
        from_ = "whatsapp:+14155238886",
        to= "whatsapp:+919582906389"
    )

    # message = client.messages.create(
    #     body = chat.respond(msg.body),
    #     from_ = "+14155238886",
    #     to= "+919582906389"
    # )

    f = msg.body
    print(msg.body)

    # if ("return" in msg.body.lower()):
    #     data = [(id_, "PENDING")]
    #     cd.curr.execute("INSERT INTO LOG(R_ID, REQ_ID, D_ID, STATUS) VALUES(1125, 231, 334, \"PENDING\")")
    # f = len(msg)
    time.sleep(10)
    # for i in msg:
    #     print(i.body)