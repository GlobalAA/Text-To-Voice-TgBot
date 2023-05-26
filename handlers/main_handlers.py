from aiogram import types
from dispatcher import dp, bot
from gtts import gTTS
from uuid import uuid4
from os import remove
import config

@dp.message_handler(commands=["start", "help"])
async def help_message(message: types.Message):
	return await message.answer(config.HELP_MESSAGE)

@dp.message_handler(commands=["lang", "language"])
async def change_language_handler(message: types.Message):
	language_key_board = types.InlineKeyboardMarkup()
	language_list = ["🇺🇸 EN", "🇷🇺 RU"]
	en = types.InlineKeyboardButton(
		language_list[0], callback_data=f"Language-{language_list[0][-2:]}")
	ru = types.InlineKeyboardButton(
		language_list[1], callback_data=f"Language-{language_list[1][-2:]}")
	language_key_board.row(en, ru)

	await message.answer("Select language", reply_markup=language_key_board)

@dp.message_handler(commands="example")
async def on_example_handler(message: types.Message):
	paths = [
		{"lang": "🇺🇸 EN", "path": "audio/example/English.mp3"}, 
		{"lang": "🇷🇺 RU", "path": "audio/example/Russian.mp3"}
	]
	answer = ""
	for i in paths:
		await bot.send_audio(chat_id=message.chat.id, audio=open(i["path"], "rb"), title=i["lang"])

@dp.message_handler()
async def convert_handler(message: types.Message):
	text = message.text
	lang = config.DEFAULT_LANGUAGE
	if len(text.strip()) == 0:
		return message.answer("Sorry, this request have only spaces!")
	for i in config.users_date:
		if i["user_name"] == message.from_user.username:
			lang=i["language"]
			
	path = f"audio/{uuid4()}.mp3"
	sp = gTTS(text=text, lang=lang.lower(), slow=False)
	sp.save(path)

	await bot.send_audio(chat_id=message.chat.id, audio=open(path, "rb"), performer=f"{message.from_user.username}", title=f"{message.text[:5]}" )

	remove(path=path)