# Weather Chatbot - Initial Learning and Future Plans

## Project Overview

This project is my first step into building a chatbot using Natural Language Processing (NLP) and API integration. The chatbot can understand user input, extract city names from the conversation, and return the current weather for the given city using the OpenWeatherMap API. This was a learning experience where I explored key concepts in chatbot development, laying the groundwork for future improvements.

_This was learned and improved from [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-an-intelligent-chatbot-in-python-using-the-spacy-nlp-library)_

### Technologies Used

- **spaCy**: For Natural Language Processing (NLP) and entity recognition.
- **OpenWeatherMap API**: For retrieving weather data.
- **Python**: Backend development and logic implementation.
- **Requests Library**: For making HTTP requests to the weather API.

---

## Key Learning Milestones

### 1. Learning **spaCy** for NLP

I started by learning how to use **spaCy**, a powerful NLP library, to process and understand user input. Specifically, I used spaCy's **Named Entity Recognition (NER)** to extract city names from the input text. I also explored how spaCy can help check the similarity between sentences, allowing the chatbot to understand if a user is asking for weather information.

#### Key Concepts:

- **Tokenization**: Breaking down text into individual tokens (words).
- **Named Entity Recognition (NER)**: Identifying specific entities such as cities (GeoPolitical Entities - GPE).
- **Similarity Matching**: Using spaCy’s vector representations to compare the similarity between user input and predefined phrases (e.g., "current weather in a city").

### 2. Working with the **OpenWeatherMap API**

Once I extracted the city from the user’s query, I learned how to fetch weather data using the **OpenWeatherMap API**. This included making API calls, parsing JSON responses, and handling various response scenarios (like invalid city names or missing weather data).

#### Key Concepts:

- **API Requests**: Using the `requests` library to make HTTP GET requests to fetch data from an external API.
- **JSON Parsing**: Extracting the relevant weather data from the JSON response.
- **Error Handling**: Dealing with cases where the city is not found or other API errors occur.

### 3. Implementing **Similarity Matching**

I added a mechanism to check how similar the user's input was to a phrase like "current weather in a city". This helps the chatbot distinguish between weather-related queries and unrelated ones. If the input has a high similarity score, the chatbot proceeds to identify the city and fetch the weather.

#### Key Concepts:

- **Vector Representations of Text**: Using spaCy’s pre-trained models to convert text into vectors and compare them.
- **Threshold for Similarity**: Setting a threshold (e.g., 0.55) to determine if the user's input is weather-related. -> I intend to have a higher threshold for better accuracy

---

## Future Plans

While this project represents the beginning of my journey in chatbot development, I plan to continue improving it and adding new features.

### 1. **Improved NLP Capabilities**

I aim to expand the chatbot’s ability to understand more complex queries, such as asking for temperature, forecasts, or other weather details. Additionally, I want to refine entity recognition so that it better handles different city names, landmarks, or even regional variations.

### 2. **Contextual Conversations**

I want to implement contextual understanding in future iterations. For example, after asking for the weather in one city, the user could ask, "How about tomorrow?" and the chatbot would know they are still referring to the same city.

### 3. **Multilingual Support**

Currently, the chatbot only supports English. I plan to incorporate spaCy’s multilingual models to support users who communicate in other languages.

### 4. **Improved User Experience**

Eventually, I want to transition this project from the command line to a user-friendly web or mobile interface. This would make the chatbot easier to use and allow me to explore technologies like interactable conversations.

---

## Conclusion

This weather chatbot is an exciting first step into NLP and chatbot development. Through this project, I learned how to work with spaCy for text processing, use APIs for data retrieval, and build a basic chatbot. There’s still a lot to learn, and I’m eager to continue improving this project by expanding its capabilities and making it smarter and more useful. This is just the beginning of my journey in chatbot development, and I look forward to seeing how much further I can take it!
