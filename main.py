from core.data_loader import DataLoader
from core.backtester import Backtester
from strategies.sma_cross import SMACrossStrategy
from strategies.rsi_bb import RSIBBStrategy
from strategies.vwap_reversion import VWAPReversionStrategy

if __name__ == '__main__':
    data_loader = DataLoader()
    price_data = data_loader.load_data()

    strategies = [
        SMACrossStrategy(price_data),
        RSIBBStrategy(price_data),
        VWAPReversionStrategy(price_data),
    ]

    for strategy in strategies:
        backtester = Backtester(strategy)
        backtester.run()
        backtester.save_results()
