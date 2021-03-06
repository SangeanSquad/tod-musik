import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v1.0"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
SESSION1 = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")
START_VID = os.getenv("START_VID", None)


def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list


sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
#delete this line 
DEVS = [ 5181183910, 1883494460, 1883494460, 1826643972, 5139656286]
for x in DEVS:
    SUDO_USERS.append(x)



#----------------------------------------------

vcbot = Client(
    'geezram',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'geezram.vc'},
)

HELP_DICT = dict()
hl = HNDLR[0]
start_time = time.time()


if GROUP_MODE == ("True" or "true" or "TRUE"):
    grp = True
else:
    grp = False


#-------------------------CLIENTS-----------------------------
if SESSION1:
    tod1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py1 = PyTgCalls(tod1)
else:
    tod1 = None
    call_py1 = None

if SESSION2:
    tod2 = Client(SESSION2, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py2 = PyTgCalls(tod2)
else:
    tod2 = None
    call_py2 = None

if SESSION3:
    tod3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py3 = PyTgCalls(tod3)
else:
    tod3 = None
    call_py3 = None

if SESSION4:
    tod4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py4 = PyTgCalls(tod4)
else:
    tod4 = None
    call_py4 = None

if SESSION5:
    tod5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py5 = PyTgCalls(tod5)
else:
    tod5 = None
    call_py5 = None

if SESSION6:
    tod6 = Client(SESSION6, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py6 = PyTgCalls(tod6)
else:
    tod6 = None
    call_py6 = None
        
if SESSION7:
    tod7 = Client(SESSION7, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py7 = PyTgCalls(tod7)
else:
    tod7 = None
    call_py7 = None

if SESSION8:
    tod8 = Client(SESSION8, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py8 = PyTgCalls(tod8)
else:
    tod8 = None
    call_py8 = None

if SESSION9:
    tod9 = Client(SESSION9, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py9 = PyTgCalls(tod9)
else:
    tod9 = None
    call_py9 = None
    
if SESSION10:
    tod10 = Client(SESSION10, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py10 = PyTgCalls(tod10)
else:
    tod10 = None
    call_py10 = None
           
if SESSION11:
    tod11 = Client(SESSION11, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py11 = PyTgCalls(tod11)
else:
    tod11 = None
    call_py11 = None

if SESSION12:
    tod12 = Client(SESSION12, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py12 = PyTgCalls(tod12)
else:
    tod12 = None
    call_py12 = None

if SESSION13:
    tod13 = Client(SESSION13, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py13 = PyTgCalls(tod13)
else:
    tod13 = None
    call_py13 = None

if SESSION14:
    tod14 = Client(SESSION14, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py14 = PyTgCalls(tod14)
else:
    tod14 = None
    call_py14 = None

if SESSION15:
    tod15 = Client(SESSION15, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'geezram.vc'})
    call_py15 = PyTgCalls(tod15)
else:
    tod15 = None
    call_py15 = None
#----------------------------------------------------------------

HELP_DICT["Music Player"] = f"""
**Basic music player commands!**

**Command:** `{hl}play`
**Usage:** __Plays the song in voice chat. Supports replied audio, Youtube link or just a keyword to search.__
**Example:** `{hl}play Closer`

**Command:** `{hl}end`
**Usage:** __Ends the music stream and leaves the voice chat.__

**Commad:** `{hl}pause`
**Usage:** __Pause the music stream in voice chat.__

**Commad:** `{hl}list`
**Usage:** __Shows the playlist in current chat.__

**Commad:** `{hl}resume`
**Usage:** __Resumes the paused stream in voice chat.__

**Commad:** `{hl}skip`
**Usage:** __Skips the current song playing in voice chat.__
"""

HELP_DICT["TOD"] = f"""
**Voice Chat RTOD Commands!**

**Commad:** `{hl}tod`
**Usage:** __start TOD the mentioned voice chat.__
**Example:**
    ~ `{hl}tod chat username/id` [If in bot PM.]
    ~ `{hl}tod` [If in a group.]

**Commad:** `{hl}vtod`
**Usage:** __start TOD With Video in the mentioned voice chat.__
**Example:**
    ~ `{hl}tod chat username/id` [If in bot PM.]
    ~ `{hl}vtod` [If in a group.]

**Commad:** `{hl}ptod`
**Usage:** __start TOD Porn in the mentioned voice chat.__
**Example:**
    ~ `{hl}ptod chat username/id` [If in bot PM.]
    ~ `{hl}ptod` [If in a group.]

**Explanation:**
    ??????First Join All Your Id's In The Group By {hl}join `@chatusername` if chat is private Then {hl}join `https://t.me/linkgrouphere` \n Then Do {hl}TOD In Groups 

**Commad:** `{hl}todend`
**Usage:** __Stop TOD and leaves voice chat.__

**Commad:** `{hl}todpause`
**Usage:** __Pauses the TOD.__

**Commad:** `{hl}todresume`
**Usage:** __Resumes the paused TOD.__
"""

HELP_DICT["Extras"] = f"""
**Some extra commands!**

**Commad:** `{hl}help`
**Usage:** __To see the help menu with all command details.__

**Commad:** `{hl}start`
**Usage:**  __To see the start message.__

**Command:** `{hl}join <username / invite link>`
**Usage:** __Joins the chat with all clients.__

**Command:** `{hl}leave <username> / <chat-id>`
**Usage:** __Leaves the chat with all clients.__
"""
