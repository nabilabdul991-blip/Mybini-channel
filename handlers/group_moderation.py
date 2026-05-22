import re
from aiogram import Router, types
from aiogram.filters import ChatMemberUpdatedFilter

router = Router()

BAD_PATTERNS = [
    r"(t\.me|telegram\.me|wa\.me|whatsapp\.com)",
    r"(judol|slot|casino|qq|pkv|bola88|macau|hongkong)",
    r"(porn|bokep|sex|onlyfans|colmek|ngentot)",
    r"(promosi|jual|bisnis|modal|cuanharian)"
]

async def is_bad_link(text: str) -> bool:
    if not text:
        return False
    text_lower = text.lower()
    return any(re.search(pattern, text_lower) for pattern in BAD_PATTERNS)

@router.message()
async def moderation_handler(message: types.Message):
    if message.text and await is_bad_link(message.text):
        try:
            await message.delete()
            await message.answer("🚫 Link promosi / bokep / judol terdeteksi dan dihapus.", delete_after=10)
        except:
            pass
