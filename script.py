from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import cups
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the Telegram bot token from the .env file
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def select_printer():
    conn = cups.Connection()
    printers = list(conn.getPrinters().keys())

    if not printers:
        print("No printers found.")
        return None

    print("Available printers:")
    for i, printer in enumerate(printers, 1):
        print(f"{i}: {printer}")

    while True:
        try:
            printer_index = int(input("Select the printer number you want to use: ")) - 1
            if 0 <= printer_index < len(printers):
                selected_printer = printers[printer_index]
                print(f'Printer "{selected_printer}" selected.')
                return selected_printer
            else:
                print("Invalid printer number, please try again.")
        except ValueError:
            print("Please enter a valid number.")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me a PDF file, and I will print it.")

def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document

    if file.mime_type == 'application/pdf':
        file_path = file.get_file().download()
        update.message.reply_text(f'Received PDF file: {file.file_name}. Printing...')

        # Print the PDF using CUPS
        conn = cups.Connection()
        conn.printFile(selected_printer, file_path, "Document from Telegram Bot", {})

        os.remove(file_path)  # Cleanup the file after printing
        update.message.reply_text(f'Printed {file.file_name} on {selected_printer}.')
    else:
        update.message.reply_text('Please send a PDF file.')

def main() -> None:
    global selected_printer
    selected_printer = select_printer()

    if not selected_printer:
        print("Exiting because no printer was selected.")
        return

    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("application/pdf"), handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
