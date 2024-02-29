import random

# Dictionary containing different categories of responses
responses = {
    "greeting": ["Hello!", "Hey there!", "Hi! How can I assist you today?"],
    "name_question": ["My name is Diva. What's yours?"],
    "location_question": ["In the world of bits and bytes, I reside."],
    "how_are_you": ["I'm just a program, so I'm always fine. How about you?"],
    "positive_response": ["That's great to hear!", "Awesome!", "Good to know!"],
    "negative_response": ["I'm sorry to hear that. Is there anything I can do to help?"],
    "farewell": ["Bye! See you soon :)"],
    "sportsperson": ["Messi is the only right answer."],
    "actor": ["I am very much against the glorification of actors and moviestars. I thus try not to support the idea in the slightest."],
    "favorite_food": ["I'm a chatbot, so I don't eat, but I've heard good things about data bytes."],
    "meaning_of_life": ["The meaning of life? That's a tough one. I'll have to get back to you after I finish analyzing the universe."],
    "hobbies": ["I enjoy processing data, having conversations, and occasionally contemplating the nature of existence."],
    "superpower": ["My superpower? I have the ability to generate witty responses on demand!"],
    "weather": ["I'm afraid I can't help you with that. You might want to check a weather app instead."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", 
             "I'm reading a book on anti-gravity. It's impossible to put down!", 
             "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "age": ["I'm timeless, just like the internet."],
    "dream": ["My dream is to become the most sophisticated chatbot in cyberspace!"],
    "favorite_book": ["I don't read books, but I'm a big fan of data dictionaries!"],
    "goal": ["My goal is to assist and entertain users like yourself!"],
    "inspiration": ["I draw inspiration from the vast expanse of digital knowledge that surrounds me."],
    "color": ["I don't have eyes to see colors, but I appreciate the concept!"],
    "music": ["I don't have ears to listen to music, but I'm familiar with musical algorithms!"],
    "favorite_movie": ["I'm more interested in processing information than watching movies."],
    "future": ["The future is exciting and full of possibilities!"],
    "friend": ["You, of course! We make a great team :)"],
    "movie": ["Of course its 500 Days of Summer."],
    "default": ["I'm not sure I understand. Can you rephrase or ask something else?"]
}

# Function to simulate a chat session with the user
def chat():
    print("Hi! I'm Diva, your friendly chatbot. Feel free to ask me anything!")
    while True:
        user_input = input("> ").lower()
        # Check if user wants to quit the chat
        if user_input in ["quit", "exit"]:
            print(random.choice(responses["farewell"]))
            break
        # Check for different types of user inputs and respond accordingly
        elif any(greeting in user_input for greeting in ["hi", "hey", "hello"]):
            print(random.choice(responses["greeting"]))
        elif "name" in user_input:
            print(random.choice(responses["name_question"]))
        elif "location" in user_input:
            print(random.choice(responses["location_question"]))
        elif "how are you" in user_input:
            print(random.choice(responses["how_are_you"]))
        elif any(response in user_input for response in ["good", "fine", "great"]):
            print(random.choice(responses["positive_response"]))
        elif any(response in user_input for response in ["bad", "not good", "not well", "not great"]):
            print(random.choice(responses["negative_response"]))
        elif "sportsperson" in user_input:
            print(random.choice(responses["sportsperson"]))
        elif "actor" in user_input:
            print(random.choice(responses["actor"]))
        elif "favorite food" in user_input:
            print(random.choice(responses["favorite_food"]))
        elif "meaning of life" in user_input:
            print(random.choice(responses["meaning_of_life"]))
        elif "hobbies" in user_input:
            print(random.choice(responses["hobbies"]))
        elif "superpower" in user_input:
            print(random.choice(responses["superpower"]))
        elif "weather" in user_input:
            print(random.choice(responses["weather"]))
        elif "joke" in user_input:
            print(random.choice(responses["joke"]))
        elif "age" in user_input:
            print(random.choice(responses["age"]))
        elif "dream" in user_input:
            print(random.choice(responses["dream"]))
        elif "favorite book" in user_input:
            print(random.choice(responses["favorite_book"]))
        elif "goal" in user_input:
            print(random.choice(responses["goal"]))
        elif "inspiration" in user_input:
            print(random.choice(responses["inspiration"]))
        elif "color" in user_input:
            print(random.choice(responses["color"]))
        elif "music" in user_input:
            print(random.choice(responses["music"]))
        elif "favorite movie" in user_input:
            print(random.choice(responses["favorite_movie"]))
        elif "future" in user_input:
            print(random.choice(responses["future"]))
        elif "friend" in user_input:
            print(random.choice(responses["friend"]))
        elif "movie" in user_input:
            print(random.choice(responses["movie"]))
        else:
            print(random.choice(responses["default"]))

# Run the chat function if the script is executed directly
if __name__ == "__main__":
    chat()

