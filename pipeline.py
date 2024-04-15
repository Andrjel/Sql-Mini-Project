import extract
import transform


def main():
    c = extract.ClientSync()
    print(c.get_all_tickers())
    # print(c.get_aggregate_bars())
    t = transform.Transformers()


if __name__ == "__main__":
    main()