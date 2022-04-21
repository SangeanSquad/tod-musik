from pyrogram import filters
from pyrogram.types import Message

from .. import (tod1, tod2, tod3, tod4,
                    tod5, tod6, tod7, tod8,
                    tod9, tod10, tod11, tod12,
                    tod13, tod14, tod15, HNDLR,
                    SUDO_USERS, vcbot)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message):
    inp = e.text[6:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or invite link to join.")
    if inp.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        if tod1:
            await tod1.join_chat(inp)
            count += 1
        if tod2:
            await tod2.join_chat(inp)
            count += 1
        if tod3:
            await tod3.join_chat(inp)
            count += 1
        if tod4:
            await tod4.join_chat(inp)
            count += 1
        if tod5:
            await tod5.join_chat(inp)
            count += 1
        if tod6:
            await tod6.join_chat(inp)
            count += 1
        if tod7:
            await tod7.join_chat(inp)
            count += 1
        if tod8:
            await tod8.join_chat(inp)
            count += 1
        if tod9:
            await tod9.join_chat(inp)
            count += 1
        if tod10:
            await tod10.join_chat(inp)
            count += 1
        if tod11:
            await tod11.join_chat(inp)
            count += 1
        if tod12:
            await tod12.join_chat(inp)
            count += 1
        if tod13:
            await tod13.join_chat(inp)
            count += 1
        if tod14:
            await tod14.join_chat(inp)
            count += 1
        if tod15:
            await tod15.join_chat(inp)
            count += 1
        await e.reply_text(f"**Joined Successfully ✅** \n\n __IDs__: `{count}` \n __Group__: `{inp}`")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    inp = e.text[7:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or chat id to leave.")
    try:
        if tod1:
            await tod1.leave_chat(inp)
            count += 1
        if tod2:
            await tod2.leave_chat(inp)
            count += 1
        if tod3:
            await tod3.leave_chat(inp)
            count += 1
        if tod4:
            await tod4.leave_chat(inp)
            count += 1
        if tod5:
            await tod5.leave_chat(inp)
            count += 1
        if tod6:
            await tod6.leave_chat(inp)
            count += 1
        if tod7:
            await tod7.leave_chat(inp)
            count += 1
        if tod8:
            await tod8.leave_chat(inp)
            count += 1
        if tod9:
            await tod9.leave_chat(inp)
            count += 1
        if tod10:
            await tod10.leave_chat(inp)
            count += 1
        if tod11:
            await tod11.leave_chat(inp)
            count += 1
        if tod12:
            await tod12.leave_chat(inp)
            count += 1
        if tod13:
            await tod13.leave_chat(inp)
            count += 1
        if tod14:
            await tod14.leave_chat(inp)
            count += 1
        if tod15:
            await tod15.leave_chat(inp)
            count += 1
        await e.reply_text(f"**Left Successfully ✅** \n\n __IDs__: `{count}` \n __Group__: `{inp}`")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
