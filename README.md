# Telegram Bot Printer

This project provides a Telegram bot that receives PDF documents and automatically prints them on a pre-selected printer using a Raspberry Pi. The printer is selected at the start of the script through the terminal.

## Features

- **Automatic PDF Printing**: Send a PDF file to the bot, and it will print it on the pre-configured printer.
- **Secure Token Management**: Utilizes a `.env` file to securely store the Telegram bot token.
- **Raspberry Pi Compatible**: Designed to run efficiently on a Raspberry Pi with a connected printer.

## Requirements

- **Hardware**: Raspberry Pi with a connected and configured printer.
- **Software**: 
  - Python 3.6+
  - CUPS (Common UNIX Printing System) installed and configured on the Raspberry Pi
- **Python Packages**:
  - `python-telegram-bot`
  - `PyPDF2`
  - `python-cups`
  - `python-dotenv`

## Installation

1. **Install System Dependencies**:

    Update your package list and install the required packages using `apt`:

    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip python3-python-telegram-bot python3-pypdf2 python3-cups python3-dotenv
    ```

2. **Clone the Repository**:

    Clone this repository to your Raspberry Pi:

    ```bash
    git clone https://github.com/petreleon/telegram-bot-printer.git
    cd telegram-bot-printer
    ```

3. **Create a `.env` File**:

    In the root of the project directory, create a `.env` file and add your Telegram bot token:

    ```plaintext
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
    ```

    Replace `your_telegram_bot_token_here` with the actual Telegram bot token you obtained from BotFather.

4. **Run the Script**:

    Start the script and select the printer you want to use:

    ```bash
    python3 your_script_name.py
    ```

    When prompted, choose the printer from the list by entering its corresponding number.

## Usage

- **Start the bot**: Use the `/start` command on Telegram to begin interacting with the bot.
- **Send a PDF**: Once the bot is running, send a PDF file to the bot via Telegram, and it will print the document on the selected printer.

## Configuration

### Environment Variables

- **`TELEGRAM_BOT_TOKEN`**: This environment variable holds your Telegram bot API token, which should be stored in the `.env` file.

## Troubleshooting

- **No Printers Found**: Ensure CUPS is installed and configured correctly on your Raspberry Pi. Verify that your printer is connected and recognized by CUPS.
- **Bot Not Responding**: Double-check the bot token in the `.env` file and ensure the bot is correctly set up with BotFather.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
