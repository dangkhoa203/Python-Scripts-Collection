import pandas as pd
from underthesea import word_tokenize
import re
data = pd.read_csv('dataset/foodtest.csv')

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

data['review'] = remove_special_character(data['review'].values)
data['review'] = data['review'].apply(lambda x: word_tokenize(x, format = 'text'))

data.to_csv("dataset/fooddatafix.csv", sep=',', encoding='utf-8',index=False)