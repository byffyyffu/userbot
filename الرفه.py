import random
from Jmthon.razan.resources.strings import *
from userbot import jmthon, CMD_HELP
from userbot import jmthon
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

@EITHON.on(admin_cmd(pattern="نسبة الرجولة(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5133858592:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5096922805:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5138443589:
        return await edit_or_reply(mention, f"**100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )

@EITHON.on(admin_cmd(pattern="رفع حيوان(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه حيوان 🐏"
    )

@EITHON.on(admin_cmd(pattern="رفع بزون(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بزون 🐈"
    )

@EITHON.on(admin_cmd(pattern="رفع زاحف(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞"
    )

