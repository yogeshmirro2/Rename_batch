from bot.client import Client
from pyrogram import filters
from pyrogram import types
from configs import Config

@Client.on_message(filters.command("from_channel") & filters.private & ~filters.edited)
async def from_channel(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any channel id to change or add as FROM_CHANNEL\nlike --- 10025648893")
    try:
        Config.FROM_CHANNEL = int(m.reply_to_message.text)
        await m.reply_text("ok i will use this channel as FROM_CHANNEL")
    except ValueError:
        await m.reply_text("don't send me string only send channel id in intiger")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong")


@Client.on_message(filters.command("to_channel") & filters.private & ~filters.edited)
async def to_channel(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any channel id to change or add as TO_CHANNEL\nlike --- 10025648893")
    try:
        Config.TO_CHANNEL = int(m.reply_to_message.text)
        await m.reply_text("ok i will use this channel as TO_CHANNEL")
    except ValueError:
        await m.reply_text("don't send me string only send channel id in intiger")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong")


@Client.on_message(filters.command("log_channel") & filters.private & ~filters.edited)
async def log_channel(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any channel id to change or add as LOG_CHANNEL\nlike --- 10025648893")
    try:
        Config.LOG_CHANNEL = int(m.reply_to_message.text)
        await m.reply_text("ok i will use this channel as LOG_CHANNEL")
    except ValueError:
        await m.reply_text("don't send me string only send channel id in intiger")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong")

@Client.on_message(filters.command("start_from") & filters.private & ~filters.edited)
async def start_from(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nthis cmd only use for batch rename\nreply to any number to change or add as START_FROM\nlike --- 100")
    try:
        Config.START_FROM = int(m.reply_to_message.text)
        await m.reply_text("ok i will use this number as START_FROM")
    except ValueError:
        await m.reply_text("don't send me string only send number in intiger")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong")

@Client.on_message(filters.command("buttom_height_crop") & filters.private & ~filters.edited)
async def buttom_height_crop(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any number to change or add as BUTTOM_HEIGHT_CROP\nlike --- 35")
    try:
        Config.BUTTOM_HEIGHT_CROP = int(m.reply_to_message.text)
        await m.reply_text("ok i will use this number as BUTTOM_HEIGHT_CROP")
    except ValueError:
        await m.reply_text("don't send me string only send number in intiger")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong")


@Client.on_message(filters.command("remove_word") & filters.private & ~filters.edited)
async def remove_word(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any text to change or add as REMOVE_WORD\nmultiple remove words must be separted by '|'\nlike --- Abcd|rtgsj|jekrk")
    try:
        Config.REMOVE_WORD = str(m.reply_to_message.text)
        await m.reply_text("ok i will use this text as REMOVE_WORD")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong plz check log")

@Client.on_message(filters.command("remove_caption") & filters.private & ~filters.edited)
async def remove_caption(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    
    if not m.reply_to_message:
        return await m.reply_text("this cmd only use for batch rename\nreply to any text to change or add as REMOVE_CAPTION\nmultiple remove words must be separted by '|'\nlike --- Abcd|rtgsj|jekrk")
    try:
        Config.REMOVE_CAPTION = str(m.reply_to_message.text)
        await m.reply_text("ok i will use this text as REMOVE_WORD")
    except Exception as e:
        print(str(type(e)))
        await m.reply_text("something went wrong plz check log")
