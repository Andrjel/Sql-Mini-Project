import extract.client


def main():
    c = extract.client.ClientSync()
    print(c.get_all_tickers())
    # print(c.get_aggregate_bars())


if __name__ == "__main__":
    main()