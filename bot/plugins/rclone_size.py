#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52 | 5MysterySD
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

from asyncio import sleep as asleep, create_subprocess_exec, subprocess
from os import path as opath
from re import findall

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import DESTINATION_FOLDER, LOGGER, UPDATES_CHANNEL 
from bot.plugins import getUserOrChaDetails

async def check_size_g(client, message):
    user_id, u_men = getUserOrChaDetails(message)
    del_it = await message.reply_text("`๐พ Checking Cloud Size... Please Wait !!!`")
    if opath.exists("rclone.conf"):
        with open("rclone.conf", "r+") as file:
            con = file.read()
            gUP = findall(r"\[(.*)\]", con)[0]
    cmd = ["rclone", "size", "--config=./rclone.conf", f"{gUP}:{DESTINATION_FOLDER}"]
    gau_tam = await create_subprocess_exec(
        *cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    gau, tam = await gau_tam.communicate()
    gautam = (gau.decode("utf-8")).replace("Total objects:", "โฃ๐ **Total Files** :").replace("Total size:", "โฃ๐ **Total Size** :")
    await asleep(5)
    await message.reply_text(f"โโโโโ โ __GDriveInfo__ โ โโโโโโโป\nโ\nโฃ๐ค **User** : {u_men}\nโฃ๐ **User ID** : #ID{user_id}\nโฃ๐งพ **Folder Name** : `{DESTINATION_FOLDER}`\n{gautam}โ\nโโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL} โฆ๏ธโโน\n\n#CloudSize")
    await del_it.delete()

async def g_clearme(client, message):

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes ๐ซ", callback_data=("fuckingdo").encode("UTF-8")),
        InlineKeyboardButton("No ๐ค", callback_data=("fuckoff").encode("UTF-8"))]
    ])
    await message.reply_text(
        "Are you sure? ๐ซ This will delete all your downloads locally ๐ซ",
        reply_markup=reply_markup,
        quote=True,
    )
