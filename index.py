import telebot
from telebot import types
import random

token = "token"

bot = telebot.TeleBot(config.token)

with open("menu.txt") as menu:
	sort = [row.strip() for row in menu]

sotr_size = len(sort)

with open("price.txt") as price:
	sort_price = [row.strip() for row in price]

price_size = len(sort_price)

pokupka = [0, 1, 3, 4, 5]

@bot.message_handler(commands=['shop'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	for i in range(sotr_size):
		print(sort[i] + " " + sort_price[i])
		url_button1 = types.InlineKeyboardButton(text= sort[i] + " " + sort_price[i], callback_data=sort[i])
		markup.add(url_button1) #Имена кнопок

	msg = bot.reply_to(message, 'Выберите товар', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		for i in range(sotr_size):
			if call.data == sort[i]:
				markup = types.InlineKeyboardMarkup()
				call_massage = call.data
				pokupka[0] = call.data
				print(pokupka[0])

				url_button1 = types.InlineKeyboardButton(text="1кг", callback_data="1кг")
				url_button2 = types.InlineKeyboardButton(text="500г", callback_data="500г")
				url_button3 = types.InlineKeyboardButton(text="250г", callback_data="250г")
				markup.add(url_button1, url_button2, url_button3) #Имена кнопок

				msg = bot.send_message(call.message.chat.id, "Выберите фасовку", reply_markup=markup)

		if call.data == "1кг" or call.data == "500г" or call.data == "250г":
			markup = types.InlineKeyboardMarkup()
			call_massage = call.data
			pokupka[1] = call.data
			print(pokupka[1])

			url_button1 = types.InlineKeyboardButton(text="1", callback_data="1")
			url_button2 = types.InlineKeyboardButton(text="2", callback_data="2")
			url_button3 = types.InlineKeyboardButton(text="3", callback_data="3")
			markup.add(url_button1, url_button2, url_button3) #Имена кнопок
			
			bot.send_message(call.message.chat.id, "Выберите количество", reply_markup=markup)

		if call.data == "1" or call.data == "2" or call.data == "3":
			markup = types.InlineKeyboardMarkup()
			call_massage = call.data
			pokupka[2] = call.data
			print(pokupka[2])

			url_button1 = types.InlineKeyboardButton(text="Розовый", callback_data="Розовый")
			url_button2 = types.InlineKeyboardButton(text="Черный", callback_data="Черный")
			url_button3 = types.InlineKeyboardButton(text="Белый", callback_data="Белый")
			markup.add(url_button1, url_button2, url_button3) #Имена кнопок
			
			bot.send_message(call.message.chat.id, "Выберите вид упаковки", reply_markup=markup)

		if call.data == "Розовый" or call.data == "Черный" or call.data == "Белый":
			markup = types.InlineKeyboardMarkup()
			call_massage = call.data
			pokupka[3] = call.data
			print(pokupka[3])

			url_button1 = types.InlineKeyboardButton(text="Зерновой", callback_data="Зерновой")
			url_button2 = types.InlineKeyboardButton(text="Молотый", callback_data="Молотый")
			markup.add(url_button1, url_button2) #Имена кнопок
			
			bot.send_message(call.message.chat.id, "Выберите вид кофе", reply_markup=markup)

		if call.data == "Зерновой" or call.data == "Молотый":
			markup = types.InlineKeyboardMarkup()
			call_massage = call.data
			pokupka[4] = call.data
			print(pokupka[4])

			bot.send_message(call.message.chat.id, "Название кофе: " + pokupka[0] + "\n" "Фасовка: " + pokupka[1] + "\n" + "Количество: " + pokupka[2] + "\n" + "Упаковка: " + pokupka[3] + "\n" + "Вид кофе: " + pokupka[4])

if __name__ == '__main__':
	bot.polling(none_stop=True)