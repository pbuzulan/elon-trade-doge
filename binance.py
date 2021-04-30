import os
from binance_f import RequestClient
from binance_f.base.printobject import PrintBasic
from binance_f.model import FuturesMarginType, OrderSide, OrderType, PositionSide, OrderRespType


def calc_percentage(n: float, v: float):
    return (n * v) / 100


BINANCE_API_KEY = os.environ['BINANCE_API_KEY']
BINANCE_SECRET_KEY = os.environ['BINANCE_SECRET_KEY']

SYMBOL = 'DOGEUSDT'
LEVERAGE = int(os.environ['LEVERAGE'])
MARGIN_TYPE = os.getenv('MARGIN_TYPE', 'ISOLATED')
TOTAL_USDT_INVESTMENT_PERCENTAGE = int(os.environ['TOTAL_USDT_INVESTMENT_PERCENTAGE'])
STOP_LOSS_PERCENTAGE = os.getenv('STOP_LOSS_PERCENTAGE')
TAKE_PROFIT_PERCENTAGE = os.getenv('TAKE_PROFIT_PERCENTAGE')


class Binance:
    def __init__(self):
        self.client = RequestClient(api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY)

    def get_wallet_value(self) -> float:
        res = self.client.get_balance()
        for e in res:
            if e.asset == 'USDT':
                return e.withdrawAvailable
        return 0

    def buy(self):
        print("creating order")
        market_price = self.get_mark_price()
        quantity = calc_percentage(TOTAL_USDT_INVESTMENT_PERCENTAGE, self.get_wallet_value()) / market_price
        self.client.change_initial_leverage(SYMBOL, LEVERAGE)
        try:
            self.client.change_margin_type(SYMBOL,
                                           FuturesMarginType.CROSSED if MARGIN_TYPE == 'CROSS'
                                           else FuturesMarginType.ISOLATED)
        except Exception:
            pass

        order = self.client.post_order(symbol=SYMBOL,
                                       side=OrderSide.BUY,
                                       ordertype=OrderType.MARKET,
                                       positionSide=PositionSide.BOTH,
                                       quantity=int(quantity))

        print(f"order created successfully: market_price: {market_price}, quantity: {quantity}")
        print(f"{PrintBasic.print_obj(order)}")

        if STOP_LOSS_PERCENTAGE is not None:
            # STOP LOSS
            stop_price = market_price - calc_percentage(market_price, int(STOP_LOSS_PERCENTAGE))
            try:
                self.stop_loss(price=float("%.4f" % stop_price))
                print(f"stop loss order created successfully: stop_price: {stop_price}")
            except Exception:
                print(f"something went wrong, could not create stop loss order")
        if TAKE_PROFIT_PERCENTAGE is not None:
            # TAKE PROFIT
            take_profit = market_price + calc_percentage(market_price, int(TAKE_PROFIT_PERCENTAGE))
            try:
                self.take_profit(price=float("%.4f" % take_profit))
                print(f"take profit order created successfully: stop_price: {take_profit}")
            except Exception:
                print(f"something went wrong, could not create take profit order")

    def stop_loss(self, price: float):
        res = self.client.post_order(symbol=SYMBOL,
                                     stopPrice=price,
                                     side=OrderSide.SELL,
                                     ordertype=OrderType.STOP_MARKET,
                                     positionSide=PositionSide.BOTH,
                                     closePosition=True,
                                     newOrderRespType=OrderRespType.RESULT)
        print(f"{PrintBasic.print_obj(res)}")
        return res

    def take_profit(self, price: float):
        res = self.client.post_order(symbol=SYMBOL,
                                     stopPrice=price,
                                     side=OrderSide.SELL,
                                     ordertype=OrderType.TAKE_PROFIT_MARKET,
                                     positionSide=PositionSide.BOTH,
                                     closePosition=True,
                                     newOrderRespType=OrderRespType.RESULT)
        print(f"{PrintBasic.print_obj(res)}")
        return res

    def get_mark_price(self, symbol: str = SYMBOL) -> float:
        return self.client.get_mark_price(symbol).markPrice
