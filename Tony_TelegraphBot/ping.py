from pyrogram import Client as Tony_TelegraphBot, filters
import time

@Tony_TelegraphBot.on_message(filters.command('ping') & filters.private)
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"Pɪɴɢ: `{time_taken_s:.3f} ᴍꜱ`")
  
