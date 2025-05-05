class WeatherData:
    def __init__(self, avg_temp, median, tempmin, tempmax):
        self.avg_temp = avg_temp
        self.median = median
        self.tempmin = tempmin
        self.tempmax = tempmax

    def to_dict(self):
        return {
            "temperature_c": {
                "average": self.avg_temp,
                "median": self.median,
                "min": self.tempmin,
                "max": self.tempmax
            }
        }