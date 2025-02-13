import asyncio

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from config import config

user_router = Router()


@user_router.message(Command('report'))
async def report_message(message: Message):
    if not message.reply_to_message:
        sent_message = await message.reply('⚠️ Вы должны ответить на сообщение, чтобы пожаловаться!')

        await asyncio.sleep(10)
        await sent_message.delete()
        return

    reported_user = message.reply_to_message.from_user
    reporter = message.from_user

    reported_user_name = f'@{reported_user.username}' if reported_user.username else f'<b>{reported_user.full_name}</b>'
    reporter_name = f'@{reporter.username}' if reporter.username else f'<b>{reporter.full_name}</b>'

    report_text = (
        f'🚨 <b>Жалоба на сообщение</b>\n'
        f'👤 <b>Отправитель:</b> {reported_user_name} (ID: {reported_user.id})\n'
        f'📩 <b>Текст:</b> {message.reply_to_message.text}\n'
        f'🆔 <b>Жалобу подал:</b> {reporter_name} (ID: {reporter.id})'
    )

    await message.bot.send_message(config.ADMIN_GROUP_ID, report_text)
    await message.reply('✅ Ваша жалоба была отправлена администраторам.')


@user_router.message(Command('rules'))
async def send_rules(message: Message):
    rules_text = (
        '📜 *Правила Telegram-канала*\n\n'
        '🚫 *Запрещено:*\n\n'
        '🔹 *Спам и флуд* – многократные повторяющиеся сообщения, '
        'чрезмерное количество стикеров, голосовых или медиафайлов.\n\n'
        '🔹 *Реклама и ссылки* на другие Telegram-каналы и чаты без одобрения администрации.\n\n'
        '🔹 *Попрошайничество, вымогательство, мошенничество* в любой форме.\n\n'
        '🔹 *Оскорбления, угрозы, шантаж* – личные нападки, разжигание конфликтов, '
        'а также упоминание родственников участников в негативном ключе.\n\n'
        '🔹 *NSFW-контент* – сцены насилия, шок-контент, материалы непристойного характера.\n\n'
        '🔹 */report abuse* – использование команды /report не по назначению/злоупотребелние командой.'
    )

    sent_message = await message.reply(rules_text, parse_mode='Markdown')

    await asyncio.sleep(30)
    await sent_message.delete()
    await message.delete()


@user_router.message(Command('help'))
async def send_help(message: Message):
    help_text = (
        '👋 Добро пожаловать в чат канала *NORD | Modern War | Arma 3*!\n\n'
        '❓ *Справка по командам*\n\n'
        '🔹 */rules* – 📜 Показывает правила чата. Ознакомьтесь с ними, чтобы избежать нарушений.\n\n'
        '🔹 */report* – 🚨 Отправляет жалобу на сообщение. Используйте эту команду, ответив на сообщение, '
        'которое нарушает правила. Администрация рассмотрит вашу жалобу.\n\n'
        '📌 Если у вас есть вопросы или предложения, свяжитесь с администрацией.'
    )

    sent_message = await message.reply(help_text, parse_mode='Markdown')

    await asyncio.sleep(20)
    await sent_message.delete()
    await message.delete()


@user_router.message()
async def echo_handler(message: Message):
   pass
