from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

#token bot
BOT_TOKEN = '6911865322:AAGlbTc2ruf1brgs7i-I8YmHJSmkfyRfBNE'

#объекты бота и диспетчера
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

#/start
@dp.message(Command(commands = ['start']))
async def proccess_start_command(message: Message):
	data = message
	await message.answer(data.model_dump_json(indent = 4, exclude_none = True))
	await message.answer('Привет!\nМеня зовут СорокАБот!\nНапиши мне что-нибудь.')

#/help
@dp.message(Command(commands = ['help']))
async def proccess_help_command(message: Message):
	await message.answer('Напиши мне что-нибудь и в ответ\nя пришлю тебе твое сообщение')

#any msg
@dp.message()
async def send_echo(message: Message):
	try:
		await message.send_copy(chat_id = message.chat.id)
	except TypeError:
		await message.reply(text = 'С этим я еще не работал.')
	print(message.model_dump_json(indent = 4, exclude_none = True))

#Строка для вывода апдейта в формате JSON (добавлять в тело функции)
#print(message.model_dump_json(indent = 4, exclude_none = True))



#pool
if __name__ == '__main__':
	dp.run_polling(bot)