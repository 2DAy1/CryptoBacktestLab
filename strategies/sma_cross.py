import vectorbt as vbt
import pandas as pd
from strategies.base import StrategyBase
from core.metrics import compute_metrics

class SMACrossStrategy(StrategyBase):
    def generate_signals(self) -> pd.DataFrame:
        fast = vbt.IndicatorFactory.from_pandas_ta('sma', length=20).run(self.price_data['Close']).output
        slow = vbt.IndicatorFactory.from_pandas_ta('sma', length=50).run(self.price_data['Close']).output
        entries = fast > slow
        exits = fast < slow
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
