#imports for the project
import discord
from discord.ext import commands
import os
import random
import praw 
from time import sleep

reddit = praw.Reddit(client_id="yourclientid",
                    client_secret="yourclientid",
                    user_agent="Made by EZCLAP03")

#setup for your discord bot
client = commands.Bot(command_prefix="/")

istatus = discord.Status.do_not_disturb # you can change this to idle or active or whatever you like
cstatus = discord.Game(name="on discord.")
client = discord.Client(status=istatus,activity=cstatus)

def get_meme():
    subreddit = ['memes', 'pewdiepiesubmissions', 'MemeEconomy', 'dankmemes', 'PrequelMemes', 'terriblefacebookmemes']
    # let the Reddit's internal API handle the random post picking for us.
    for submission in reddit.subreddit(random.choice(subreddit)).new(limit=10):
        embed = discord.Embed(
            title = f'{submission.title}',
            colour = discord.Color.blue()
        )

    embed.set_footer(text=f'posted by u/{submission.author}.')
    embed.set_image(url=submission.url)
    
    return embed  

def eightball():
    #this func is for the 8ball functionality in most bots
    answers = ['no', 'yes', 'definitely not', 'absolutely']# you can add on as many answers as you like
    sent_answer = random.choice(answers)

    return sent_answer

def get_game():
    games = ['csgo', 'valorant', 'hitman', 'GTA V']# you can add how many ever games you want in here.
    game_to_play = random.choice(games)
    
    return game_to_play


def loot(user_id):

    self.user_id = user_id

    if user_id.startswith('<'):
        status = 'user found'
        money = random.randint(0, 500)
        x = f'you stole {money} coins from {user_id}'
            
        f=open("database.txt", "a")
        f.write(f'{user_id}:{money}\n')
        f.close()

        return status

    if user_id.startswith('@'):
        status = 'no user found'
        return status

    if user_id.startswith(''):
        status = 'no user found'
        return status
    
    def get_money():
        author = discord.Message.author.name

    

def random_guess():
    number = random.randint(0, 10)
    return number




#indication that the bot is ready
@client.event
async def on_ready():
    print("Bot ready!")

#executing all the classes
@client.event
async def on_message(message):
    if message.content.startswith('/meme'):# you can change the /meme to whatever command you like
        embed = get_meme()
        await message.channel.send(embed=embed)
    
    if message.content.startswith('/loot'):
        q = message.content.split('/loot')
        q = q.strip()
        loot(q)
        await message.channel.send('kinda works')
        
    if message.content.startswith('/8ball'):
        q = message.content.split('/8ball')

        if q.startswith('why' or 'when' or 'how' or 'what' or 'where'):
            await message.channel.send('Ask me facts!')
        
        else:
            answer = eightball()
            await message.channel.send(answer)

    if message.content.startswith('/what game should we play'):
        game = get_game()
        await message.channel.send(f'Play {game}')
    
    if message.content.startswith('/guess the number'):
        await message.channel.send('I will generate a random number between 1-10. You get one chnace and if you guess the number you get 500 coins.')
        answer = random_guess()
        
        f = open('database.txt', 'a')
        f.write('this works\n')
        f.close()



client.run('yourid', bot=True)# place you discord token here. Do not share this code on github with the token.