import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

csv_path = "Dataset/training_dataset.xlsx"

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:        
        return ''

df_websites = pd.read_excel("{}".format(csv_path), usecols=["tld","industry"], converters={'tld': convert_dtype,'industry': convert_dtype})

categories = [category for category in df_websites['industry'] if '[' not in category]
categories = set(filter(None, categories))
print(categories)

df_filtered = df_websites[df_websites["industry"].isin(categories)]
df_remaining = df_websites[~df_websites["industry"].isin(categories)]

counted = Counter(df_filtered["industry"])
counted.update({"Multilabel":len(df_remaining), "Blank":len([cell for cell in df_websites['industry'] if cell == ''])})
bar = plt.bar(counted.keys(), counted.values(), 0.5)
plt.bar_label(bar)
plt.xlabel('Categories')
plt.ylabel('Number of Websites')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
