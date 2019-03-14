from nltk.chat.util import Chat, reflections
from random import randint

pairs = [
    [
        r"hello|hi|hey(.*)",
        ["Hello, how may we help you?", ]
    ],

    [
        r"(.*) want (.*) return (.*) goods",
        ["Are the goods damaged or expired?"]
    ],
    [ 
        r"(.*) damaged",
        ["Please select- 1.On shelf Damage , 2. Cutomer Damage, 3. Transportation Damage"]

    ],
    [
        r"damaged",
        ["Please select- 1.On shelf Damage , 2. Cutomer Damage, 3. Transportation Damage"]
    ],
    [
        r"1(.*)|2(.*)|3(.*)" ,
        ["Please send us a picture of the damaged product your request ID is "+ str(randint(1, 3500))+". We will reach back to you as soon as possible."]
    ],
    [
        r"(.*)expired(.*)",
        ["Thankyou for reporting, your request ID is "+ str(randint(1, 3500))+" we will send a salesman to pick it up as soon as possible."]
    ],

    [
        r"okay",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ]  ,
    [
        r"(.*)",
        [
            " Hi!Do you want to send damaged or expired goods?" 
        ]
    ]

]
# def chatty():
#     print("Hi, I'm Chitti and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ")  # default message at the start


# # chat = Chat(pairs, reflections)
# # chat.converse()
# if __name__ == "__main__":
#     chatty()
