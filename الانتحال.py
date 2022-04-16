# Copyright (C) 2021 EITHON TEAM
# t.me/EITHON
import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from ..Config import Config
from ..Config import Config
from . import (
    ALIVE_NAME,
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    edit_delete,
    get_user_from_event,
    EITHON,
)

DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = str(DEFAULT_BIO) if DEFAULT_BIO else "الـحمد لله عـلى كـل شـيء"

CLONE_CMD = Config.CLONE_CMD or "انتحال"
RETRUN_CMD = Config.RETRUN_CMD or "اعادة"

@EITHON.on(admin_cmd(pattern=f"{CLONE_CMD}(?:\s|$)([\s\S]*)"))
async def _(event):
    reply_EITHON, error_i_a = await get_user_from_event(event)
    if reply_EITHON is None:
        return
    user_id = reply_EITHON.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(reply_EITHON.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = reply_EITHON.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    reply_EITHON = await event.client(GetFullUserRequest(reply_EITHON.id))
    user_bio = reply_EITHON.about
    if user_bio is not None:
        user_bio = reply_EITHON.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    pfile = await event.client.upload_file(profile_pic)
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "- تـم نسـخ الـحساب بـنجاح  ✓")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#CLONED\nsuccessfully cloned [{first_name}](tg://user?id={user_id })",
        )


@EITHON.on(admin_cmd(pattern=f"{RETRUN_CMD}$"))
async def _(event):
    name = f"{DEFAULTUSER}"
    roz = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=roz))
    await edit_delete(event, "- تـم اعـادة الـحساب بـنجاح ✓")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"- تـم اعادة الـحساب الى وضـعه الاصلـي ✓"
        )
