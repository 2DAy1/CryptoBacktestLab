import vectorbt as vbt
import pandas as pd
from strategies.base import StrategyBase
from core.metrics import compute_metrics

class VWAPReversionStrategy(StrategyBase):
    def generate_signals(self) -> pd.DataFrame:
        vwap = self.price_data['Close'].rolling(20).mean()
        entries = self.price_data['Close'] < (vwap * 0.97)
        exits = self.price_data['Close'] > vwap
        self.entries = entries
        self.exits = exits
        return entries

    def run_backtest(self) -> pd.DataFrame:
        pf = vbt.Portfolio.from_signals(
            close=self.price_data['Close'],
            entries=self.entries,
            exits=self.exits,
            fees=0.001,
            slippage=0.001
        )
        self.stats = pf.stats()
        return pf

    def get_metrics(self) -> dict:
        return compute_metrics(self.stats)
