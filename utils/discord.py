from classes.result import Result
from interactions import Embed


def to_embed(result: Result) -> Embed:
    embed = Embed()
    embed.title = result.title
    embed.description = result.summary
    if result.uri:
        embed.url = result.uri
    if result.footer:
        embed.set_footer(text=result.footer)
    if result.image:
        embed.set_thumbnail(url=result.image)
    for widget in result.widgets:
        widget.append_embed(embed)
    return embed
