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

