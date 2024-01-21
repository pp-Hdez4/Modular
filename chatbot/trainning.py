import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

from keras.preprocessing.sequence import pad_sequences

from keras.models import Sequential
from keras.layers import Dense

from keras.optimizers import SGD




#Pasar por un lematizador el archivo de intents.json para convertirlo en una matriz de 1 y 0 para que la red neuronal lo entienda
lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        print("Pattern:", pattern)
        word_list = nltk.word_tokenize(pattern)
        # Resto del código...

        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)

# Obtener las listas separadas para las entradas y las etiquetas
X = np.array([i[0] for i in training])
y = np.array([i[1] for i in training])

# Utilizar pad_sequences para igualar las longitudes de las secuencias
X_padded = pad_sequences(X)

# Ahora puedes imprimir X_padded para verificar la forma
print(X_padded)

#Reparte los datos para pasarlos a la red
train_x = np.array([i[0] for i in training])
train_y = np.array([i[1] for i in training])

#Creamos la red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

#Creamos el optimizador y lo compilamos
sgd = SGD(learning_rate=0.001, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])

#Entrenamos el modelo y lo guardamos
train_process = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=5, verbose=1)
model.save("chatbot_model.h5", train_process)