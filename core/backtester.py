import os
import pandas as pd
import vectorbt as vbt
from core.metrics import compute_metrics

class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy
        self.name = strategy.__class__.__name__

    def run(self) -> None:
        self.signals = self.strategy.generate_signals()
        self.results = self.strategy.run_backtest()
        self.metrics = self.strategy.get_metrics()

    def save_results(self) -> None:
        os.makedirs('results/screenshots', exist_ok=True)
        pd.DataFrame([self.metrics]).to_csv(f'results/{self.name}_metrics.csv', index=False)
        self.results.plot().write_image(f'results/screenshots/{self.name}_equity.png')
