from aiogram import Router, types
from aiogram.filters import Command
from services.email_sender import send_appeal_email
from services.rate_limiter import check_limit, add_usage

router = Router()

@router.message(Command("fix"))
async def fix_merah(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply("Format: `/fix 628xxxxxxxxxx`")
    
    phone = args[1].strip()
    
    can_use, remaining = await check_limit(message.from_user.id, phone)
    if not can_use:
        return await message.reply(f"❌ Limit habis. Sisa: {remaining}")
    
    status = await send_appeal_email(phone)
    if status:
        await add_usage(message.from_user.id, phone)
        await message.reply(f"✅ Appeal untuk {phone} telah dikirim ke WhatsApp.\nJeda 1 menit diterapkan.")
    else:
        await message.reply("❌ Gagal mengirim appeal.")
