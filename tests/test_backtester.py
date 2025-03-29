import pandas as pd
from core.backtester import Backtester
from strategies.sma_cross import SMACrossStrategy

def test_backtester():
    df = pd.DataFrame({'Close': [1, 2, 3, 2, 5, 6, 7, 6, 9, 8]*10})
    strategy = SMACrossStrategy(df)
    backtester = Backtester(strategy)
    backtester.run()
    assert 'total_return' in backtester.metrics
