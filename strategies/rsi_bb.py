import vectorbt as vbt
import pandas as pd
from strategies.base import StrategyBase
from core.metrics import compute_metrics

class RSIBBStrategy(StrategyBase):
    def generate_signals(self) -> pd.DataFrame:
        rsi = vbt.IndicatorFactory.from_pandas_ta('rsi', length=14).run(self.price_data['Close']).output
        bb = vbt.IndicatorFactory.from_pandas_ta('bbands', length=20).run(self.price_data['Close'])
        entries = (rsi < 30) & (self.price_data['Close'] < bb.lower)
        exits = rsi > 50
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
