import pandas as pd
import requests
from django.conf import settings


class DailyFxCollector:

    def __init__(self):
        self._events_endpoint = settings.COLLECTOR_DAILYFX_EVENTS_ENDPOINT
        self._proxy = bool(settings.PROXY)
        self._proxy_config = settings.PROXY_URL
        self._timezone = settings.TIME_ZONE

    @property
    def proxy(self):
        if not self._proxy:
            return {}
        return {'proxies': {'http': self._proxy_config,
                            'https': self._proxy_config}}

    def get_events(self, **kwargs) -> pd.DataFrame:
        response = requests.get(self._events_endpoint, **self.proxy).json()['calendarEvents']

        df = pd.DataFrame(response)

        # Apply filters
        for key in kwargs:
            df = df[df[key] == kwargs[key]]

        # Apply timezone
        df['date'] = pd.to_datetime(df['date'], utc=True)
        df.index = df.pop('date')
        df = df.tz_convert(self._timezone)

        return df
