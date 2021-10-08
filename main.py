import os

import hikari
import lightbulb
from lightbulb.context import Context
from dotenv import load_dotenv
from hikari import Activity, ActivityType

load_dotenv()
intents = hikari.Intents.ALL

bot = lightbulb.Bot(
    token=os.getenv("DISCORD_TOKEN"),
    prefix="..",
    insensitive_commands=True,
    owner_ids=515586764472320010,
)


@bot.command()
async def ping(ctx: Context):
    await ctx.respond(f"Pong! `{bot.heartbeat_latency * 1_000:.0f}ms`")


bot.run(activity=Activity(name="with mud.", type=ActivityType.PLAYING))
