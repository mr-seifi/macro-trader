from . import BaseAnalyst


class EOTSAnalyst(BaseAnalyst):
    """
        EOT Analyst stands for End-Off-Tightening-Stagflation.
            Following up the title of strategy, it's totally clear Fed's monetary policies are too Hawkish since
        High Inflation thus so many companies are going to be bankrupt, and the global economic is bear the pressure
        United States Tightening.
            Strategies in this class must be in the way of recession since recession makes Fed more sensitive about
        economic conditions.
    """
    def __init__(self):
        super().__init__()
        self._filter = {'UNITEDSTAREDIND': self.STRATEGY_CHANGED_HIGHER_THAN_PRICED}
