import config
import telebot
from telebot import types
from string import Template
bot = telebot.TeleBot(config.shwabra_token)

data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    data['order']=''
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALHX2Aa2thSpwZU0cSHsZNlfCDmjgUBAAL9DgAC6VUFGAEGX7AwR0S8HgQ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
    order_btn = types.KeyboardButton('/заказ')
    about_btn = types.KeyboardButton('/о_нас')
    address_btn = types.KeyboardButton('/адрес')
    contacts_btn = types.KeyboardButton('/контакты')
    markup.add(
        order_btn, about_btn, address_btn,contacts_btn
    )
    bot.send_message(
        message.chat.id, f'Привет, {message.from_user.first_name}, я  бот Швабра-Кадабра и я могу помочь тебе сделать покупки мыломоющих средств. Начнем?',
        reply_markup=markup
    )

@bot.message_handler(commands=['контакты'])
def send_about_msg(message):
    text = """
    *Режим работы:
       понедельник- суббота: с 9:00 до 17:00
       воскресенье:с 9:00 до15:00

     Телефон для справок: 0555722474*
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(commands=['о_нас'])
def send_contact(message):
    text = """
    *Привет, я бот "Швабра-Кадабра" у меня очень большой выбор мыломоющих средств и всего, что нужно для чистоты.
    У меня оптовые цены, есть доставка и консультация. Рады тебя приветсвовать!!*
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALIqmAcPNgU-fkPPrTy_eR3DoL8ikRZAAJiAQACygMGCzYVIxzwn1B9HgQ')


@bot.message_handler(commands=['адрес'])
def send_address_msg(message):
    bot.send_location(message.chat.id, latitude='42.890941', longitude='74.848999')

@bot.message_handler(commands=['заказ'])
def get_order(message):
         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALHZGAa202m2GnQVD9fz5xDfk8BdBbIAAIPywACY4tGDBRdVLsJlRRRHgQ') 
         # Готовим кнопки 
         keyboard = types.InlineKeyboardMarkup()
         key_poroshok = types.InlineKeyboardButton(text='Стиральный порошок', callback_data='poroshok') 
         # И добавляем кнопку на экран 
         keyboard.add(key_poroshok) 
         key_posuda = types.InlineKeyboardButton(text='Средсво для мытья посуды', callback_data='posuda') 
         keyboard.add(key_posuda) 
         key_pol = types.InlineKeyboardButton(text='Средсво для мытья пола', callback_data='pol') 
         keyboard.add(key_pol) 
         key_chistyashee = types.InlineKeyboardButton(text='Чистящее средство', callback_data='chistyashee') 
         keyboard.add(key_chistyashee) 
         key_otbelivatel = types.InlineKeyboardButton(text='Отбеливатель', callback_data='otbelivatel') 
         keyboard.add(key_otbelivatel) 
         key_opolaskivatel = types.InlineKeyboardButton(text='Ополаскиватель для белья', callback_data='opolaskivatel') 
         keyboard.add(key_opolaskivatel) 
         key_okna = types.InlineKeyboardButton(text='Средство для мытья окон', callback_data='okna') 
         keyboard.add(key_okna) 
         key_unitaz = types.InlineKeyboardButton(text='Средство для мытья унитазов', callback_data='unitaz') 
         keyboard.add(key_unitaz) 
         bot.send_message(message.from_user.id, text='Выбери покупку', reply_markup=keyboard)
        
         


def get_weight (message):
  
    chat_id = message.chat.id
    data['id'] = chat_id
    
    if 'order' not in data:
        data['order'] = message.text
    elif 'order' in data:
        data['order'] = str(data.get('order'))+ '--'+message.text
    list_of_weight = ('1 кг', '3 кг', '5 кг', '9 кг')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(*list_of_weight)
    msg = bot.send_message(chat_id, 'Выберите вес', reply_markup=markup) 
    
    bot.register_next_step_handler(msg, get_more)


def get_capacity_small (message):
    chat_id = message.chat.id
    data['id'] = chat_id
   
    if 'order' not in data:
        data['order'] = message.text
    elif 'order' in data:
        data['order'] = str(data.get('order'))+ '--'+message.text
    
    list_capacity_small = ('0.5 литра', '0,75 литра', '1 литр')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(*list_capacity_small)
    msg = bot.send_message(chat_id, 'Выберите объем', reply_markup=markup) 
    bot.register_next_step_handler(msg, get_more)

def get_capacity_big (message):
    chat_id = message.chat.id
    data['id'] = chat_id
    if 'order' not in data:
        data['order'] = message.text
    elif 'order' in data:
        data['order'] = str(data.get('order'))+ '--'+message.text
    list_capacity_big= ('1 литр', '1.5 литра', '2 литра','5 литров')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(*list_capacity_big)
    msg = bot.send_message(chat_id, 'Выберите объем', reply_markup=markup) 
    bot.register_next_step_handler(msg, get_more)


def get_amount (message):
    chat_id = message.chat.id
    data['id'] = chat_id
   
    if 'order' not in data:
        data['order'] = message.text
    elif 'order' in data:
        data['order'] = str(data.get('order'))+ '--'+message.text
    list_capacity_big= ('1 шт', '3 шт', '2 шт','5 шт')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(*list_capacity_big)
    msg = bot.send_message(chat_id, 'Выберите количество', reply_markup=markup) 
    bot.register_next_step_handler(msg, get_more)


def get_more (message):
    chat_id = message.chat.id
    data['id'] = chat_id
    if 'order' not in data:
        data['order'] = message.text
    elif 'order' in data:
        data['order'] = str(data.get('order'))+ '--'+message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
    yes_btn = types.KeyboardButton('/добавить')
    no_btn = types.KeyboardButton('/оформляем')
    markup.add(yes_btn, no_btn)
    bot.send_message(message.chat.id, 'Добавить еще что-то в заказ или переходим к оформлению?', reply_markup=markup)
   

@bot.message_handler(commands=['добавить'])
def if_yes(message):
    
    msg=bot.send_message(message.chat.id, 'Добавляем товар?')
    bot.register_next_step_handler(msg, get_order)

@bot.message_handler(commands=['оформляем'])
def if_no(message):
    
    msg=bot.send_message(message.chat.id, 'Оформляем заказ?')
    bot.register_next_step_handler(msg, get_phonenumber)


@bot.callback_query_handler(func=lambda call: True) 
def callback_worker(call):
    try:   
        if call.data=='poroshok':
           
            list_of_powder = (
            'Персил', 'Тайд', 'Миф', 'ABC', 'Ариель','Ушастый нянь'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_powder )
            msg = bot.send_message(call.message.chat.id, 'Выберите стиральный порошок', reply_markup=markup)
            bot.register_next_step_handler(msg, get_weight)

        elif call.data=='posuda':
           
            list_of_dishwashing  = (
            'Фери', 'АОС', 'Мила', 'Пчелка', 'Morning Fresh'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_dishwashing )
            msg = bot.send_message(call.message.chat.id, 'Выберите средство для мытья посуды', reply_markup=markup)
            bot.register_next_step_handler(msg, get_capacity_small)

        elif call.data=='pol':
            
            list_of_floor_cleaner  = (
            'Мистер Пропер', 'Grasse', 'Миф'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_floor_cleaner )
            msg = bot.send_message(call.message.chat.id, 'Выберите средство для мытья пола', reply_markup=markup)
            bot.register_next_step_handler(msg, get_amount)

        elif call.data=='chistyashee':
           
            list_of_cleaning_agent  = (
            'Комет', 'АБС', 'Ашкан', 'Санита', 'Брайт'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_cleaning_agent )
            msg = bot.send_message(call.message.chat.id, 'Выберите Чистящее средство', reply_markup=markup)
            bot.register_next_step_handler(msg, get_amount)

        elif call.data=='otbelivatel':
            
            list_of_bleach = (
            'Sanfor', 'Sanita', 'Vanish', 'ABC'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_bleach )
            msg = bot.send_message(call.message.chat.id, 'Выберите отбеливатель', reply_markup=markup)
            bot.register_next_step_handler(msg, get_amount)

        elif call.data=='opolaskivatel':
            
            list_of_conditioner = (
            'Ленор', 'Персил', 'Ушастый нянь', 'ABC', 'Ариель'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_conditioner )
            msg = bot.send_message(call.message.chat.id, 'Выберите ополаскиватель для белья', reply_markup=markup)
            bot.register_next_step_handler(msg, get_capacity_big)

        elif call.data=='okna':
           
            list_of_window_cleaner = (
            'Мистер мускул', 'Грасс', 'Уникум', 'ABC'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_window_cleaner )
            msg = bot.send_message(call.message.chat.id, 'Выберите средство для мытья окон', reply_markup=markup)
            bot.register_next_step_handler(msg, get_amount)
        
        elif call.data=='unitaz':
           
            list_of_toilet_bowl = (
            'Sanfor', 'Туалетный Утенок', 'Мистер Мускул', 'Санита', 'WS-гель'
            )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) 
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add(*list_of_toilet_bowl )
            msg = bot.send_message(call.message.chat.id, 'Выберите средство для мытья унитаза', reply_markup=markup)
            bot.register_next_step_handler(msg, get_amount)

    except Exception as e:
        print(repr(e))
       
def get_phonenumber(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALHbGAa3Ob-p6KUHbCCHe_aOLFjRNIhAAIIAANr7XwKNYGgf24KQ38eBA') 
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, 'Отправьте номер телефона', reply_markup=markup)
    bot.register_next_step_handler(msg, get_address)
    
def get_address(message):
    if not message.text.isdigit():
        msg = bot.send_message(message.chat.id, 'Неправильный номер')
        bot.register_next_step_handler(msg, get_address)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALHdGAa3cbWMmmTKCqAh1kucPHN-7zjAAISCwAC-gu2CCrNGxAKttgRHgQ') 
        data['phone_number'] = message.text
        msg = bot.send_message(message.chat.id, 'Отправьте ваш адрес')
        bot.register_next_step_handler(msg, send_finally)
       
def send_finally(message):
    data['address'] = message.text
    bot.send_message(message.chat.id, get_order_finally_data(data, 'Спасибо за покупку! для уточнения заказа и его стоймости, вам перезвонят'), parse_mode='Markdown')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALIrWAcPVF4mxXu29qW-3ZGsoKALnxcAAIEDwAC6VUFGPrvJ69KStqKHgQ') 
    bot.send_message(message.chat.id, 'Для более подробной информаци о товарах и ценах посетите нашу страницу в Инстаграм https://www.instagram.com/shvabra_kadabra_kant/')

def get_order_finally_data(data, message):
    template = Template(
        '$text \n Идентификатор клиента: *$id* \n Наименование товара: *$order*  \n Адрес клиента: *$address*' 
    )
        
    return template.substitute(
        {
            'id': data.get('id'),
            'order':  data.get('order'),
            'weight':data.get('weight'),
            'address': data.get('address'),
            'text': message
        }
    )


bot.polling(none_stop=True, interval=0)