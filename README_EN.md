# Telegram Webhook Service

English | [简体中文](./README.md)

This is a FastAPI-based webhook service that receives HTTP requests and forwards messages to Telegram. The service provides a secure API interface that supports sending messages to specified Telegram users via webhook.



## Features

- Built on FastAPI, providing high-performance asynchronous API
- Supports security key verification to ensure API call security
- Simple and easy-to-use RESTful API interface
- Configurable server port
- Comprehensive error handling mechanism

## Requirements

- Python 3.8+
- [Poetry](https://python-poetry.org/) package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/q275343119/msg_webhook_to_telegram.git
cd msg_webhook_to_telegram
```

2. Install Poetry (if not already installed):
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/macOS
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install project dependencies:
```bash
poetry install
```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Edit `.env` file with necessary configuration:
     ```
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
     SECRET_KEY=your_secret_key_here
     PORT=8000
     ```

## Configuration

### Environment Variables

- `TELEGRAM_BOT_TOKEN`: Telegram Bot token obtained from @BotFather
- `SECRET_KEY`: Security key for webhook request verification
- `PORT`: Service running port, defaults to 8000

### Getting Telegram Bot Token

1. Search for and contact @BotFather in Telegram
2. Send the `/newbot` command
3. Follow the prompts to set up bot name and username
4. Save the generated token

## Usage

1. Start the service:
```bash
poetry run python main.py
```

2. Send a message to a specific user:
```bash
curl -X POST "http://localhost:8000/webhook" \
     -H "Content-Type: application/json" \
     -d '{
           "secret_key": "your_secret_key",
           "msg": "Hello, World!",
           "user_id": "123456789"
         }'
```

### API Documentation

- **Endpoint**: `/webhook`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "secret_key": "string",  // Security key
    "msg": "string",        // Message content
    "user_id": "string"     // Telegram user ID
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Message sent successfully"
  }
  ```

## Error Handling

The service may return the following error status codes:

- `403`: Invalid security key
- `500`: Server internal error (e.g., message sending failure)

## Security Recommendations

1. Use a sufficiently complex security key (SECRET_KEY)
2. Ensure `.env` file is not committed to version control
3. Use HTTPS in production environment
4. Regularly rotate security keys

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 