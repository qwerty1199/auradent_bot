# AuraDent Bot Project Instructions

This is a Telegram bot project for handling dental consultation requests from website forms.

## Project Overview
- **Purpose**: Receive consultation requests from website forms, store them in Excel files, and serve the Excel file on request
- **Technology**: Python with python-telegram-bot library
- **Data Storage**: Excel files using openpyxl library
- **Architecture**: Single bot instance handling webhook/polling from Telegram

## Key Features
- Receive consultation request messages
- Parse and validate consultation data
- Store requests in Excel format with timestamps
- Serve Excel file to authorized users on request
- Handle multiple consultation requests efficiently

## Development Guidelines
- Use environment variables for sensitive configuration (bot token, etc.)
- Implement proper error handling for file operations
- Follow Telegram bot best practices for message handling
- Ensure data persistence and backup strategies
- Use structured logging for debugging and monitoring