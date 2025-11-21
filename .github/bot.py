from telethon import TelegramClient
import asyncio
from telethon.sessions import StringSession
from telethon.tl.types import InputReplyToMessage
import os
import sys

API_ID = 611335
API_HASH = "d524b414d21f4d37f08684c1df41ac9c"

BETTER_NET = os.environ.get("BETTER_NET")
REKERNEL = os.environ.get("REKERNEL")
KERNEL = os.environ.get("KERNEL")
KERNELSU = os.environ.get("KERNELSU")
BBG = os.environ.get("BBG")
LXC = os.environ.get("LXC")
SUSFS = os.environ.get("SUSFS")
HOOKS = os.environ.get("HOOKS")
KERNEL = os.environ.get("KERNEL")
ZRAM = os.environ.get("ZRAM")
SSG = os.environ.get("SSG")
STOCK_CONFIG = os.environ.get("STOCK_CONFIG")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))
RUN_URL = os.environ.get("RUN_URL")
BOT_CI_SESSION = os.environ.get("BOT_CI_SESSION")
MSG_TEMPLATE = """
```
kernel source: {kernel}
root impl: {kernelsu}
ssg io: {ssg}
stock config: {stock_config}
rekernel status: {rekernel}
lxc support status: {lxc}
BBG: {bbg}
better_net status: {better_net}
susfs status: {susfs}
hook type: {hooks}
more ZRAM: {zram}
```
[Workflow run]({run_url})
""".strip()


def get_caption():
    msg = MSG_TEMPLATE.format(
        kernel=KERNEL,
        kernelsu=KERNELSU,
        ssg=SSG,
        stock_config=STOCK_CONFIG,
        rekernel=REKERNEL,
        lxc=LXC,
        bbg=BBG,
        better_net=BETTER_NET,
        susfs=SUSFS,
        hooks=HOOKS,
        zram=ZRAM,
        run_url=RUN_URL,
    )
    return msg


async def send_telegram_message(file_path: str):
    async with TelegramClient(StringSession(BOT_CI_SESSION), api_id=API_ID, api_hash=API_HASH) as client:
        await client.start(bot_token=BOT_TOKEN)
        print("[+] Caption: ")
        print("---")
        print("---")
        print("[+] Sending")
        await client.send_file(
            entity=CHAT_ID,
            file=file_path,
            parse_mode="markdown",
            caption=get_caption(),
            reply_to=29147
        )

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python send_kernel.py <file_to_upload>")
        sys.exit(1)

    file_to_upload = sys.argv[1]
    if not os.path.isfile(file_to_upload):
        print(f"Error: {file_to_upload} does not exist!")
        sys.exit(1)

    asyncio.run(send_telegram_message(file_to_upload))
