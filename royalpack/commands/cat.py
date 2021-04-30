import io
import logging

import aiohttp
import royalnet.engineer as engi
import royalpack.bolts as rb

log = logging.getLogger(__name__)


@rb.capture_errors
@engi.TeleportingConversation
async def cat(*, _msg: engi.Message, **__):
    """
    Invia un gatto in chat! 🐈
    """

    log.debug("Creating a new HTTP session")
    async with aiohttp.ClientSession() as session:

        log.info("Making a GET request to The Cat API Image Search")
        async with session.get("https://api.thecatapi.com/v1/images/search") as response:

            log.debug("Ensuring the request was successful")
            if response.status >= 400:
                log.error(f"The Cat API returned an HTTP error: {response.status}")
                await _msg.reply(
                    text="⚠️ Couldn't request a cat from https://thecatapi.com :("
                )
                return

            log.debug("Reading the JSON received from The Cat API")
            try:
                result = await response.json()
            except aiohttp.ContentTypeError:
                log.error(f"Couldn't decode received JSON from The Cat API")
                await _msg.reply(
                    text="⚠️ Couldn't understand what the cat from https://thecatapi.com was saying :("
                )
                return

        # Example result:
        # [
        #     {
        #         "breeds": [],
        #         "id": "MjAzMjY3MQ",
        #         "url": "https://cdn2.thecatapi.com/images/MjAzMjY3MQ.jpg",
        #         "width": 557,
        #         "height": 724
        #     }
        # ]

        log.debug("Ensuring at least one image was received")
        if len(result) == 0:
            log.error("Didn't receive any image from The Cat API")
            await _msg.reply(
                text="⚠️ I couldn't find any cats at https://thecatapi.com :("
            )
            return

        # Select the first image received
        selected_cat = result[0]
        log.debug(f"Selected {selected_cat!r}")

        log.debug("Ensuring an image url is available")
        if "url" not in selected_cat:
            log.error("Image received from The Cat API did not have any URL")
            await _msg.reply(
                text="⚠️ I found a cat at https://thecatapi.com, but I couldn't find its image :("
            )
            return

        # Download the cat image
        log.info("Making a GET request to retrieve a The Cat API image")
        async with session.get(selected_cat["url"]) as response:

            log.debug("Reading image bytes into memory")
            img = io.BytesIO()
            while img_data := await response.content.read(8192):
                img.write(img_data)
            img.seek(0)

    log.debug("Sending image in the chat")
    await _msg.reply(files=[img])


# Objects exported by this module
__all__ = (
    "cat",
)
