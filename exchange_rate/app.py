import telebot
from extensions import CurrencyConverter, ConvertionException
from config import TOKEN, keys_

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты>' \
           '<в какую валюту перевести>' \
           '<количество переводимой валюты>\nУвидеть список всех доступных валют--> /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys_.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        values_ = message.text.split()

        if len(values_) != 3:
            raise ConvertionException(f'Не правильный ввод параметров, для помощи нажмите --> /help')

        quote, base, amount = values_

        total_base = CurrencyConverter.converter(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:
        text = f'Цена {amount} {quote} в {base} - {total_base * int(amount)}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
