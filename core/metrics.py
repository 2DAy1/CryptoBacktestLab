from typing import Any

def compute_metrics(stats: Any) -> dict:
    return {
        'total_return': stats.total_return,
        'sharpe_ratio': stats.sharpe_ratio,
        'max_drawdown': stats.max_drawdown,
        'win_rate': stats.win_rate,
        'expectancy': stats.expectancy,
        'exposure_time': stats.exposure_time
    }
