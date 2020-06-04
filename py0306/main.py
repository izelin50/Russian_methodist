import telebot;
from telebot import apihelper
bot = telebot.TeleBot('1120765994:AAE6P-3QH4I2VYKDJhPcxIqaJ6-9JUR5XxU');
PROXY = 'socks5://148.72.209.6:57437'
apihelper.proxy = {'https': PROXY}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    data = open('wp1.txt', encoding='utf8').read()

    query = input('Дай ')

    sent = data.split(".")
    word = data.split()

    count, conditions = query.split(':')
    type = count[1]
    count = count[0]
    count = int(count)
    conditions = conditions.split(',')

    conditions = [c.strip() for c in conditions]
    checker = 0
    a = 0
    if type == "п":
        a = 0
        list = []
        checker = 0
        for s in sent:
            if all(c in s for c in conditions) and not list.__contains__(s):
                list.append(s)
                print(s)
                print('=================')
                a += 1
            if a == count:
                break

    if type == "с":
        a = 0
        list = []
        for s in word:
            if all(c in s for c in conditions) and not list.__contains__(s):
                list.append(s)
                bot.send_message(message.from_user.id, s)
                bot.send_message(message.from_user.id, '=================')
                a += 1
            if a == count:
                break
    if a != count:
        if type == "с": type_str = "слово"
        if type == "п": type_str = "предложение"
        bot.send_message(message.from_user.id, "Насколько я понял, вы хотели получить", type_str, ", содержащее:",
                         conditions,
                         "в количестве", count,
                         ", однако в полном издании Войны и мира нет такого количества примеров ",
                         "(вы получили ровно столько, сколько было)! Попробуйте смягчить условия поиска.")
bot.polling(none_stop=True, interval=0)