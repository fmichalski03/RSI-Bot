import discord
import asyncio
import pandas as pd
import ta
from pybit.unified_trading import HTTP

TOKEN = 'your_token'
CHANNEL_ID = 123123123123

if __name__ == '__main__':
    session = HTTP(testnet=True)
    SYMBOL = "SOLUSDT"
    INTERVAL = 60
    PERIOD = 14
    CYCLE = 3600  # Time between 2 fetches

    client = discord.Client(intents=discord.Intents.default())


    def fetch_kline_data(symbol, interval):
        try:
            data = session.get_kline(category="spot", symbol=symbol, interval=interval, limit=200)
            return data['result']['list']
        except Exception as e:
            print(f"Error fetching data from Bybit API: {e}")
            return None


    def calculate_rsi(data, period):
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'turnover'])
        df['close'] = df['close'].astype(float)

        rsi = ta.momentum.RSIIndicator(df['close'], window=period).rsi()
        return rsi.iloc[-1]


    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        channel = client.get_channel(CHANNEL_ID)
        while True:
            kline_data = fetch_kline_data(SYMBOL, INTERVAL)
            if kline_data is None:
                await asyncio.sleep(60)  # Wait 1 minute before trying again
                continue

            rsi = calculate_rsi(kline_data, PERIOD)
            if rsi > 70:
                await channel.send(f'RSI Alert: {SYMBOL} RSI is over 70 ({rsi})')
            elif rsi < 30:
                await channel.send(f'RSI Alert: {SYMBOL} RSI is below 30 ({rsi})')

            await asyncio.sleep(CYCLE)  # Wait 1 hour before fetching again


    client.run(TOKEN)
