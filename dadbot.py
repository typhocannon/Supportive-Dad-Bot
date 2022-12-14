# dadbot.py
import os
from tabnanny import check
import discord
import random
import string
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive

keep_alive()

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
    if "i'm" in list or "im" in list or "I'm" in list or "Im" in list or "IM" in list or "I’m" in list or "i’m" in list or "I’M" in list or "I'M" in list: 
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
            if word.lower() == "i'm":
                index = list.index(word)
            elif word.lower() == "im":
                index = list.index(word)
            elif word.lower() == "i’m":
                index = list.index(word)
        
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
        # Currently has 30 quotes
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
            f"Hey {name.capitalize()}, I'll leave the rest to you.",
            f"Hi {name.capitalize()}! Cooked your favorite today. Hurry on home!",
            f"Hey {name.capitalize()}! Remember I'm always there for you. Give your old man a call some times alright?",
            f"{name.capitalize()}, Never stop fighting.",
            f"Hey {name.capitalize()}! Look! I've learned the moves of the youth. ✊👊. Pretty swag from your pops right?",
            f"Hi there {name.capitalize()}, went to the market today and this reminded me of those anime things you like! Here ya' go kiddo! You call these uhh a 'waifu'? I think.",
            f"Hey {name.capitalize()}, wanna listen to some old bangers with your old man?",
            f"Hey {name.capitalize()}, you've grown up so much. I'm proud of you.",
            f"Hi {name.capitalize()}, looks like you've been online for a while. Do you wanna take a break and play some catch with your dear ol' dad?",
            f"Hey {name.capitalize()}, Stay strong kiddo. Greatness awaits you, I know it.",
            #30
        ]
        
        # If user calls themself supportive dad bot it has a special message
        bot_name = 'Supportive Dad Bot'
        if name == bot_name.lower():
            response = "Hey! That's me! Haha great joke kiddo."
        else:
            # Chooses randomly between 0 and 1 to see if it takes original quote (0) or webscrapes (1)
            num = random.randint(0, 1)
            if num == 1:
                response = random.choice(father_quotes)
            else:
                # url to scrape the joke from
                URL = "https://icanhazdadjoke.com/"
                page = requests.get(URL)
                
                # parse the html from the url
                soup = BeautifulSoup(page.content, "html.parser")
                
                # find the area that contains the joke
                joke = soup.find("p", "subtitle")
                joke2 = joke.prettify()

                # get the text by removing the html objects from the joke
                joke3 = BeautifulSoup(joke2, 'html.parser')
                joke3 = joke3.get_text()
                joke4 = joke3.strip()
                
                # random number between 0 and 2 to see which greeting to use
                num2 = random.randint(0, 2)
                if num2 == 0:
                    greeting = f"Hey there {name.capitalize()}, "
                elif num2 == 1:
                    greeting = f"Hi {name.capitalize()}, "
                else:
                    greeting = f"Hey {name.capitalize()}! "
                response = greeting + joke4
        print(response)
        await message.channel.send(response)
    else:
        print("no im")
        return

client.run(TOKEN)