import requests

alerts = {"HUR" : "Hurricane Local Statement",
    "TOR": "Tornado Warning",
    "TOW": "Tornado Watch",
    "WRN": "Severe Thunderstorm Warning",
    "SEW": "Severe Thunderstorm Watch",
    "WIN": "Winter Weather Advisory",
    "FLO": "Flood Warning",
    "WAT": "Flood Watch / Statement",
    "WND": "High Wind Advisory",
    "SVR": "Severe Weather Statement",
    "HEA": "Heat Advisory",
    "FOG": "Dense Fog Advisory",
    "SPE": "Special Weather Statement",
    "FIR": "Fire Weather Advisory",
    "VOL": "Volcanic Activity Statement",
    "HWW": "Hurricane Wind Warning",
    "REC": "Record Set",
    "REP": "Public Reports",
    "PUB": "Public Information Statement",
}

class ZipCode():
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.weather_info = False
        self.current_conditions = False
        self.forecast = False
        self.sunrise = False
        self.sunset = False
        self.weather_alert = False
        self.hurricane_alert = False
        self.location = False

    def get_base_url(self):
        return 'http://api.wunderground.com/api/785718799666cf26'

    def retrieve_weather_info(self):
        if not self.weather_info:
            url = self.get_base_url() + '/conditions/forecast10day/astronomy/alerts/currenthurricane/q/{}.json'.format(self.zip_code)
            weather_info = requests.get(url)
            self.weather_info = weather_info.json()
        return self.weather_info

    def check_current_conditions(self):
        if not self.current_conditions:
            self.current_conditions = self.retrieve_weather_info()['current_observation']['temp_f']
        return self.current_conditions


    def check_forecast(self):
        if not self.forecast:
            self.forecast = self.retrieve_weather_info()['forecast']['simpleforecast']['forecastday']
        return self.forecast


    def check_sunrise_sunset(self):
        if not self.sunrise:
            self.sunrise = self.weather_info['sun_phase']['sunrise']
        if not self.sunset:
            self.sunset = self.weather_info['sun_phase']['sunset']
        return self.sunrise, self.sunset


    def check_weather_alerts(self):
        try:
            if not self.weather_alert:
                self.weather_alert = self.weather_info['alerts'][0]['type']
        except:
            pass

        return self.weather_alert

    def check_for_hurricanes(self):
        if not self.hurricane_alert:
            self.hurricane_alert = self.weather_info['currenthurricane']

            if not self.hurricane_alert:
                    print("No hurricanes to report...FOR NOW.")

        return self.hurricane_alert
