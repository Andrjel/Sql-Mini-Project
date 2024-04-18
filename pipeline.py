import extract
import transform


def main():
    c = extract.ClientSync()
    t = transform.Transformers()
    raw_data = c.get_all_tickers()
    extract.write_json(raw_data)
    result = t.transform_tickers_response(raw_data)
    print(result)
    # print(c.get_aggregate_bars())
    # data = t.transform_tickers_response(raw_data)


if __name__ == "__main__":
    main()