# Tour-Guide Chatbot

## Algorithm used:
The chatbot application employs a rule-based decision-making algorithm augmented by OpenAI's GPT model for natural language understanding and response generation.

## Input Handling:
- The application accepts user input either via a web interface or an API POST request.
- It identifies whether the input is weather-related or a general query using keyword detection (e.g., checking for "weather" in the user's input).

## Decision-Making Flow:
- If the input contains the keyword "weather":
  - Extracts the location field from the request payload.
