import telebot
from JSON import *
from marks import *
import time
bot = telebot.TeleBot("5051213671:AAHna1LjAM1n37qdlTtEkKmOZEXCpw1o8sw", parse_mode="html")
@bot.message_handler(commands=['start'])
def welecome(mess):
    if check("admin", mess.chat.id):
        pass
    else:
        if not check(id=mess.chat.id):
            users = get_from_json("users.json")
            bot.send_message(mess.chat.id, "Assalomu alaykum. \"Geek School\" onlayn maktabining o'quv platformasiga xush kelibsiz !!!")
            time.sleep(2)
            user = {
                'id' : mess.chat.id,
                'username' : f"@{mess.from_user.username}"
            }
            users.append(user)
            add_to_json('users.json', users)
        if not check("student", mess.chat.id):
            bot.send_message(mess.chat.id,
                "Bizning platformadan foydalanish uchun ro'yxatdan o'tishingiz zarur.",
                reply_markup=start_markup
            )

@bot.message_handler(commands=["id"])
def send_id(mess):
    bot.send_message(mess.chat.id, mess.chat.id)

@bot.message_handler(content_types=["text", "contact"])
def all_messages(mess):
    admins = get_from_json("admins.json")
    users = get_from_json("users.json")
    students = get_from_json("students.json")
    teachers = get_from_json("teachers.json")
    if check("admin", mess.chat.id):
        bot.send_message(mess.chat.id, "Siz adminsiz")
    else:
        if mess.text == "📋 Ro'yxatddan o'tish":
            if not check("student", mess.chat.id):
                student = {
                    "id" : mess.chat.id,
                    "username" : f"@{mess.from_user.username}",
                    "name" : "",
                    "date_birth" : "",
                    "phone_number" : ""
                }
                students.append(student)
        if students[find("user", mess.chat.id)]['name'] == '' and students[find("user", mess.chat.id)]['date_birth'] != ("" or "none") and students[find("user", mess.chat.id)]['phone_number'] != ("" or "none"):
            bot.send_message(mess.chat.id, "Ism-sharifingizni jo'nating.\nMisol uchun: <code>Burxon Nurmurodov</code>")
            students[find("user", mess.chat.id)]['name'] = 'none'
        elif students[find("user", mess.chat.id)]['name'] == 'none':
            students[find("user", mess.chat.id)]['name'] = f"{mess.text}"
        if students[find("user", mess.chat.id)]['date_birth'] == '' and students[find("user", mess.chat.id)]['name'] != ("" or "none") and students[find("user", mess.chat.id)]['phone_number'] != ("" or "none"):
            bot.send_message(mess.chat.id, "Tug'ilgan sanangizni jo'nating.\nFormat: <code>KK.OO.YYYY</code>\nMisol uchun: <code>02.07.2005</code>")
            students[find("user", mess.chat.id)]['date_birth'] = 'none'
        elif students[find("user", mess.chat.id)]['date_birth'] == 'none':
            students[find("user", mess.chat.id)]['date_birth'] = f"{mess.text}"
        if students[find("user", mess.chat.id)]['phone_number'] == '' and students[find("user", mess.chat.id)]['name'] != ("" or "none") and students[find("user", mess.chat.id)]['date_birth'] != ("" or "none"):
            bot.send_message(mess.chat.id, "Telefon raqamingizni jo'nating", reply_markup=share_number)
            students[find("user", mess.chat.id)]["phone_number"] = "none"
        elif students[find("user", mess.chat.id)]["phone_number"] == "none":
            students[find("user", mess.chat.id)]["phone_number"] = mess.text or mess.contact.phone_number
    add_to_json("admins.json", admins)
    add_to_json("users.json", users)
    add_to_json("students.json", students)
    add_to_json("teachers.json", teachers)


bot.infinity_polling()