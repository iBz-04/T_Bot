<div align="center" style="margin-bottom: 20px">
  <a href="https://authen-sandy.vercel.app/">
    <img
      src="https://res.cloudinary.com/diekemzs9/image/upload/v1745491657/photo_5787624364898895914_c_hytcnl.jpg"
      alt="T_Bot"
      height="100"
    />
  </a>

  <h3 align="center">T_Bot
  </h3>
  <b>
     Earthquake response telegram bot for Tuzla Belediyesi
  </b>
</div>
<hr>


T_Bot is a specialized Telegram bot designed to help residents of Tuzla, Istanbul, quickly locate the nearest emergency gathering areas during earthquake events. The bot provides critical information to ensure safety during seismic activities, focusing specifically on the Tuzla district.

## T_Bot: Tuzla Deprem Güvenli Toplanma Alanları Telegram Botu

T_Bot, Tuzla, İstanbul sakinlerinin deprem anında en yakın acil toplanma alanlarını hızlıca bulmalarına yardımcı olmak için tasarlanmış özel bir Telegram botudur. Bot, özellikle Tuzla ilçesine odaklanarak, sismik aktiviteler sırasında güvenliği sağlamak için kritik bilgiler sunar.

## Features

- **Location-Based Search**: Find the nearest emergency gathering area by:
  - Sharing your current location directly through Telegram
  - Entering specific latitude and longitude coordinates
  - Searching by neighborhood (mahalle) name

- **Comprehensive Data**: Access information about designated safe spots including:
  - Name and exact location of the gathering area
  - Distance from your current location (in kilometers)
  - Type of facility (usually parks or open areas)

- **Multilingual Support**: Available in Turkish to serve the local community effectively
- **Emergency Numbers**: Use `/acil` to get Istanbul emergency phone numbers.
- **Earthquake Precautions**: Use `/onlem` to receive earthquake safety tips.

## Data Source

The bot uses official emergency gathering area data for Tuzla district, stored in `toplanma.csv`. Each entry contains detailed information about safe spots, including:

- Geographic coordinates (latitude and longitude)
- Neighborhood (mahalle) information
- Facility type and status
- Available amenities (electricity, water, WC)
- Total area and capacity information

## Technical Implementation

- **Framework**: Built using Python and the python-telegram-bot library
- **Data Processing**: Uses pandas for efficient data handling and filtering
- **Distance Calculation**: Implements the Haversine formula to calculate precise distances between coordinates
- **Deployment**: Can be deployed locally or on a cloud server with the included Procfile

## Installation and Setup

### Requirements

- Python 3.x
- Telegram Bot API token (obtained from [@BotFather](https://t.me/botfather))

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/T_BOT.git
   cd T_BOT
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Telegram Bot token:
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   CSV_PATH=toplanma.csv
   ```

5. Run the bot:
   ```bash
   python src/bot.py
   ```

## Usage

1. Start a chat with the bot on Telegram: [https://t.me/ToplanmaIstanbulBot](https://t.me/ToplanmaIstanbulBot)
2. Send the `/start` command to receive instructions
3. Use the `/bul` command followed by:
   - A neighborhood name: `/bul Cami`
   - Coordinates: `/bul 40.82196 29.31523`
   - Or simply share your location
4. Use the `/acil` command to get emergency numbers
5. Use the `/onlem` command to get earthquake precautions

## Limitations

- Currently only supports the Tuzla district of Istanbul
- Data is static and requires manual updates

## Future Enhancements

- Expand coverage to other districts in Istanbul
- Add real-time earthquake alert integration
- Implement route guidance to the nearest safe spot
- Add multi-language support

## Kurulum ve Kullanım (Turkish)

Bot ile doğrudan iletişime geçmek için: [https://t.me/ToplanmaIstanbulBot](https://t.me/ToplanmaIstanbulBot)

### Gereksinimler

- Python 3.x
- Telegram Bot API anahtarı ([@BotFather](https://t.me/botfather)'dan alınabilir)

### Yerel Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/yourusername/T_BOT.git
   cd T_BOT
   ```

2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv venv
   # Windows için:
   venv\Scripts\activate
   # Unix veya MacOS için:
   source venv/bin/activate
   ```

3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. `.env` dosyası oluşturun ve Telegram Bot token'ınızı ekleyin:
   ```
   TELEGRAM_TOKEN=telegram_bot_token_buraya
   CSV_PATH=toplanma.csv
   ```

5. Botu çalıştırın:
   ```bash
   python src/bot.py
   ```

## Komutlar

- `/start` : Bot ile iletişimi başlatır ve kullanılabilir komutları listeler.
- `/bul <mahalle adı>` veya `<enlem> <boylam>`: En yakın toplanma alanını bulur.
- `/acil`: İstanbul acil durum numaralarını gösterir.
- `/onlem`: Deprem önlemlerini gösterir.