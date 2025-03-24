import pandas as pd
import re
def filterdata(string):
  
    flag=False
    if(len(string)==0):
      flag=True
    check=string.str.lower()
    if(check.__contains__("vay")):
      flag=True
    return flag

data = pd.read_csv('dataset/test.csv')

newdata=data[data["review"].str.contains("vay",na=False)==False]
newdata=newdata[newdata["review"].str.len()>35]
newdata.to_csv("dataset/newtrain.csv", sep=',', encoding='utf-8',index=False)