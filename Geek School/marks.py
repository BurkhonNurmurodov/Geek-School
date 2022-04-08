from telebot import types

start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_reg = types.KeyboardButton("📋 Ro'yxatdan o'tish")
btn_info = types.KeyboardButton("🏫 Maktab haqida")
start_markup.row(btn_reg, btn_info)

share_number = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_share_number = types.KeyboardButton("☎️ Raqamimni ulashish", request_contact=True)
share_number.row(btn_share_number)