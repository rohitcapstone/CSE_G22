# Tour-Guide Chatbot

## Algorithm used:
The chatbot application employs a rule-based decision-making algorithm augmented by OpenAI's GPT model for natural language understanding and response generation.

## Input Handling:
- The application accepts user input either via a web interface or an API POST request.
- It identifies whether the input is weather-related or a general query using keyword detection (e.g., checking for "weather" in the user's input).

## Decision-Making Flow:
- Weather-Related Queries:
  - If the input contains the keyword "weather":
    - Extracts the location field from the request payload.
    - Calls the get_weather() function to fetch weather data from the OpenWeatherMap API.
    - If the location is missing, it prompts the user to provide one.
- General Queries:
  - If the input does not relate to weather:
    - Passes the user's input to the chatbot_response() function.
    - This function sends the input to the OpenAI API to generate a contextually relevant response based on the conversation setup.

## Weather Information Retrieval:
The get_weather() function follows these steps:
- API Request:
  - Constructs a URL with the location and API key to query the OpenWeatherMap API.
  - url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
- Response Parsing:
  - Parses the JSON response from the API to extract:
    - City name
    - Temperature (in Celsius)
    - Weather description
- Error Handling:
  - Handles cases where:
    - The location is invalid.
    - The API resquest fails.

## ChatBot Response Generation:
The chatbot_response() function follows these steps:
- API Request to OpenAI GPT:
  Sends the user input to the OpenAI GPT model using the openai.ChatCompletion.create() method with a system role and conversation history:
  - response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful tour guide chatbot..."},
        {"role": "user", "content": user_input},
    ]
)
