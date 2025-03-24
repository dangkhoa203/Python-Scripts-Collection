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

class TokenLayer:
   def __init__(self):
        with open('pickle/tokenizerlite.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
   def GetSequence(self,sample):
        sample_new=remove_special_character([sample])
        sample_new = word_tokenize(sample_new[0],format="text")
        sample_new=word_tokenize(sample_new)
        seq = self.tokenizer.texts_to_sequences(sample_new)
        padding = pad_sequences(seq)
        return padding

     
class MyModel:
   def __init__(self):
    self.tokenlayer=TokenLayer()
    self.model=keras.models.load_model('weight/foodlite.keras')
    self.label={
      0: 'xấu',
      1: 'tốt',
    }
    
    

   def get_test(self,sample):
    padding=self.tokenlayer.GetSequence(sample)
    y_pred = self.model.predict(padding)
    y_pred = np.argmax(y_pred, axis = -1)
    leng=len(y_pred)
    total=sum(y_pred)

    avg=total/leng
    print("Số diểm: ",avg)
    y_pred = self.label[round(avg)]
    #print('{} - Predicted: {}'.format(sample,y_pred))
    return y_pred

   
def App():
  model=MyModel()
  flag=True
  print("Hãy nhập Review để nhận xét")
  while(flag==True):
      human_response = input('Enter review : ')
      if human_response.lower() != 'quit' and human_response.lower() != 'q':
          try:
              print('Kết quả: ' + model.get_test(human_response))
          except:
              print("Lỗi xảy ra")
      else:
          flag=False
          print("Đóng ứng dụng")

if __name__ == '__main__':
    App()