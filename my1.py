import telebot
from telebot import types
bot = telebot.TeleBot("5090930136:AAEY8wZNJAflPDQXJr-jpnF2MjWpQlqvnVQ")

name = ''
surname = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    sti = open('C:\Python\Projects\TelegramBot\Images\AmongUsKill.tgs', 'rb')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Комманды")
    item2 = types.KeyboardButton("Регестрация")

    markup.add(item1, item2)

    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     "Приевет {0.first_name}!\nМеня зовут <b>{1.first_name}!</b>\nЕсли понадобится моя помашь введие /commands что бы узнать мои уммения.".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['com', 'commands'])
def commands_message(message):
    print('com')








@bot.message_handler(func=lambda m: True)

def live(message):
    commands = ['com', 'commands', 'start', 'help', 'reg']

    if message.chat.type == 'private':
        if message.text == "Комманды":
            print('Commans')
        elif message.text == 'Регестрация':
            bot.send_message(message.from_user.id, 'Привет, ведите игформацию о себе: Ваше имя?')
            bot.register_next_step_handler(message, reg_name)
        elif message.text == commands:
            print('Commands')
        else:
            print('Не понял')

    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет, ведите игформацию о себе: Ваше имя?')
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    print(name)
    bot.send_message(message.from_user.id, 'Выша фамилия?')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    print(surname)
    bot.send_message(message.from_user.id, 'Выш возрост?')
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    age = message.text
    print(age)
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите цифроми!')

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes)
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text =question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda m: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Приятно познокомится! Теперь запиушу в базу данных.')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Попробуйте еще раз!')
        bot.send_message(call.message.chat.id, 'Ваше имя?')
        bot.register_next_step_handler(call.message, reg_name)




bot.infinity_polling()
