from flask import Flask, request, jsonify, render_template
import openai
import requests
from amadeus import Client, ResponseError

# Initialize Flask app
app = Flask(__name__)

# Set your API keys
openai.api_key = "sk-OD1YjOk7TRRiWK7BQb7z_Q2dFTqRsnlFx8NMb81bnYT3BlbkFJlYnsArIDMiBoWQukczgezQJzR91PmYOmQ0ZZMili4A"
weather_api_key = "52274ddab19670d29220b4736690e5af"
amadeus_client_id = "fLXG5B2mFsSXonhm73Hst3ofaGcw1Mv6"
amadeus_client_secret = "fE00hkxrKBBiJlYY"

# Initialize Amadeus API client
amadeus = Client(
    client_id=amadeus_client_id,
    client_secret=amadeus_client_secret
)

# Function to get chatbot responses using OpenAI
def chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful tour guide chatbot. You can provide tour costs, weather information, and travel recommendations."},
                {"role": "user", "content": user_input},
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# Function to fetch weather information
def get_weather(location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if weather_data["cod"] == 200:
            city = weather_data["name"]
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            return f"The current weather in {city} is {temp}°C with {description}."
        else:
            return "I couldn't find weather information for that location. Please check the city name."
    except Exception as e:
        return f"Error: {e}"

# Function to fetch flight cost using Amadeus API
def get_flight_cost(origin, destination, departure_date, return_date=None):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            returnDate=return_date,
            adults=1
        )
        flights = response.data

        if flights:
            first_flight = flights[0]
            price = first_flight['price']['total']
            airline = first_flight['validatingAirlineCodes'][0]
            return f"The cheapest flight from {origin} to {destination} costs ${price} (Airline: {airline})."
        else:
            return "No flights found for the given route and dates."
    except ResponseError as e:
        return f"Error fetching flight cost: {e}"

# Route for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input")
    if "weather" in user_input.lower():
        location = request.json.get("location")
        result = get_weather(location)
    elif "flight cost" in user_input.lower():
        origin = request.json.get("origin")
        destination = request.json.get("destination")
        departure_date = request.json.get("departure_date")
        return_date = request.json.get("return_date")
        result = get_flight_cost(origin, destination, departure_date, return_date)
    elif "tour cost" in user_input.lower():
        result = "The average cost of a guided city tour is $50 per person. For customized packages, please contact your local tour operator."
    else:
        result = chatbot_response(user_input)

    return jsonify({"response": result})

# Route for frontend
@app.route("/")
def index():
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
