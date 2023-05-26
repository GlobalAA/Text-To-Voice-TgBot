from aiogram import types
from dispatcher import dp, bot
from config import users_date

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('Language'))
async def change_lang(callback_query: types.CallbackQuery):
	language = callback_query.data[-2::]
	for i in users_date:
		if i["user_name"] == callback_query.from_user.username:
			i["language"] = language
			return await bot.answer_callback_query(
				callback_query.id, text='Language changed successful!', show_alert=True)

	date = {"user_name": callback_query.from_user.username, "language": language}
	users_date.append(date)
	return await bot.answer_callback_query(
		callback_query.id, text='Language changed successful!', show_alert=True)