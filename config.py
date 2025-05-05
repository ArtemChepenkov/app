import os

class Config:
    VERSION = os.getenv("VERSION", default="0.1.0")
    SERVICE = "weather"
    AUTHOR = "a.chepenkov"
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    API_KEY = os.getenv("API_KEY")
    PORT = os.getenv("PORT", default=5000)