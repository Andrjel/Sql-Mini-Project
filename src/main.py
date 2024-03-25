from dbConnection import DbConnection
from client import ClientSync


def main():
    c = ClientSync()
    # result = c.get_all_tickers()
    # result = c.get_all_ticker_types()
    # result = c.get_grouped_daily("2024-03-22")
    # result = c.get_stock_dividend("NVDA")
    # result = c.get_aggregate_bars("MSFT", 1, "day", "2023-01-09", "2024-03-22")
    print(result)
    # c.get_all_ticker_types()


if __name__ == "__main__":
    main()
