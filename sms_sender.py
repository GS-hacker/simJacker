import africastalking

username = "sandbox"
api_key = "732c67db06ce4d51ed0afa83a689da10456d8c98781c2399c3dc7858eee2d247"

africastalking.initialize(username, api_key)
sms = africastalking.SMS


# response  = sms.send("Hello Msg", ["+254793723138"])
# print(response)

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

message=input("enter a message:")
number=input("enter a number{+254793723138}:")
sms.send(message, [number], callback=on_finish)
