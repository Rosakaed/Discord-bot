import discord
import praw
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

ri = os.getenv('rid')
rsecret = os.getenv('rsec')
ruser = os.getenv('user')
password= os.getenv('pass')
dbot = os.getenv('dtoken')
intents = discord.Intents.all()

client = commands.Bot(command_prefix="r/", case_insensitive=True,intents=intents)
client.remove_command("help")

reddit = praw.Reddit(client_id=ri,client_secret=rsecret, username=ruser, password=password, user_agent='prawns')


@client.event
async def on_ready():
    print("Welcome to rcrawl, {0.user}".format(client))

@client.command()
async def hello(ctx):
    await ctx.send("hi")


@client.command()
async def hot(ctx, subsr):
    all_submission = []
    try:
        subreddit = reddit.subreddit(subsr)
        hot = subreddit.hot(limit=50)
        for submission in hot:
            all_submission.append(submission)
        rand = random.choice(all_submission)
        while rand.stickied:
          rand=random.choice(all_submission)
        em = discord.Embed(title=rand.title, description=f"{rand.url}", )
        em.set_image(url=rand.url)
        em.add_field(name=f"Updoots:", value=rand.ups)
        await ctx.send(embed=em)
    except:
        await ctx.send("Subreddit not found")


@client.command()
async def top(ctx, subsr):
    all_submission = []
    try:
        subreddit = reddit.subreddit(subsr)
        hot = subreddit.top(limit=50)
        for submission in hot:
            all_submission.append(submission)
        rand = random.choice(all_submission)
        while rand.stickied:
          rand=random.choice(all_submission)
        em = discord.Embed(title=rand.title, description=f"{rand.url}", )
        em.set_image(url=rand.url)
        em.add_field(name=f"Updoots:", value=rand.ups)
        await ctx.send(embed=em)
    except:
        await ctx.send("Subreddit not found")



@client.command()
async def new(ctx, subsr):
    all_submission = []
    try:
        subreddit = reddit.subreddit(subsr)
        hot = subreddit.new(limit=50)
        for submission in hot:
            all_submission.append(submission)
        rand = random.choice(all_submission)
        while rand.stickied:
          rand=random.choice(all_submission)
        em = discord.Embed(title=rand.title, description=f"{rand.url}", )
        em.set_image(url=rand.url)
        em.add_field(name=f"Updoots:", value=rand.ups)
        await ctx.send(embed=em)
    except:
        await ctx.send("Subreddit not found")




@client.command()
async def help(ctx):
  await ctx.send("Use r/commands to get a list of commands to begin your experience")

@client.command()
async def commands(ctx):
  await ctx.send("Welcome to Heddit!!\nHere is the list of commands\n\nr/hot subreddit_name :Get a random hot post from subreddit\nr/top subreddit_name :Get a random top post from subreddit\nr/new subreddit_name :Get a random new post from subreddit\nEnter subreddit name without the Apostrophe")



client.run(dbot)
