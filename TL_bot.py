import telebot
import base2
import tl_api

bot = telebot.TeleBot(base2.TOKEN2)
print("well done!")

@bot.message_handler(['start'])
def send_message(message):
    bot.send_message(message.chat.id , text="wellcome my friend!!:<3")

@bot.message_handler(['help'])
def reply_message(message):
    bot.reply_to(message , text="@yoko__kkkk")

@bot.message_handler(commands=['music'])
def show_msg(message):
    msg = bot.send_message(message.chat.id, 'enter name artist..')
    bot.register_next_step_handler(msg, show_music_info)

def show_music_info(message):
    artist_name = message.text
    result = tl_api.get_music_info_by_artist(artist_name)
    if result == 'ERROR':
        bot.send_message(message.chat.id , "Api error!")
        return
    text =""
    for song in result:
        text += f"title: {song[0]} \ngenre:{song[1]} \album:{song[2]} \naddress: {song[3]} \n"
    bot.send_message(message.chat.id, text)

##############################
if __name__ == '__main__':
    bot.infinity_polling()