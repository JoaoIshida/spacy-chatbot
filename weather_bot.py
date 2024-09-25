import spacy
import requests
import os
from dotenv import load_dotenv

nlp = spacy.load("en_core_web_md")

# api key from env
load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather(city):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

    response = requests.get(api_url)
    response_dict = response.json()

    if response.status_code == 200:
        if "weather" in response_dict:
            weather = response_dict["weather"][0]["description"]
            return weather
        else:
            return "Error: 'weather' information not found in the response."
    else:
        print(f'[!] HTTP {response.status_code} calling [{api_url}]')
        print(f"Error message: {response_dict.get('message', 'No additional information')}")
        return None

def chatbot(statement):
    # This variable will be used to check similarity with the input statement
    weather_query = nlp("current weather in a city") 
    statement_nlp = nlp(statement)
    min_similarity = 0.55

    print(weather_query.similarity(statement_nlp))
    if weather_query.similarity(statement_nlp) >= min_similarity:
        city = None
        for ent in statement_nlp.ents:
            if ent.label_ == "GPE":  # GeoPolitical Entity
                city = ent.text
                break
        
        if city:  # Only if a city was found
            city_weather = get_weather(city)
            if city_weather is not None:
                return "In {} the weather is: {}".format(city, city_weather)
            else:
                return "Something went wrong"
        else:
            return "You need to tell me a city to check."
    else:
        return "Sorry, I don't understand that. Please rephrase your statement."

response = chatbot("what's the weather in Rome today?")
print(response)
