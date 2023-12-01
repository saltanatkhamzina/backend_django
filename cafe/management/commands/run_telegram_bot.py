from django.core.management.base import BaseCommand
import telebot
from telebot import types
from cafe.models import Food

bot = telebot.TeleBot("6292694564:AAFIwnfE_wFvHAkB9atirOOA30oTNiIh038")  # Вставьте сюда свой токен


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['foods'])
def foods(message):
    foods = Food.objects.all()
    for food in foods:
        bot.send_message(message.chat.id, f"{food.name} {food.price}")


response = (
    "Commands:\n"
    "/start: type start to get Hello World!\n"
    "/foods: show foods\n"
    "/add <shape> <color>: add another food"
)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, response)


@bot.message_handler(commands=['add'])
def handle_add_food(message):
    parts = message.text.split(maxsplit=2)
    if len(parts) == 3:
        _, name, price = parts
        food = Food.objects.create(name=name, price=price)
        bot.send_message(message.chat.id, f"Еда {name} - {price}KZT!")
    else:
        bot.send_message(message.chat.id, "Используйте /add <name> <price>")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
