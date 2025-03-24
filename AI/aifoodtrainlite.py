import pandas as pd
import numpy as np
import seaborn as sns
from underthesea import word_tokenize
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from tensorflow import keras
from keras.models import Model, Sequential
from keras.layers import Dense, Input, Embedding, LSTM, Dropout, BatchNormalization, Bidirectional, GRU
from tensorflow.keras.callbacks import EarlyStopping
from keras.utils import to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import regularizers
data = pd.read_csv('dataset/foodtestlite.csv')


def remove_special_character(data):
  list_txt = []
  for comment in data:
    comment = str(comment)
    comment = re.sub('\W+|http|https|www|com|COM|HTTP|HTTPS|WWW|net|NET|ORG|org', ' ', comment)
    comment = re.sub('[0-9]', ' ', comment)
    comment = re.sub('_', ' ', comment)
    comment = re.sub('(?<=\s) +|^ +(?=\s)', '', comment).strip()
    comment = comment.lower()
    list_txt.append(comment)
  return list_txt
      
data['txt'] = remove_special_character(data['review'].values)
print("Remove done")
data['txt'] = data['txt'].apply(lambda x: word_tokenize(x, format = 'text'))
list_nn = [word_tokenize(i) for i in data['txt'].values]
print("tokenize done")
num_words = 5000

tokenizer = Tokenizer(num_words = num_words,oov_token = '<OOV>')
tokenizer.fit_on_texts(list_nn)

token2seq = tokenizer.texts_to_sequences(list_nn)
padding = pad_sequences(token2seq)

x_train, x_test, y_train, y_test = train_test_split(padding,data['class'],test_size = 0.1,random_state=42,stratify=data['class'])

x_train, x_valid, y_train, y_valid = train_test_split(x_train,y_train,test_size=0.1,random_state=42,stratify=y_train)

y_train = y_train.astype(float)
y_test = y_test.astype(float)
y_valid = y_valid.astype(float)

input = Input(shape = (None, ))
x = Embedding(num_words,64)(input)
x = LSTM(32, return_sequences=False,
         kernel_regularizer=regularizers.l2(0.01))(x)
x = Dropout(0.5)(x)
output = Dense(3, activation='softmax')(x)
model = Model(input,output)
model.summary()

learning_rate = 0.01
batch_size = 64
epochs = 50
factor = 0.2

model.compile(
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy'],
    optimizer = keras.optimizers.Adam(learning_rate = learning_rate),
)

early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=7, restore_best_weights=True)
reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor= factor, patience=3, min_lr=1e-7)

H = model.fit(
    x_train, y_train, batch_size=batch_size,
    validation_data=(x_valid, y_valid),
    steps_per_epoch=x_train.shape[0] // batch_size,
    epochs = epochs,
    callbacks = [early_stopping , reduce_lr]
)

model.save("weight/foodlitenew.keras")
with open('pickle/tokenizerlite.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)