import asyncio
from collections import deque

from . import *


@bot.on(admin_cmd(pattern=r"^π€¬", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^π€¬", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "πΈ ππ πππππ’ ")
    deq = deque(list("π‘π₯π€¬π₯π‘π₯π€¬π₯π‘π₯"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


import asyncio
from collections import deque

from . import *


@bot.on(admin_cmd(pattern=r"^π€£", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^π€£", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Lots Of Laugh")
    deq = deque(list("ππ€£ππ€£ππ€£"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"^β", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^β", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Confusion")
    deq = deque(list("ββββββββ"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


CmdHelp("angry").add_command(
    "π€¬", None, "ΟΡΡ it also it describes all about ur felling that u r angry - π€¬"
).add_command("π€£", None, "funny command use it and see it").add_command(
    "β", None, "Confusion Use and See But Without dot(.)"
).add_type(
    "Official"
).add_info(
    "Its Very Useful Module this module explains all about your fellings like (π€¬) for ur angry(π€£)friends message is funny "
).add_warning(
    "Harmless Moduleβ"
).add_type(
    "Addons"
).add()
