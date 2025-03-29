import os
import pandas as pd
from pathlib import Path
from typing import Literal

class DataLoader:
    def __init__(self, data_path: str = 'data/btc_1m_feb25.parquet', cache: bool = True):
        self.data_path: str = data_path
        self.cache: bool = cache

    def load_data(self) -> pd.DataFrame:
        if self.cache and Path(self.data_path).exists():
            return pd.read_parquet(self.data_path)
        df = self.download_data()
        df.to_parquet(self.data_path, compression='snappy')
        return df

    def download_data(self) -> pd.DataFrame:
        from vectorbt.data.custom import BinanceData
        df = BinanceData.fetch(
            symbols='BTC/USDT',
            timeframe='1m',
            start='2025-02-01 UTC',
            end='2025-03-01 UTC',
            tz='UTC',
            include_columns=['Open', 'High', 'Low', 'Close', 'Volume'],
            multi_index=True
        )
        return df
