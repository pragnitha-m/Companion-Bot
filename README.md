# CompanionBot

CompanionBot is a simple chatbot created using Python and Tkinter that engages in conversations with users. The chatbot can respond to greetings, questions about its name, inquiries about its well-being, expressions of gratitude, requests for recipes, stories, and motivational boost.

## Features
- **Greeting Responses:** The chatbot responds to greetings like "Hello," "Hi," or "Hey" with friendly messages.
- **Personalized Responses:** It can handle questions about its name and provide a personalized response when the user shares their name.
- **Well-being:** The chatbot can inquire about the user's well-being and respond accordingly.
- **Recipes:** Users can request a randomly selected recipe, and the chatbot will provide the name, ingredients, and steps for preparation.
- **Stories:** Users can request a randomly selected story, and the chatbot will present a story title and its content.
- **Motivational Quotes:** Users can request a motivational quote or express their downtrodden mood, and the chatbot will share an uplifting quote along with the author.
- **Speech Responses:** Additional to text responses, the bot incorporates pyttsx3 for text-to-speech synthesis, enabling it to verbally communicate with users.

## Getting Started
1. Clone the repository to your local machine.
2. Ensure you have the required dependencies installed (`pandas`, `numpy`, `spacy`, `tkinter`, `pyttsx3`, `translate`).
3. Run the `create_chat_window()` function to start interacting with CompanionBot.

## Usage
- Enter your messages in the provided input field.
- Click the "Send" button or press "Enter" to submit your message.
- CompanionBot will respond based on the content of your input.

## Additional Information
- The chatbot uses spaCy for natural language processing (NLP) to understand and generate responses.
- Randomized responses are generated for variety, including recipes, stories, and motivational quotes.
