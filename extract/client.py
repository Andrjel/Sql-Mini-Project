import dataclasses
import aiohttp
import asyncio
import requests


def fetch_data_decorator(func):
    """Decorator to fetch data from the API.
    
    Arguments:
    func -- The API function being decorated.
    
    Return:
    wrapper -- The wrapper function.
    """
    async def wrapper(self, *args):
        """Wrapper function
        
        Arguments:
        self - ClientAsync - Client async object,
        args - list - request parameters
        
        Return:
        result - list - list of requests results
        """
        result = []
        result.append({"name": func.__name__})
        response = await func(self, *args)  
        if response.get("next_url", None):
            result.extend(await self.fetch_data(response.get("next_url")))
        return result
    return wrapper


@dataclasses.dataclass
class ClientAsync:
    """
    Polygon.io API async client
    """
    
    _api_key: str = "BH1TqYfUvL6xV1YWnpVdxiXYYZsikHM8"
    _endpoint: str = "https://api.polygon.io"

    @fetch_data_decorator
    async def get_all_tickers(self, ticker: str = None, market: str = "stocks", active: bool =True, limit: int = 100, sort: str = "ticker", order: str = "asc"):
        """Get all active tickers from the Polygon.io API.
        
        Keyword arguments:
        ticker - str - ticker symbol (default None)
        market - str - market type (default "stocks")
        active - bool - is ticker active (default True)
        limit - int - results limit on page (default 100, max 1000)
        sort - str - sort by param (default "ticker")
        order - str - order keyword (default "asc") ("asc", "desc")
        
        Return value:
        dict - response object, empty if response failed
        """
        params={
                "ticker": ticker,
                "market": market,
                "active": active,
                "limit": limit,
                "sort": sort,
                "order": order,
                "apiKey": self._api_key
        }
        params = {k: (str(v).lower() if isinstance(v, bool) else v) for k, v in params.items() if v is not None}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self._endpoint}/v3/reference/tickers",
                params=params
            ) as response:
                return await response.json()

    @fetch_data_decorator
    async def get_all_ticker_types(self, asset_class: str = None, locale: str = None):
        """Get all ticker types from the Polygon.io API.
        
        Keyword arguments:
        asset_class - str - asset class,
        locale - str - locale origin (us, global)
        
        Return:
        dict - response object, empty if response failed
        """
        params = {
            "asset_class": asset_class,
            "locale": locale,
            "apiKey": self._api_key
        }
        params = {k: v for k, v in params.items() if v is not None}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self._endpoint}/v3/reference/tickers/types",
                params=params
            ) as response:
                return await response.json()

    @fetch_data_decorator
    async def get_stock_dividend(self, ticker="AAPL"):
        """Get dividend information for certain ticker from Polygon.io API.
        
        Keyword argument:
        ticker - str - company ticker (default "AAPL")
        
        Return
        dict - response object, empty if response failed
        """
        params = {
            "ticker": ticker,
            "apiKet": self._api_key
        }
        params = {k: v for k, v in params.items() if v is not None}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self._endpoint}/v3/reference/dividends",
                params=params
            ) as response:
                return await response.json()

    @fetch_data_decorator
    def get_aggregate_bars(self, ticker, multiplier, timespan, date_from, date_to, sort="asc", limit=5000):
        """
        Get aggregate bars for a stock over a given date range in custom time window sizes.
        For example, if timespan = ‘minute’ and multiplier = ‘5’ then 5-minute bars will be returned.
        :param ticker: Specify a case-sensitive ticker symbol.
        :param multiplier: The size of the timespan multiplier.
        :param timespan: The size of the time window.
        :param date_from: YYYY-MM-DD or a millisecond timestamp
        :param date_to: YYYY-MM-DD or a millisecond timestamp
        :param sort: asc/desc
        :param limit: Max 50000 and Default 5000
        :return:
        """
        return requests.get(
            f"{self._endpoint}/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{date_from}/{date_to}",
            params={
                "sort": sort,
                "limit": limit,
                "apiKey": self._api_key
            }
        ).json()

    @fetch_data_decorator
    def get_grouped_daily(self, date):
        """
        Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets.
        :param date: The beginning date for the aggregate window.
        :return: list
        """
        return requests.get(
            f"{self._endpoint}/v2/aggs/grouped/locale/us/market/stocks/{date}",
            params={
                "apiKey": self._api_key
            }
        ).json()

    async def fetch_data(self, url):
        """
        Support method to fetch data from the API
        :param url: next URL to fetch data from (next page)
        :return: list
        """
        result = []
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url,
                params={
                    "apiKey": self._api_key
                }
            ) as response:
                data = await response.json()
                result.extend(data.get("results", {}))
                if next_url := data.get("next_url", None):
                    result.extend(await self.fetch_data(next_url))
        return result
    
async def main():
    client = ClientAsync()
    tickers = await client.get_all_tickers()
    print(tickers)

if __name__ == "__main__":
    asyncio.run(main())
