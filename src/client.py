import polygon
import dotenv
import dataclasses


@dataclasses.dataclass
class Client:
    __api_key = dotenv.dotenv_values(".env")['API_KEY']

    def get_entire_stock_daily(self, date: str, adjusted: bool = True, raw_response: bool = False) -> dict | None:
        """
        Get the entire stock daily for a given date.
        :param date: The date for which the stock data is to be retrieved
        :param adjusted: True if the stock data should be adjusted, False otherwise
        :param raw_response: True if the stock data should include OTC stocks, False otherwise
        :return: The stock data for the given date
        """
        with polygon.StocksClient(self.__api_key, False) as stock_client:
            return stock_client.get_grouped_daily_bars(date, adjusted, raw_response)

    def get_all_tickers(self) -> dict | None:
        """
        Get all the tickers for the stock market
        :return: The tickers for the stock market
        """
        with polygon.StocksClient(self.__api_key, False) as stock_client:
            return stock_client.get