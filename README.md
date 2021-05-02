# elon-trade-doge

## RUN with Docker

```shell script
main directory

docker build -t etd:latest . && docker run -it --name trade_doge -d etd
```

## CONFIGURATION FILE (.env)
####Please configure .env file according to your preferences
- BINANCE_API_KEY*: binance api key
- BINANCE_SECRET_KEY*: binance secret key
- TWITTER_ACCESS_TOKEN*: twitter access token
- TWITTER_ACCESS_TOKEN_SECRET*: twitter access token secret
- TWITTER_CONSUMER_KEY*: twitter consumer key
- TWITTER_CONSUMER_SECRET*: twitter consumer secret key
- LEVERAGE*: leverage you want to open position
- MARGIN_TYPE: CROSS or ISOLATED (default)
- TOTAL_USDT_INVESTMENT_PERCENTAGE*: total USDT you want to invest (**expressed as a percentage**)
- STOP_LOSS_PERCENTAGE: stop loss market (**expressed as a percentage**)
- TAKE_PROFIT_PERCENTAGE: take profit market (**expressed as a percentage**)

NOTE: for twitter tokens please go to: https://developer.twitter.com/en/portal/dashboard

## USEFUL
- The BOT is listening for Elon Musk tweets about DOGE, if he tweets the bot will open automatically open a position for you
- Everytime Elon tweeted about DOGE, the price went up 20% minimum
- The BOT is working on **BINANCE ONLY**
- TOTAL_USDT_INVESTMENT_PERCENTAGE: only feature wallet is considered. Example, If you have 100$ in features wallet, and you set TOTAL_USDT_INVESTMENT_PERCENTAGE=10, it means you want to open a 10$ LONG position for DOGEUSDT.
- Make sure to have enough money to buy **(minimum 5 USDT)**
- If you provide STOP_LOSS_PERCENTAGE the bot will create market stop loss position for you at the price you indicated. Example, if you indicate **15**, it means that if the entry price goes lower than 15% than close position.
- If you provide TAKE_PROFIT_PERCENTAGE the bot will create market take profit position for you at the price you indicated. Example, if you indicate **20**, it means that if the entry price goes up more than 20% than take profit and position.
