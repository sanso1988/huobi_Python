from huobi.constant import *
from huobi.model.market import *


class CandlestickEvent:
    """
    The candlestick/kline data received by subscription of candlestick/kline.

    :member
        symbol: the symbol you subscribed.
        timestamp: the UNIX formatted timestamp generated by server in UTC.
        interval: candlestick/kline interval you subscribed.
        data: the data of candlestick/kline.

    """

    def __init__(self):
        self.symbol = ""
        self.timestamp = 0
        self.interval = CandlestickInterval.INVALID
        self.data = Candlestick()


    def print_object(self, format_data=""):
        from huobi.utils.printobject import PrintBasic
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.timestamp, format_data + "Unix Time")
        PrintBasic.print_basic(self.interval, format_data + "Interval")
        self.data.print_object(format_data)