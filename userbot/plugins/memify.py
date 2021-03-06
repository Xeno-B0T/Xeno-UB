import asyncio
import os

import cv2
from PIL import Image, ImageDraw, ImageFont

from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.helpers.convert import deEmojify

from . import *

path = "./legendmify/"
if not os.path.isdir(path):
    os.makedirs(path)

from userbot.Config import Config

lg_id = os.environ.get("LOGGER_ID", None)


@bot.on(admin_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def _(event):
    _reply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (_reply and (_reply.media)):
        legen_ = await eod(event, "`Can't memify this 🥴`")
        return
    legend = await _reply.download_media()
    if legend.endswith((".tgs")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        cmd = ["lottie_convert.py", legend, "pic.png"]
        file = "pic.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif legend.endswith((".webp", ".png")):
        legen_ = await eor(event, "**Memifying 🌚🌝**")
        pic = Image.open(legend)
        pic.save("pic.png", format="PNG", optimize=True)
        file = "pic.png"
    else:
        await eor(event, "**Memifying 🌚🌝**")
        img = cv2.VideoCapture(legend)
        tal, semx = img.read()
        cv2.imwrite("pic.png", semx)
        file = "pic.png"
    output = await draw_meme(file, msg)
    await bot.send_file(
        event.chat_id, output, force_document=False, reply_to=event.reply_to_msg_id
    )
    await legen_.delete()
    try:
        os.remove(legend)
        os.remove(file)
    except BaseException:
        pass
    os.remove(pic)


@bot.on(admin_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(event):
    legend = event.pattern_match.group(1)
    if not legend:
        if event.is_reply:
            (await event.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(event, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(event, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(legend))}")
    if troll:
        await event.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                event.chat_id,
                legen_,
                caption="",
            )
        await legen_.delete()
    else:
        await eod(event, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="gg(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gg(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    legend = kraken.pattern_match.group(1)
    if not legend:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Googlax need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(legend))}")
    if troll:
        await kraken.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                kraken.chat_id,
                legen_,
                caption="",
            )
        await kraken.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="honk(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="honk(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    legend = kraken.pattern_match.group(1)
    if not legend:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Honka need some text to make sticker.")

    troll = await bot.inline_query("honka_says_bot", f"{(deEmojify(legend))}.")
    if troll:
        await kraken.delete()
        legen_ = await troll[0].click(Config.LOGGER_ID)
        if legen_:
            await bot.send_file(
                kraken.chat_id,
                legen_,
                caption="",
            )
        await legen_.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


@bot.on(admin_cmd(pattern="gogl(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gogl(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    hell = kraken.pattern_match.group(1)
    if not hell:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Need some text...")

    troll = await bot.inline_query("stickerizerbot", f"#12{(deEmojify(hell))}")
    if troll:
        await kraken.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                kraken.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


client = borg


@bot.on(admin_cmd(pattern="(memify|mmf) ?(.*)"))
@bot.on(sudo_cmd(pattern="(memify|mmf) ?(.*)", allow_sudo=True))
async def handler(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "You might want to try `.help memify`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "```Reply to a image/sticker.```")
        return
    file = await client.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    await edit_or_reply(event, "```Memifying this image! (」ﾟﾛﾟ)｣ ```")
    text = str(event.pattern_match.group(1)).strip()
    if len(text) < 1:
        return await edit_or_reply(event, "You might want to try `.help memify`")
    meme = await drawText(file, text)
    await client.send_file(event.chat_id, file=meme, force_document=False)
    os.remove(meme)


async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if "," in text:
        upper_text, lower_text = text.split(",")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, "webp")
    return webp_file


CmdHelp("memify").add_command(
    "mmf",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in sticker format.",
    "mmf <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "memify",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in sticker format.",
    "mmf <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "mms",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in image format.",
    "mms <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "doge", "<text>", "Makes A Sticker of Doge with given text.", "doge Hello"
).add_command(
    "gogl", "<text>", "Makes Sticker"
).add_command(
    "gg", "<text>", "Makes google search sticker.", "gg Hello"
).add_command(
    "honk", "<text>", "Makes a sticker with honka revealing given text.", "honk Hello"
).add_info(
    "Make Memes on telegram 😉"
).add_warning(
    "✅ Harmless Module."
).add_type(
    "Addons"
).add()
