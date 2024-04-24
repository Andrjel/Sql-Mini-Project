import pandas as pd
import numpy as np


class Transformers:
    def __init__(self) -> None:
        pass

    def transform_tickers_response(self, response: dict) -> pd.DataFrame:
        raw_data = pd.json_normalize(response)
        return raw_data        
        # return raw_data
    
    def transform_ticker_types_response(self, response: dict) -> pd.DataFrame:
        raw_data = pd.json_normalize(response)
        raw_data.drop(["locale"], axis=1, inplace=True)
        raw_data["code"] = raw_data["code"].str.upper()
        return raw_data
        # return raw_data
