import telebot
import os
from dotenv import load_dotenv

load_dotenv()
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Create bot instance
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Get the photo file_id
        file_id = message.photo[-1].file_id

        # Get file path using file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path

        # Download the photo
        downloaded_file = bot.download_file(file_path)

        # Specify the local path to store the image
        local_path = f"uploads/upload.jpg"

        # Save the image locally
        with open(local_path, 'wb') as f:
            f.write(downloaded_file)

        # Respond to the user
        bot.reply_to(message, "Image saved successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Polling to continuously check for new messages
    bot.polling(none_stop=True)
