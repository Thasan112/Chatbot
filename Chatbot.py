from textblob import TextBlob

# Define Intents and corresponding responses
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": ["We are open from 9AM to 5 PM, Monday to Friday."]
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to assist you with the return process. Let me transfer you to a live agent."
    }
}


# Message handler
def get_response(message):
    message = message.lower()
    # Check if any keyword matches the message
    for intent in intents.values():
        if any(word in message for word in intent["keywords"]):
            return intent["response"]

    # Analyze sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity
    if sentiment > 0:
        return "That's so great to hear!"
    elif sentiment < 0:
        return "I'm so sorry to hear that. How can I help?"
    else:
        return "I see, tell me more about that?"


# Chat function
def chat():
    print("Chatbot: Hi, how can I help you today?")
    while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")


# Start the chat
chat()


