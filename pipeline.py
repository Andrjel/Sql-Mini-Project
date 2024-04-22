import extract
import transform


def main():
    # c = extract.ClientSync()
    t = transform.Transformers()
    # raw_data = c.get_all_tickers()
    # extract.write_json(raw_data)
    # result = t.transform_tickers_response(raw_data)
    # print(result)
    raw_data = extract.read_json("data/2024-04-19/18-54-07.json")
    result = t.transform_tickers_response(raw_data)
    print(result.head())
    




if __name__ == "__main__":
    main()