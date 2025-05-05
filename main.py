from flask import Flask
from routes.weather_routes import setup_weather_routes
from config import Config

app = Flask(__name__)

setup_weather_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=Config.PORT)