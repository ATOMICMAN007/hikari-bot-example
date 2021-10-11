import os

import hikari
import lightbulb
from dotenv import load_dotenv
from lightbulb.context import Context

load_dotenv()
owners = (515586764472320010,)
bot_guilds = (771293539928637470,)
prefix = ("..",)

bot = lightbulb.Bot(
    prefix=lightbulb.when_mentioned_or(prefix),
    insensitive_commands=True,
    owner_ids=owners,
    intents=hikari.Intents.ALL,
    token=os.getenv("DISCORD_TOKEN"),
)


@bot.command()
async def ping(ctx: Context):
    """Shows the ping of the bot."""
    await ctx.respond(f"Pong! `{bot.heartbeat_latency * 1_000:.0f}ms`")


bot.load_extensions_from("./plugs")
# bot.load_extension("plugs.slashes")

bot.run(activity=hikari.Activity(name="with mud.", type=hikari.ActivityType.PLAYING))
