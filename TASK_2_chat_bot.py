# Import required modules from NLTK
import nltk
from nltk.chat.util import Chat, reflections

# Create a list of patterns and responses
# These are regular expressions to match user input
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]  # %1 matches the name captured by (.*)
    ]

],
[
    r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!"]  # Greeting responses
    ],
[
        r"what is your name?",
["You can call me ChatBot.", "I'm a friendly chatbot."]  # Bot's name
    ],
[
        r"how are you?",
        ["I'm doing good. How about you?", "I'm great, thanks for asking!"]  # Small talk
    ],
[
r"sorry (.*)",
        ["No problem", "It's okay", "Don't worry about it."]  # Response to apologies
    ],
[
    r"quit",
        ["Bye! Have a nice day.", "Goodbye!"]  # Exit response
    ]


# Create a function to initiate the chatbot
def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to quit.")  # Greeting message

    # Initialize a Chat object with the pairs and reflections
    chat = Chat(pairs, reflections)

    # Begin the conversation loop
    chat.converse()

# Call the chatbot function
chatbot()