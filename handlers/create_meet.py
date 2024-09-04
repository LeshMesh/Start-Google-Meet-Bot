from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from quickstart import start_google_meet

router = Router()


@router.message(Command("meet"))
async def create_meet(message: Message, command: CommandObject):
    if command.args is None:
        url_meet = start_google_meet()
        await message.answer(
            f"Готово: {url_meet}"
        )
        return
    try:
        title, list_user = command.args.split("@", maxsplit=1)
    except ValueError:
        await message.answer(
            "Ошибка..."
        )
        return
    url_meet = start_google_meet()
    await message.answer(
        f"{title if title != '' else 'Готово'}: {url_meet}"
        f"\n@{' '.join(list_user.split(' '))}"
    )

# TODO Добавить возможность планирования встреч
