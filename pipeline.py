import extract
import transform
import load
import os
from datetime import datetime  


def main():
    """
    Main function to run the ETL pipeline
    """
    e = extract.ClientSync()
    t = transform.Transformers()
    l = load.Insert()
    # insert ticker types into the database
    file_to_check = datetime.now().strftime('%Y-%m-%d')
    exists = False
    for file in os.listdir("data/get_all_ticker_types"):
        if file.startswith(file_to_check):
            ticker_types = extract.read_json(f"data/get_all_ticker_types/{file}")
            exists = True
            break
    if not exists:
        ticker_types = e.get_all_ticker_types()
        extract.write_json(ticker_types)
    ticker_types = t.transform_ticker_types_response(ticker_types)
    l.insert_tiker_types(ticker_types)
    # insert tickers into the database
    # tickers = e.get_all_tickers()
    # extract.write_json(tickers)
    tickers = extract.read_json("data/get_all_tickers/2024-05-05-20-42-30.json")
    tickers = t.transform_tickers_response(tickers)
    l.insert_tickers(tickers)


if __name__ == "__main__":
    main()