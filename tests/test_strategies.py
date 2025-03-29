import pytest
import pandas as pd
from strategies.sma_cross import SMACrossStrategy

def test_sma_cross():
    df = pd.DataFrame({'Close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10})
    strategy = SMACrossStrategy(df)
    signals = strategy.generate_signals()
    assert isinstance(signals, pd.Series)
