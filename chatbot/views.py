# chatbot/views.py
import random
import os
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from django.shortcuts import render
from django.http import JsonResponse

# Obtén la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Actualiza la carga del archivo intents.json
intents_path = os.path.join(current_dir, 'intents.json')
intents = json.loads(open(intents_path).read())

lemmatizer = WordNetLemmatizer()

#Importamos los archivos generados en el código anterior
words = pickle.load(open(os.path.join(current_dir, 'words.pkl'), 'rb'))
classes = pickle.load(open(os.path.join(current_dir, 'classes.pkl'), 'rb'))
model = load_model(os.path.join(current_dir, 'chatbot_model.h5'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res == np.max(res))[0][0]
    category = classes[max_index]
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            break
    return result

def ChatPage(request):
    return render(request, 'chatbot/chat.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    # Predict the class and get a response
    tag = predict_class(userMessage)
    response = get_response(tag, intents)
    return JsonResponse({'botResponse': response})
