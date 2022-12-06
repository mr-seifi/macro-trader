from analyst.exceptions import StrategyNotFound


class BaseAnalyst:

    def __init__(self):
        self.STRATEGY_CHANGED_LOWER_THAN_PRICED = 'CLTP'
        self.STRATEGY_CHANGED_HIGHER_THAN_PRICED = 'CHTP'
        self._filters = {}

    def add_strategy(self, ticker: str, strategy: str):
        if strategy not in (self.STRATEGY_CHANGED_LOWER_THAN_PRICED,
                            self.STRATEGY_CHANGED_HIGHER_THAN_PRICED):
            raise StrategyNotFound
        self._filters[ticker] = strategy
