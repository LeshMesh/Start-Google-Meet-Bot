from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import create_meet

router = Router()


@router.message(Command("start"))
async def start_bot(message: Message):
    await message.answer(
        "Привет! Я создаю конференции в Google Meet."
        "\nВыберите действие ниже или отправьте мне команду '/meet'.",
        reply_markup=create_meet()
    )