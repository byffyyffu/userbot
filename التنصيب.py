from userbot.utils import admin_cmd


@borg.on(admin_cmd("التنصيب"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "⌯︙**مـرحبا بـك عزيـزي** \n⌯︙رابط التنصيب - [اضغط هنا](https://heroku.com/deploy?template=https://github.com/SelVa12345/Assistant)\n⌯︙قناة السورس -https://t.me/EITHON"
        )
