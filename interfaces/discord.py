import asyncio
from typing import List

import interactions

from classes import Result
from modules import get_threads
from utils.query import exception_pattern
from utils.thread import on_thread
from utils.discord import to_embed

from utils.config import config

CHANNEL = int(config['discord']['channel'])
TOKEN = config['discord']['token']
GUILD_ID = config['discord']['guild_id'].strip()


async def send_discord(result: Result, channel: interactions.Channel):
    try:
        await channel.send(embeds=[to_embed(result)])
    except Exception as ex:
        print(f"{ex}")


async def on_result(results: List[Result], channel=None):
    send_threads = [send_discord(result, channel) for result in results]
    await asyncio.gather(*send_threads)


def run_discord():
    print("Starting discord bot")
    bot = interactions.Client(token=TOKEN)

    async def search(ctx: interactions.CommandContext, query: str):
        await ctx.send("ok", ephemeral=True)
        guild = await ctx.get_guild()
        channels = await guild.get_all_channels()
        channel = next(x for x in channels if x.id == CHANNEL)
        await channel.purge(amount=200)
        show_errors = bool(exception_pattern.search(" " + query + " "))
        await asyncio.gather(*on_thread(get_threads(query), on_result, add_exceptions=show_errors, channel=channel),
                             return_exceptions=True)

    @bot.command(name="search", description="Search", scope=[GUILD_ID], options=[
        interactions.Option(name="query", description="Query", required=True, type=interactions.OptionType.STRING)])
    async def _search(ctx: interactions.CommandContext, query: str):
        await search(ctx, query)

    @bot.command(name="s", description="Search", scope=[GUILD_ID], options=[
        interactions.Option(name="query", description="Query", required=True, type=interactions.OptionType.STRING)])
    async def _s(ctx: interactions.CommandContext, query: str):
        await search(ctx, query)

    bot.start()
