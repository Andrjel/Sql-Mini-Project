import pandas as pd
import numpy as np


class Transformers:
    def __init__(self) -> None:
        pass

    def transform_tickers_response(self, response: dict) -> pd.DataFrame:
        raw_data = pd.json_normalize(response)
        return raw_data        
        # return raw_data
