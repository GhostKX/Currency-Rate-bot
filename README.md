# Telegram Currency Exchange Bot

A **Python-based Telegram bot** that helps users convert between UZS (Uzbekistan Som) and USD (US Dollar). The bot allows users to input currency amounts in either UZS or USD and converts them based on the current exchange rate. The bot is built using the **PyTelegramBotAPI** library, and it provides a user-friendly interface with buttons for navigation.

## Features

### **Currency Conversion**
- **UZS to USD**: Converts amounts from Uzbekistan Som (UZS) to US Dollars (USD).
- **USD to UZS**: Converts amounts from US Dollars (USD) to Uzbekistan Som (UZS).
- **Dynamic Conversion**: Exchange rates are hardcoded in the bot (currently 1 USD = 12648.75 UZS).
- **Real-Time Conversion**: Instant conversion results based on the user’s input.

### **User Interaction**
- **Start Command (`/start`)**: Initializes interaction with the user and provides options for conversion.
- **Currency Selection**: Users can choose between converting **UZS to USD** or **USD to UZS** via interactive buttons.
- **Back Button**: Users can navigate back to the main menu to select other actions.

### **Error Handling**
- **Input Validation**: Ensures users enter valid numeric values for currency amounts.
- **Back Button Handling**: Allows users to return to the previous step if needed.

## Requirements

- **Python 3.8+**
- **PyTelegramBotAPI** (`pyTelegramBotAPI`)
- **python-dotenv** (to load environment variables)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/GhostKX/Currency-Rate-bot.git
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot

- Create `.env` file to store the Telegram API_KEY
```python
bot = telebot.TeleBot(API_KEY)
```

4. Navigate to the file
```bash
cd Currency-Rate-bot
```

5. Run the bot
```bash
python PythonCurrencyBot.py
```

## Usage

### Starting the Bot
- Use the `/start` command to begin interacting with the bot.
- The bot will present two options:
  - **📝 Register**: Begin the process of registering a new user.
  - **‼️ Delete**: Delete an existing user from the database.
- Users can navigate through the registration steps, providing their first name, last name, email, and phone number.

### Currency Conversion
- **UZS to USD**: Select **"UZS > USD($)"** to convert from UZS to USD.
- **USD to UZS**: Select **"USD($) > UZS"** to convert from USD to UZS.
- **Enter Amount**: After selecting the currency conversion, the bot will ask for an amount to convert.


## Author

- Developed by **GhostKX**
- Github: **[GhostKX](https://github.com/GhostKX/Currency-Rate-bot)**
