import pandas as pd
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('punkt')

def concatenate_strings(group):
    return ' '.join(group['Cleaned'].astype(str).tolist())

def count_words(group):
    return len(group['Cleaned'].str.split().sum())

df_cleaned = pd.read_csv("Cleaned.csv", usecols = ['Cleaned','Category'])
df_cleaned['Cleaned'] = df_cleaned['Cleaned'].str.split()
# create a new DataFrame with the words and their categories
df_result = df_cleaned.explode('Cleaned')
# count the number of occurrences of each word
frequencies = df_result.groupby(['Category','Cleaned']).size().reset_index(name='Count')
frequencies.columns = ['Category', 'Word', 'Count']
# create a new DataFrame that has the category and the sum of the counts next to it
denominater = frequencies.groupby('Category')['Count'].sum().reset_index()
# Get Vocabulary of all classes
vocabulary = len(list(set(frequencies['Word'])))
denominater.columns = ['Category', 'Total Number']
denominater['Total Number'] = denominater['Total Number'] + vocabulary
# Get Prior probability
df = pd.read_excel("/content/training_dataset.xlsx")
industry_list = df['industry'].tolist()
counts = Counter(industry_list)
df_prior = pd.DataFrame(columns=["Category", "Prior"])
for category, count in counts.items():
    prior = count / len(industry_list)
    df_prior = df_prior.append({"Category": category, "Prior": prior}, ignore_index=True)

frequencies.to_csv('frequencies.csv')
denominater.to_csv('denominater.csv')
df_prior.to_csv('prior.csv')
