#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
     await message.reply_text("🙏 Welcome...!", quote=True)
     channel_id = str(AUTH_CHANNEL)[4:]
     message_id = 99
     display the /help
    
    await message.reply_text("""<b>Need Any Help? Then Contact me</b>--𝙿𝚕𝚎𝚊𝚜𝚎 𝚁𝚎𝚊𝚍 𝙿𝚒𝚗𝚗𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎\n\n<b> and also Don't forget to Subscribe Our Channel</b>: <a href="https://t.me/">JOIN CHANNEL""", disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="🙏 Welcome...!",
            url="https://t.me/"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "🌀Thank you !",
        quote=True,
        reply_markup=reply_markup
    )
