# dadbot.py
import os
from tabnanny import check
import discord
import random
import string
from dotenv import load_dotenv

# checking intents to be able to send msgs
intents = discord.Intents.default()
intents.members = True

# getting tokens
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# establishing client
client = discord.Client(intents=intents)

# mainly used for debug/client purposes to check if the bot is connected to discord within the terminal
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# called on the event where someone sends a message
@client.event
async def on_message(message):
    # checking if user sent a msg
    if message.author == client.user:
        return
    
    # checks if I'm or im is in the message to commence dad joke
    list = message.content.split()
    if len(list) == 1:
            return
    if "i'm" in list or "im" in list or "I'm" in list or "Im" in list or "IM" in list:
        print("does have I'm")
        # creating a list of words in the message
        index = -1
        name = 'doglogbog'
        # list = message.content.split()
        print(list)
        print(len(list))

        # look through the list to find im 
        for word in list:
            print(word)
            if word == "i'm":
                index = list.index("i'm")
            elif word == "im":
                index = list.index("im")
            elif word == "Im":
                index = list.index("Im")
            elif word == "I'm":
                index = list.index("I'm")
            elif word == "IM":
                index = list.index("IM")
        
        # check if index is valid
        if index != -1:
            for word in list:
                for item in string.punctuation:
                    if list[index + 1] == item:
                        return
                # setting first part of name
                if (index + 1) == list.index(word):
                    name = word
                # setting the next words
                elif index != list.index(word) and word != list[-1]:
                    name = name + ' ' + word
                # setting last word and getting rid of puncuation
                elif word == list[-1]:
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    name = name + ' ' + word

        # list of quotes from a supportive father
        # Currently has 20 quotes
        father_quotes = [
            f"Hi {name.capitalize()}! Hope you're having a great day today.", 
            f'Hi {name.capitalize()}! Have you done the dishes yet? We can get some ice cream afterwards!', 
            f'Hi {name.capitalize()}! Wanna play some catch with your old man?',
            f'Hey there, {name.capitalize()}! Gonna go grab some McDonalds do you want any?',
            f'Hey {name.capitalize()}! Wanna go shoot some hoops with your pops?',
            f"Hey {name.capitalize()}, you're doing great things out there in the world. I hope you know that I'm proud of you.",
            f"Hi {name.capitalize()}. Have you been having a good time lately?",
            f"Hey there, {name.capitalize()}. Even if you can't do it, what matters is that you tried",
            f"Hi {name.capitalize()}, did you know that Edelgard has always been right? You do? Of course you do. You're my favorite person in the whole world.", 
            f"Hey {name.capitalize()}! Make sure you drink water today! Cheers from your old man.",
            #10 
            f"Hey {name.capitalize()}! Looking sharp today!",
            f"Hi {name.capitalize()}! Here's some advice from your old pops: just keep being yourself, alright? You're great just the way you are.",
            f"Hey {name.capitalize()}. Y'know I like telling Dad jokes. Sometimes he laughs! Haha get it? Get it?",
            f"Hi {name.capitalize()}, do you ever wonder when a joke becomes a dad joke? When it becomes apparent! Have a great day kiddo.",
            f"Hi {name.capitalize()}, Hope you're hungry sport! I made your favorite!", 
            f"Hi {name.capitalize()}, I'm dad.",
            f"Hey {name.capitalize()}, Love ya kiddo. Hope your day has been great.",
            f"Hey {name.capitalize()}, you've got a good heart. Don't ever lose it.",
            f"Hi {name.capitalize()}, ready to do some errands with your good ol' pops?",
            f"Hi {name.capitalize()}, are ya' winning?",
            #20
        ]
        bot_name = 'Supportive Dad Bot'
        if name == bot_name.lower():
            response = "Hey! That's me! Haha great joke kiddo."
        else:
            response = random.choice(father_quotes)
        print(response)
        await message.channel.send(response)
    else:
        print("no im")
        return

client.run(TOKEN)