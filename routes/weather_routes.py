from flask import request, Response
from services.weather_service import WeatherService

def setup_weather_routes(app):
    @app.route("/info")
    def return_info():
        return {
            "version": "0.1.0",
            "service": "weather",
            "author": "a.chepenkov"
        }

    @app.route("/info/weather")
    def return_weather():
        try:
            args = request.args.to_dict()
            city = args.get("city", "")
            date_from = args.get("date_from")
            date_to = args.get("date_to")
            
            weather_service = WeatherService()
            weather_data = weather_service.get_weather(city, date_from, date_to)
            return {
                "data": weather_data.to_dict(),
                "service": "weather"
            }
        except Exception as e:
            return Response(e, status=500, content_type='application/json')
