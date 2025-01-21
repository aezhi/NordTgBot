import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot(token='8077209075:AAFumjkYEHnp9rdxBXZSmbSRxD3ve2O-G_o')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('asda')


async def main():
    await dp.start_polling(bot)
    await bot.session.close()




if __name__ == '__main__':
    asyncio.run(main())
