from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (tod1, tod2, tod3, tod4,
                tod5, tod6, tod7, tod8,
                tod9, tod10, tod11, tod12,
                tod13, tod14, tod15, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

tod = ALIVE_PIC or "https://telegra.ph/file/ca2001c80c6a2638e21f7.png"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if tod1:
            ids += 1
        if tod2:
            ids += 1
        if tod3:
            ids += 1
        if tod4:
            ids += 1
        if tod5:
            ids += 1
        if tod6:
            ids += 1
        if tod7:
            ids += 1
        if tod8:
            ids += 1
        if tod9:
            ids += 1
        if tod10:
            ids += 1
        if tod11:
            ids += 1
        if tod12:
            ids += 1
        if tod13:
            ids += 1
        if tod14:
            ids += 1
        if tod15:
            ids += 1
        tod_msg = f"Geez|RAM online. \n\n"
        tod_msg += f"===================\n"
        tod_msg += f"► Bot Version : `{__version__}` \n"
        tod_msg += f"► Pyrogram Version : `{pyro_vr}` \n"
        tod_msg += f"► Active ID : `{ids}` \n"
        tod_msg += f"===================\n\n"
        await e.reply_photo(
        photo=tod,
        caption=tod_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• GEEZ Support •", url="https://t.me/GeezSupport")
                ], [
                    InlineKeyboardButton(
                        "• RAM Support •", url="https://t.me/ramsupportt")
                ]],
        ),
    ) 
    except Exception as lol:         
        tod_msg = f"Geez|RAM online. \n\n"
        tod_msg += f"===================\n"
        tod_msg += f"► Bot Version : `{__version__}` \n"
        tod_msg += f"► Pyrogram Version : `{pyro_vr}` \n"
        tod_msg += f"===================\n\n"
        await e.reply_photo(
        photo=tod,
        caption=tod_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• GEEZ Support •", url="https://t.me/GeezSupport"),
                ],
                [
                    InlineKeyboardButton("• RAM Support •", url="https://t.me/ramsupportt"),
                ],
            ],
        ),
    ) 
