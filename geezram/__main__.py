import asyncio

from pyrogram import idle

from . import (tod1, tod2, tod3, tod4, tod5, tod6, tod7, tod8, tod9, tod10, tod11, tod12, tod13, tod14, tod15, vcbot, hl)
               
from . import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8,
               call_py9, call_py10, call_py11, call_py12,
               call_py13, call_py14, call_py15)


async def startup():
    # STARTING CLIENTS
    if tod1:
        try:
            await tod1.start()
            await tod1.join_chat("GeezSupport")
            await tod1.join_chat("ramsupportt")
            await tod1.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod2:
        try:
            await tod2.start()
            await tod2.join_chat("GeezSupport")
            await tod2.join_chat("ramsupportt")
            await tod2.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod3:
        try:
            await tod3.start()
            await tod3.join_chat("GeezSupport")
            await tod3.join_chat("ramsupportt")
            await tod3.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod4:
        try:
            await tod4.start()
            await tod4.join_chat("GeezSupport")
            await tod4.join_chat("ramsupportt")
            await tod4.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod5:
        try:
            await tod5.start()
            await tod5.join_chat("GeezSupport")
            await tod5.join_chat("ramsupportt")
            await tod5.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod6:
        try:
            await tod6.start()
            await tod6.join_chat("GeezSupport")
            await tod6.join_chat("ramsupportt")
            await tod6.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod7:
        try:
            await tod7.start()
            await tod7.join_chat("GeezSupport")
            await tod7.join_chat("ramsupportt")
            await tod7.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod8:
        try:
            await tod8.start()
            await tod8.join_chat("GeezSupport")
            await tod8.join_chat("ramsupportt")
            await tod8.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod9:
        try:
            await tod9.start()
            await tod9.join_chat("GeezSupport")
            await tod9.join_chat("ramsupportt")
            await tod9.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod10:
        try:
            await tod10.start()
            await tod10.join_chat("GeezSupport")
            await tod10.join_chat("ramsupportt")
            await tod10.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod11:
        try:
            await tod11.start()
            await tod11.join_chat("GeezSupport")
            await tod11.join_chat("ramsupportt")
            await tod11.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod12:
        try:
            await tod12.start()
            await tod12.join_chat("GeezSupport")
            await tod12.join_chat("ramsupportt")
            await tod12.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod13:
        try:
            await tod13.start()
            await tod13.join_chat("GeezSupport")
            await tod13.join_chat("ramsupportt")
            await tod13.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod14:
        try:
            await tod14.start()
            await tod14.join_chat("GeezSupport")
            await tod14.join_chat("ramsupportt")
            await tod14.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))

    if tod15:
        try:
            await tod15.start()
            await tod15.join_chat("GeezSupport")
            await tod15.join_chat("ramsupportt")
            await tod15.join_chat("beritabaruu")
        except Exception as e:
            print(str(e))


    # STARTING BOT CLIENT
    await vcbot.start()
    get_me = await vcbot.get_me()
    usernamee = get_me.username
    await tod1.join_chat("ramsupportt")
    msg = f"**My Geez|RAM Deployed Successfully ✅ \n\n Bot Username :** @{usernamee} \n Hndlr : {hl}"
    await tod1.send_message(-1001692751821, text=msg)
    await tod1.leave_chat(-1001692751821)

    # STARTING ASSISTANTS
    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    
    # STARTUP COMPLETED
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
