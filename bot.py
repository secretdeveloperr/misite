import telebot
import os
import key
from telebot import types


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

bot = telebot.TeleBot(key.key)

@bot.message_handler(commands=['start'])
def welcome(message):
    global keyboard
    global back
    global door
    global choose_hm
    global Ukrainian_lenguage_edit_or_add
    global Ukrainian_Literature_edit_or_add
    global Music_bot

    #   BACK KEYBOARD
    back = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton(text="Back ⬅️", callback_data="back")
    back.add(back_btn)

    #   KEYBOARD
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Home work 🏠", callback_data="work")
    Music = types.InlineKeyboardButton(text="Music 🎶", callback_data="music")
    My_economy = types.InlineKeyboardButton(text="Economy", callback_data="Economy")
    keyboard.add(callback_button)
    keyboard.add(Music)
    keyboard.add(My_economy)
    bot.send_message(message.chat.id, "I`m Yde, \n Please choose mode in menu below :)" , reply_markup=keyboard)



    # MESSAGE.chat_id
    door = message.chat.id


    # CHOOSE HOME WORK...
    choose_hm = types.InlineKeyboardMarkup()
    Ukrainian_literature = types.InlineKeyboardButton(text="Ukrainian Literature 🖊", callback_data="UKR_LIT")
    Ukrainian_lenguage = types.InlineKeyboardButton(text="Ukrainian lenguage 🇺🇦", callback_data="UKR_LENG")
    choose_hm.add(Ukrainian_literature, Ukrainian_lenguage)
    choose_hm.add(back_btn)

    #choose or edit Ukrainian Literature
    Ukrainian_Literature_edit_or_add = types.InlineKeyboardMarkup()
    Edit = types.InlineKeyboardButton(text="Edit 🔧", callback_data="edit_ukr_lit")
    Look = types.InlineKeyboardButton(text="Look 👁‍🗨", callback_data="look_ukr_lit")
    Ukrainian_Literature_edit_or_add.add(Edit, Look)
    Ukrainian_Literature_edit_or_add.add(back_btn)

    #choose or edit Ukrainian Lenguage
    Ukrainian_lenguage_edit_or_add = types.InlineKeyboardMarkup()
    Edit = types.InlineKeyboardButton(text="Edit 🔧", callback_data="edit_ukr_leng")
    Look = types.InlineKeyboardButton(text="Look 👁‍🗨", callback_data="look_ukr_leng")
    Ukrainian_lenguage_edit_or_add.add(Edit, Look)
    Ukrainian_lenguage_edit_or_add.add(back_btn)

    # Music

    Music_bot = types.InlineKeyboardMarkup()
    Upload = types.InlineKeyboardButton(text="Upload music ➕", callback_data="Upload_music")
    Listen = types.InlineKeyboardButton(text="Listen to music 🎧", callback_data="Listen_music")
    back_btn = types.InlineKeyboardButton(text="Back ⬅️", callback_data="back")
    Music_bot.add(Upload, Listen)
    Music_bot.add(back_btn)








def UKR_lit_edit(message):
    open('Ukrainian Literature.txt', 'w').write(str(message.text))
    bot.send_message(door, "Success!", reply_markup= back)

def UKR_lit_look():
    looking = open('Ukrainian Literature.txt', 'r')
    bot.send_message(door, "Success!  \n\nYou`r home work:\n\n" + str(looking.read()), reply_markup= back)

def UKR_len_edit(message):
    open('Ukrainian lenguage.txt', 'w').write(str(message.text))
    bot.send_message(door, "Success! ", reply_markup= back)

def UKR_len_look():
    looking = open('Ukrainian lenguage.txt', 'r')
    bot.send_message(door, "Success!  \n\nYou`r home work:\n\n" + str(looking.read()), reply_markup= back)

def get_my_dir():
        global total
        global food
        global entertainment
        global clothes

        GET_USER_ID = door
        path = "./ECONOMY/%s" % GET_USER_ID
        total = str(path) + "/total.txt"
        food = str(path) + "/food.txt"
        entertainment = str(path) + "/entertainment.txt"
        clothes = str(path) + "/clothes.txt"
        if os.path.isdir(path) == False:
            try:
                 os.makedirs(path)
                 total_m = open(total, "w+")
                 food_m = open(food, "w+")
                 entertainment_m = open(entertainment, "w+")
                 clothes_m = open(clothes, "w+")

            except OSError:
                bot.send_message(door,"Creation of the directory %s failed" % path)
            else:
                msg = bot.send_message(door,"Please, write your total money on mounth. \n  \nExample: 15000")
                bot.register_next_step_handler(msg,write_total_money)
        else:
            econ_menu = types.InlineKeyboardMarkup()
            show_result = types.InlineKeyboardButton(text="Show result now ", callback_data="show_result")
            add_total = types.InlineKeyboardButton(text="Edit month salary", callback_data="add_total")
            add_entertainment = types.InlineKeyboardButton(text="Add enetertainment expenses", callback_data="add_entertainment")
            add_food = types.InlineKeyboardButton(text="Add food expenses", callback_data="add_food")
            add_clothes = types.InlineKeyboardButton(text="Add clothes expenses", callback_data="add_clothes")
            back_btn = types.InlineKeyboardButton(text="Back ⬅️", callback_data="back")
            econ_menu.add(show_result)
            econ_menu.add(add_total)
            econ_menu.add(add_entertainment)
            econ_menu.add(add_food)
            econ_menu.add(add_clothes)
            econ_menu.add(back_btn)
            total_write = open(total , "r")
            entertainment_write = open(entertainment , "r")
            bot.send_message(door, "Success!",reply_markup = econ_menu)

def write_total_money(message):
    back = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton(text="Back ⬅️  ", callback_data="back")
    back.add(back_btn)
    total_write = open(total , "w").write(str(message.text))
    total_write = open(total , "r")
    entertainment_write = open(entertainment , "r")
    bot.send_message(door, "Success! \n Now your monthly salary: %s" % str(total_write.read(), reply_markup = back))





def show_result():
    total_write = open(total , "r")
    food_write = open(food , "r")
    entertainment_write = open(entertainment , "r")
    clothes_write = open(clothes , "r")

    bot.send_message(door,"\nNow your monthly salary:" + str(total_write.read()) + " \n Your enetertainment expenses:"+ str(entertainment_write.read()) +"\n Your food expenses:"+ str(food_write.read()) +"\n Your clothes expenses"+ str(clothes_write.read()) +"\n left:")











@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        global msg
        if call.data == "work":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="OK, choose you`r home work? \n(!old home work was delate!) ",reply_markup=choose_hm)
            call.data += ""

        if call.data == "back":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="I`m Yde, \n Please choose mode in menu below :)" , reply_markup=keyboard)
            call.data += ""

        if call.data == "UKR_LIT":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Edit / look ?" , reply_markup = Ukrainian_Literature_edit_or_add )
            call.data += ""

        if call.data == "edit_ukr_lit":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Write... ")
            bot.register_next_step_handler(msg, UKR_lit_edit)
            call.data += ""
        if call.data == "look_ukr_lit":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Looking...")
            UKR_lit_look()
            call.data += ""

        if call.data == "UKR_LENG":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Edit / look ?" , reply_markup = Ukrainian_lenguage_edit_or_add )
            call.data += ""

        if call.data == "edit_ukr_leng":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Write... ")
            bot.register_next_step_handler(msg, UKR_len_edit)
            call.data += ""

        if call.data == "look_ukr_leng":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Looking... ")
            UKR_len_look()
            call.data += ""
        if call.data == "music":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Choose mode:" , reply_markup = Music_bot)
            call.data += ""
        if call.data == "Economy":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Loading...")
            get_my_dir()
            call.data += ""
        if call.data == "show_result":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Loading...")
            show_result()
            call.data += ""

bot.polling(none_stop = True , interval = 0)
