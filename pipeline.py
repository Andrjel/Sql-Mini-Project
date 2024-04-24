import extract
import transform


def main():
    e = extract.ClientSync()
    t = transform.Transformers()
    raw_data = extract.read_json("data/get_all_ticker_types/2024-04-24.json")
    result = t.transform_ticker_types_response(raw_data)  
    print(result.info())


if __name__ == "__main__":
    main()