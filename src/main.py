from dbConnection import DbConnection
from client import Client


def main():
    c = Client()
    result = c.get_all_tickers()
    print(result)


if __name__ == "__main__":
    main()
