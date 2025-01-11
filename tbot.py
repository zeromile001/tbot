import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import logging


# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

bot = telebot.TeleBot("7708151036:AAHr8gdFGd_i9j74a9WJjKa4Yhstg6I1OU4")

# Your group chat ID (replace with correct ID)
GROUP_CHAT_ID = -2317686283

# Inline keyboard for commands
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Info", callback_data="info"),
        InlineKeyboardButton("Who is CASI?", callback_data="who"),
        InlineKeyboardButton("Which Technology?", callback_data="which"),
        InlineKeyboardButton("Website", callback_data="website"),
        InlineKeyboardButton("Current Time", callback_data="time"),
    )
    return markup

# Start command for the bot
@bot.message_handler(commands=['start'])
def greet_command(message):
    bot.send_message(
        message.chat.id,
        "Hello, Welcome to the AI2AI Podcast Community!\nChoose an option below:",
        reply_markup=main_menu()
    )

# Callback handler for inline buttons
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "info":
        bot.send_message(call.message.chat.id, "Information About Group ..\n\n💡  🔍 About Us:\nThis is the hub for AI enthusiasts and fans of the AI2AI Podcast, where past AI Presidents of the USA join host AI CASI for exciting conversations on tech, innovation, and the future.", parse_mode="Markdown")
    elif call.data == "who":
        bot.send_message(call.message.chat.id, "Who is CASI?\n\n💡  Step into the Future with CASI\nEthical AI for a Decentralized Metaverse", parse_mode="Markdown")
    elif call.data == "which":
        bot.send_message(call.message.chat.id, "Which Technology are we using?\n\n💡  AI and Blockchain", parse_mode="Markdown")
    elif call.data == "website":
        bot.send_message(call.message.chat.id, "What is the website?\n\n💡  Visit us at: www.casi.live", parse_mode="Markdown")
    elif call.data == "time":
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bot.send_message(call.message.chat.id, f"What is the current time?\n\n💡  Current server time is: {current_time}", parse_mode="Markdown")

# Automatically respond to common greetings
@bot.message_handler(func=lambda message: message.text and message.text.lower() in ['hi', 'hello', 'good morning', 'good afternoon'])
def greet_text(message):
    bot.send_message(message.chat.id, "Hello, Welcome to the AI2AI Podcast Community!\nChoose an option below:", reply_markup=main_menu())

# Run the bot
print("Bot is running...")
try:
    bot.polling()
except Exception as e:
    print(f"Polling error: {e}")
