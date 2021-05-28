"""
Service that fetches Crypt of the NecroDancer daily run scores, and broadcasts them to the chat.

Data is fetched from the `Toofz API`_, which in turn fetches it from the Steam leaderboard using `SteamKit`_.

.. _Toofz API: https://api.toofz.com/help
.. _SteamKit: https://github.com/SteamRE/SteamKit
"""

import royalnet.royaltyping as t
import aiohttp
import asyncio
import datetime


async def get_leaderboards_info() -> list[t.JSON]:
    """
    :return: A list of all available leaderboards.
    """

    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.toofz.com/leaderboards/dailies") as request:
            data = await request.json()
            return data["leaderboards"]


async def get_latest_leaderboard_info() -> dict[str, t.JSON]:
    """
    :return: List data about the latest leaderboard.
    """

    leaderboards = await get_leaderboards_info()
    latest = leaderboards[0]
    assert latest["production"] is True
    assert latest["product"] == "amplified"
    assert datetime.datetime.fromtimestamp(latest["date"]).date() == datetime.date.today()
    assert latest["total"] > 0
    return latest


async def get_all_leaderboard_entries(lbid):
    """
    :param lbid: The leaderboard id to retrieve entries of.
    :return: All entries from the daily leaderboard with the specific lbid.
    """

    total = None
    offset = 0
    result = []

    while total is None or offset < total:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.toofz.com/leaderboards/dailies/{lbid}/entries?offset={offset}&limit=100") as request:
                print(f"{total=} {offset=} {result=}")
                data = await request.json()
                assert data["leaderboard"]["id"] == lbid
                if total is None:
                    total = data["total"]
                assert data["total"] == total
                offset += len(data["entries"])
                result = [*result, *data["entries"]]
                await asyncio.sleep(1)

    return result
