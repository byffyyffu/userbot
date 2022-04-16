# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/JM-THON >
# Please read the GNU Affero General Public License in;
# < https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# ===============================================================

import random
from Jmthon.razan.resources.strings import *
from userbot import EITHON, CMD_HELP
from userbot import EITHON
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event


@EITHON.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بڪلبك 🖤 "
    )


@EITHON.on(admin_cmd(pattern="رفع زوجي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجج روحوا خلفوا 🤤😂",
    )


@EITHON.on(admin_cmd(pattern="رفع مطي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1939538780:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 2042690935:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5048122708:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه مطي هـنا "
    )


@EITHON.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 2042690935:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5048122708:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 1939538780:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
    )


@EITHON.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1939538780:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 2042690935:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5048122708:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه جلب خليه خله ينبح 😂🐶",
    )


@EITHON.on(admin_cmd(pattern="كت(?: |$)(.*)"))
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@EITHON.on(admin_cmd(pattern="هينه(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5048122708:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 2042690935:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@EITHON.on(admin_cmd(pattern="نسبة الحب(?: |$)(.*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@EITHON.on(admin_cmd(pattern="نسبة الانوثة(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5048122708:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 2042690935:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 2034443585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@EITHON.on(admin_cmd(pattern="نسبة الغباء(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@EITHON.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥"
    )


@EITHON.on(admin_cmd(pattern="رفع قرد(?: |$)(.*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5138443589:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 5133858592:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 885018394:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == :
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@EITHON.on(admin_cmd(pattern="اوصف(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")

@EITHON.on(admin_cmd(pattern="شغله(?: |$)(.*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )
