from .db_connection import DbConnection
import pandas as pd


class Insert:
    def __init__(self):
        self.db = DbConnection()

    def insert_tiker_types(self, tiker_types: pd.DataFrame) -> None:
        """
        Insert the tiker types into the database
        :param tiker_types: DataFrame with the tiker types
        """
        query = "INSERT INTO StockTypes (Code, AssetClass, Description) VALUES (?, ?, ?)"
        for _, row in tiker_types.iterrows():
            self.db.execute_query(query, False, row["code"], row["asset_class"], row["description"])
        print("Tiker types inserted successfully")
    