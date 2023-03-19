import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from language_tool_python import LanguageTool
from langdetect import detect_langs
import pandas as pd
import re

# download nltk resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Define language tool
tool = LanguageTool('en-US')

def get_website(tld):
    # URL to scrape
    url = "https://"+tld
    print(url)
    html_code = requests.get(url, timeout=15).text
    return html_code

def clean(html_code):
  soup = BeautifulSoup(html_code, 'html.parser')
  text = soup.get_text()
  text = re.compile(r"\s+").sub(" ",text).strip().lower()
  text = re.sub('[^a-z ]','',text)
  text = text.split()
  stop_words = set(stopwords.words('english'))
  filtered_words = [word for word in text if word.isalpha() and word.lower() not in stop_words]
  filtered = [word for word in filtered_words if len(word) >= 4 and len(word) <= 12]
  no_duplicate = list(set(filtered))
  words = [word for word in no_duplicate if not tool.check(word)]
  words_list = [word for word in filtered if word in words]
  line = ""
  for txt in words_list:
      line += txt + " "
  line=line.strip()    
  return line

csv_path = "Dataset/training_dataset.xlsx"
df_websites = pd.read_excel(csv_path, usecols=["tld","industry"]) 
categories = list(set([category for category in df_websites['industry'] if '[' not in category and category != '']))
df_websites= df_websites[df_websites.industry.isin(categories)]
cat = []
words=[]
for tld, industry in df_websites.itertuples(index=False):
    try:
        html_code=get_website(i,tld)
    except: 
        continue
    line=clean(html_code)
    if not(line == ""):
        words.append(line) 
        cat.append(industry)
df_results = pd.DataFrame({'Category':list(cat), 'Cleaned':list(words)},columns=['Category','Cleaned'])
df_results.to_csv('cleaned.csv')