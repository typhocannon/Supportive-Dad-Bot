# dadbot.py
import os
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
    
    # default variables for index and name
    index = -1
    name = 'dsdfsdfsdgsdgshsoekfseos'

    # checks if I'm or im is in the message to commence dad joke
    if "i'm" in message.content.lower() or "im" in message.content.lower():
        # creating a list of words in the message
        list = message.content.split()

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
        
        # check if index is valid
        if index != -1:
            name = list[index + 1]

        # check if name is valid
        if name != 'dsdfsdfsdgsdgshsoekfseos':
            # check if the next word is 'a' or 'your'
            if name.lower() == 'a':
                name = name + ' ' + list[index + 2]
            elif name.lower() == 'your':
                name = name + ' ' + list[index + 2]
            # get rid of puncuation in the name
            name = name.translate(str.maketrans('', '', string.punctuation))
            # debug check if name is correct
            print(name)

        # list of quotes from a supportive father
        # Currently has 19 quotes
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
        ]
        response = random.choice(father_quotes)
        await message.channel.send(response)

client.run(TOKEN)