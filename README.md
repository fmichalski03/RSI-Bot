# Discord RSI Alert Bot

This is a Discord bot that fetches K-line data for the SOL/USDT pair from Bybit, calculates the RSI, and sends an alert to a Discord channel if the RSI value is over 70 or below 30.

## Requirements

- Docker
- Discord bot token

## How to Run

1. Clone this repository.
2. Replace __TOKEN__ and __CHANNEL_ID__ in bot.py with your Discord bot token and channel ID.
3. Build the Docker image:
```commandline
docker build -t discord-bot .
```
4. Run the Docker container:
```commandline
docker run -d --name discord-bot discord-bot
```
The bot will start and send RSI alerts to the specified Discord channel.

