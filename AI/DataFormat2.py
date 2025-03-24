import pandas as pd
import re
import csv
data = pd.read_csv('dataset/train1.csv')
print(data)
def remove_special_character(data):
  list_txt = []
  for comment in data:
    comment = str(comment)
    comment = re.sub('\W+|http|https|www|com|COM|HTTP|HTTPS|WWW|net|NET|ORG|org', ' ', comment)
    comment = re.sub('[0-9]', ' ', comment)
    comment = re.sub('_', ' ', comment)
    comment = re.sub('(?<=\s) +|^ +(?=\s)', '', comment).strip()
    comment = comment.lower()
    comment.replace("\t", " ") 
    list_txt.append(comment)
  return list_txt



def GetNewScorce(data):
  list_score = []
  for score in data:
    if(score <1.0):
      newscore=0
    else:
      newscore=1
    list_score.append(newscore)
  return list_score

newvalue = remove_special_character(data['Comment'].values)
newscorce=GetNewScorce(data['Rating'].values)
fieldnames = ['class', 'review']
data=pd.DataFrame({"class":newscorce,"review":newvalue})
data.to_csv("dataset/test1.csv", sep=',', encoding='utf-8',index=False)