from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from config import config

user_router = Router()


@user_router.message(Command("report"))
async def report_message(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Вы должны ответить на сообщение, чтобы пожаловаться!")

    reported_user = message.reply_to_message.from_user
    reporter = message.from_user

    reported_user_name = f"@{reported_user.username}" if reported_user.username else f"<b>{reported_user.full_name}</b>"
    reporter_name = f"@{reporter.username}" if reporter.username else f"<b>{reporter.full_name}</b>"

    report_text = (
        f"🚨 <b>Жалоба на сообщение</b>\n"
        f"👤 <b>Отправитель:</b> {reported_user_name} (ID: {reported_user.id})\n"
        f"📩 <b>Текст:</b> {message.reply_to_message.text}\n"
        f"🆔 <b>Жалобу подал:</b> {reporter_name} (ID: {reporter.id})"
    )

    await message.bot.send_message(config.ADMIN_GROUP_ID, report_text)
    await message.reply("✅ Ваша жалоба была отправлена администраторам.")


@user_router.message(Command("help"))
async def send_help(message: Message):
    rules_text = (
        "📜 <b>Правила чата:</b>\n"
        "1️⃣ Соблюдайте уважительный тон.\n"
        "2️⃣ Запрещены оскорбления, спам и реклама.\n"
        "3️⃣ Соблюдайте законы и правила Telegram.\n"
        "4️⃣ Если возникли проблемы, используйте /report."
    )

    await message.reply(rules_text)


@user_router.message()
async def echo_handler(message: Message) -> None:
    await message.answer(f"Echo: {message.from_user.id}")
