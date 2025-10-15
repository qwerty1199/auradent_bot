# AuraDent Telegram Bot

A Telegram bot designed to handle dental consultation requests from website forms. The bot receives consultation data, stores it in Excel format, and provides administrative access to download consultation records.

## Features

- 📝 **Consultation Request Handling**: Receives and parses consultation requests from users
- 📊 **Excel Integration**: Automatically stores consultation data in Excel format with timestamps
- 🔐 **Admin Controls**: Secure access to download Excel files with all consultations
- 📱 **Real-time Notifications**: Notifies administrators of new consultation requests
- 📈 **Statistics**: View consultation statistics and summaries
- 🛡️ **Error Handling**: Robust error handling and logging for reliable operation

## Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- A Telegram bot token (get one from [@BotFather](https://t.me/botfather))
- Your Telegram chat ID for admin access

### 2. Installation

```bash
# Clone or download the project
cd auradentbot

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### 3. Configuration

Edit the `.env` file with your settings:

```env
# Telegram Bot Configuration
BOT_TOKEN=your_bot_token_here

# Chat/User Configuration  
ADMIN_CHAT_ID=your_admin_chat_id_here

# File Configuration
EXCEL_FILE_PATH=consultations.xlsx

# Logging Configuration
LOG_LEVEL=INFO
```

### 4. Run the Bot

```bash
python bot.py
```

## Usage

### For Patients (Consultation Requests)

Send a message to the bot in the following format:

```
Name: John Doe
Phone: +1234567890
Email: john@example.com
Age: 30
Consultation Type: General Checkup
Message: I need a dental consultation for tooth pain
```

**JSON format is also supported:**
```json
{
    "name": "John Doe",
    "phone": "+1234567890",
    "email": "john@example.com", 
    "age": "30",
    "consultation_type": "General Checkup",
    "message": "I need a dental consultation for tooth pain"
}
```

### For Administrators

- `/get_consultations` - Download Excel file with all consultations
- `/stats` - View consultation statistics
- `/help` - Show help information

## Bot Commands

| Command | Description | Access |
|---------|-------------|--------|
| `/start` | Start the bot and see instructions | Everyone |
| `/help` | Show help and format examples | Everyone |
| `/get_consultations` | Download Excel file with all consultations | Admin only |
| `/stats` | Show consultation statistics | Everyone |

## Excel File Structure

The bot automatically creates and maintains an Excel file with the following columns:

| Column | Description |
|--------|-------------|
| Timestamp | Date and time of the consultation request |
| Name | Patient's name |
| Phone | Patient's phone number |
| Email | Patient's email address |
| Age | Patient's age |
| Consultation Type | Type of consultation requested |
| Message | Additional message or details |
| Chat ID | Telegram chat ID of the requester |

## Configuration Options

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `BOT_TOKEN` | Yes | - | Telegram bot token from BotFather |
| `ADMIN_CHAT_ID` | Yes | - | Telegram chat ID for admin access |
| `EXCEL_FILE_PATH` | No | `consultations.xlsx` | Path to Excel file |
| `LOG_LEVEL` | No | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR) |

### Getting Your Chat ID

To find your Telegram chat ID:
1. Start a conversation with [@userinfobot](https://t.me/userinfobot)
2. Send any message
3. The bot will reply with your chat ID

## Project Structure

```
auradentbot/
├── .github/
│   └── copilot-instructions.md
├── bot.py                 # Main bot application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your environment variables (create this)
├── .gitignore           # Git ignore file
├── README.md            # This file
└── consultations.xlsx   # Excel file (auto-created)
```

## Development

### Adding New Features

The bot is structured with a `ConsultationManager` class that handles all Excel operations. To add new features:

1. **New Data Fields**: Update the headers in `_ensure_excel_file_exists()` method
2. **New Commands**: Add new command handlers in the `main()` function
3. **Message Parsing**: Modify `parse_consultation_message()` for different input formats

### Logging

The bot includes comprehensive logging. Logs include:
- Consultation requests received and processed
- Excel file operations
- Error messages and stack traces
- Admin actions and file downloads

### Error Handling

- Graceful handling of malformed consultation requests
- Excel file creation and write error recovery
- Network error handling for Telegram API calls
- Input validation and sanitization

## Security Considerations

- Admin access is restricted by chat ID verification
- Sensitive configuration stored in environment variables
- Input validation prevents Excel injection attacks
- Error messages don't expose internal system details

## Deployment

### Cloud Deployment (Pella) - Recommended

**Quick Deploy to Pella:**
[![Deploy to Pella](https://img.shields.io/badge/Deploy%20to-Pella-blue)](https://pella.dev/deploy?repository=https://github.com/qwerty1199/auradent_bot)

For detailed Pella deployment instructions, see [PELLA_DEPLOYMENT.md](PELLA_DEPLOYMENT.md)

**Required Environment Variables for Pella:**
- `BOT_TOKEN`: Your Telegram bot token
- `ADMIN_CHAT_ID`: Your Telegram chat ID
- `WEBHOOK_URL`: Your Pella app URL (e.g., `https://your-app.pella.app`)

### Local Development
```bash
python bot.py
```

### Other Cloud Platforms

The bot supports both webhook and polling modes:
- **Webhook mode**: For cloud platforms (automatic when `WEBHOOK_URL` is set)
- **Polling mode**: For local development (when `WEBHOOK_URL` is empty)

For production deployment on other platforms, consider:

1. **Process Management**: Use `systemd`, `supervisor`, or `pm2`
2. **Environment Security**: Secure your `.env` file permissions
3. **Backup Strategy**: Regular backups of Excel files
4. **Monitoring**: Set up log monitoring and alerts
5. **Updates**: Plan for bot restarts during updates

### Example systemd service file:

```ini
[Unit]
Description=AuraDent Telegram Bot
After=network.target

[Service]
Type=simple
User=auradent
WorkingDirectory=/path/to/auradentbot
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Troubleshooting

### Common Issues

1. **Bot doesn't respond**
   - Check `BOT_TOKEN` in `.env` file
   - Verify bot is started with `/start` command
   - Check network connectivity

2. **Admin commands don't work**
   - Verify `ADMIN_CHAT_ID` matches your Telegram chat ID
   - Use [@userinfobot](https://t.me/userinfobot) to confirm your chat ID

3. **Excel file errors**
   - Check file permissions in the bot directory
   - Ensure Excel file isn't open in another application
   - Verify sufficient disk space

4. **Consultation parsing fails**
   - Check message format against examples
   - Ensure proper line breaks and colons in key-value format
   - Validate JSON syntax if using JSON format

### Debug Mode

Enable debug logging by setting `LOG_LEVEL=DEBUG` in your `.env` file:

```env
LOG_LEVEL=DEBUG
```

This will show detailed information about message processing, Excel operations, and API calls.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review the logs for error details

---

**Note**: Remember to keep your `.env` file secure and never commit it to version control. Always use the `.env.example` template for sharing configuration structure.