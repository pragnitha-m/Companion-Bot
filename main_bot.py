import random
import csv
import spacy
import pandas as pd
import numpy as np
import tkinter as tk

# load the spaCy model
nlp = spacy.load('en_core_web_sm')

def get_recipe():
    file=pd.read_csv("D:\⁮\Data Sets\\Indianfood\\IndianFoodDatasetCSV.csv", encoding='ISO-8859-1')
    food_array=np.array(file)
    name=food_array[:,0]
    ingredients=food_array[:,1]
    process=food_array[:,2]
    k=random.randint(0,6871)
    recipe_text="Recipe selected is "+name[k]+" Ingredients used are "+ingredients[k]+" Delicious steps to prepare our recipe "+process[k]
    return recipe_text

def get_stories():
    file=pd.read_csv("D:\⁮\Data Sets\\stories_me.csv", encoding='ISO-8859-1')
    story_array=np.array(file)
    title=story_array[:,1]
    story=story_array[:,2]
    k=random.randint(1,40)
    story_text="lets begin our story of "+title[k]+story[k]
    return story_text

def get_quotes():
    file=pd.read_csv("D:\⁮\Data Sets\\quotes.csv\\quotes.csv", encoding='ISO-8859-1')
    quotes_array=np.array(file)
    quote=quotes_array[:,0]
    author=quotes_array[:,1]
    #category=quotes_array[:,2]
    k=random.randint(0,6871)
    quote_text="Here's a Motivational Quote for you "+quote[k]+" written by"+author[k]
    return quote_text

# define a list of possible chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I help you today?"],
    "how are you": ["I'm doing well, thank you for asking! How are you doing?", "I'm good, thanks! How about you?"],
    "what's your name": ["My name is Companion bot. What's yours?"],
    "name response": ["Nice to meet you"],
    "status": ["Nice to hear that"],
    "recipe": [get_recipe()],
    "stories": [get_stories()],
    "quotes": [get_quotes()],
    "byee": ["Goodbye! It was nice chatting with you! see you soon"],
    "gratitude": ["You are welcome","Anytime"],
    "default": ["I'm sorry, I didn't understand that. Can you please rephrase your question?"],
}



# function to generate a response based on user input using NLP
def generate_response(user_input):
    doc = nlp(user_input)
    if any(token.text.lower() in ["bye","goodbye","quit","exit"] for token in doc):
        return random.choice(responses["byee"])

    # check if user input contains a greeting
    elif any(token.text.lower() in ["hello", "hi", "hey"] for token in doc):
        return random.choice(responses["hi"])
    
    elif any(token.text.lower() in ["thank","thanks","tnx"] for token in doc):
        return random.choice(responses["gratitude"])

    # check if user input contains a question about the chatbot's name
    elif any(token.text.lower() in ["what","your"] for token in doc):
        return random.choice(responses["what's your name"])

    elif any(token.text.lower() in ["my","name"] for token in doc):
        return random.choice(responses["name response"])

    # check if user input contains a question about how the chatbot is doing
    elif any(token.text.lower() in ["how", "doing"] for token in doc):
        return random.choice(responses["how are you"])
    
    elif any(token.text.lower() in ["am doing","well","fine","good","ok","okay"] for token in doc):
        return random.choice(responses["status"])
    
    elif any(token.text.lower() in ["recipe","cooking"] for token in doc):
    # retrieve a recipe
        return random.choice(responses["recipe"])
    
    elif any(token.text.lower() in ["story","stories"] for token in doc):
    # retrieve a story
        return random.choice(responses["stories"])
    
    elif any(token.text.lower() in ["motivational","quote","quotes","feeling","unmotivated","sad","lonely","depressed"] for token in doc):
    # retrieve a story
        return random.choice(responses["quotes"])

    # if user input doesn't match any of the above, return a default response
    else:
        return random.choice(responses["default"])
import pyttsx3
from translate import Translator
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
def TextToSpeech(text):
    translation = text
    engine.say(translation)
    engine.runAndWait()

# define a function to generate a response and display it in the chat window
def generate_and_display_response():
    # retrieve the user input from the entry field
    user_input = entry_field.get()
    
    # generate a response based on the user input
    response = generate_response(user_input)
    
    # display the response in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n\n")
    chat_window.insert(tk.END, "CompanionBot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    
    # speak the response using the text-to-speech engine
    TextToSpeech(response)
    # clear the entry field
    entry_field.delete(0, tk.END)
    
    # if the response is a goodbye message, destroy the window
    if response == "Goodbye! It was nice chatting with you! see you soon":
        window.destroy()

# define a function to create and display the chat window
def create_chat_window():
    global chat_window
    global entry_field
    
    # create the main window
    global window
    window = tk.Tk()
    window.title("CompanionBot")
    
    # create the chat window
    chat_window = tk.Text(window, state=tk.DISABLED)
    chat_window.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # create the label and entry field for user input
    input_label = tk.Label(window, text="Enter your message:")
    input_label.pack(side=tk.LEFT, padx=10, pady=10)
    entry_field = tk.Entry(window, width=50)
    entry_field.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
    
    # create the send button
    send_button = tk.Button(window, text="Send", command=generate_and_display_response)
    send_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    # bind the enter key to the send button
    window.bind('<Return>', lambda event: send_button.invoke())
    
    # run the window
    window.mainloop()

# call the function to create and display the chat window
create_chat_window()