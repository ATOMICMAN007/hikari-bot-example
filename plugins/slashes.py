import hikari
import lightbulb
from lightbulb.slash_commands import SlashCommand


class Slashes(lightbulb.Plugin):
    @lightbulb.command()
    async def test(self, ctx):
        """A test command which sends a messages when triggered."""
        await ctx.respond("This is a test cmd.")


class Slashy(SlashCommand):
    name = "test"
    description = "This is a test command."

    async def callback(self, ctx):
        await ctx.respond("Sup, This is a test command.")


def load(bot: lightbulb.Bot):
    bot.add_plugin(Slashes())
    bot.add_slash_command(Slashy)


def unload(bot: lightbulb.Bot):
    bot.remove_plugin("Slashes")
    # The slash command name has to be passed in here, not class name.
    bot.remove_slash_command("test")
