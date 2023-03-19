import pandas as pd
import numpy as np
from clean import get_website, clean

frequencies = pd.read_csv("frequencies.csv") 
denominator = pd.read_csv("denominator.csv") 
prior = pd.read_csv("prior.csv") 

def classify(url):
    try:
        html_code=get_website(url)
        cleaned = clean(html_code)
        categories = prior['Category']
        data = np.array([cleaned.split(), np.repeat(categories, len(words))]).T
        to_compute = pd.DataFrame(data, columns=['Word', 'Category'])
        to_compute = to_compute.merge(frequencies, on=['Word','Category'], how='left')
        to_compute.fillna(0, inplace=True)
        to_compute.rename(columns={'Count':'Probability'}, inplace=True)
        # add 1 to all values to make sure that none of them 0
        to_compute['Probability'] = to_compute['Probability'] + 1
        to_compute = to_compute.drop('Word', axis=1)
        # divide the values in probability by the denominator
        to_compute = to_compute.merge(denominator, on='Category', how='left')
        to_compute['Probability'] = to_compute['Probability']/to_compute['Total Number']
        to_compute = to_compute.drop(columns=['Total Number'])      
        to_compute = to_compute.groupby('Category').prod()
        # multiply each value by the prior probability
        naive_bayes = pd.merge(to_compute, prior, on='Category')
        naive_bayes['Product'] = naive_bayes['Prior'] * naive_bayes['Probability']
        naive_bayes.drop(['Probability','Prior'], axis=1, inplace=True)
        print(naive_bayes)
        max_category = naive_bayes.loc[naive_bayes['Product'].idxmax(), 'Category']
        return max_category
    except:
        return "error in url"

# define the test data frame
df_test = pd.read_excel('Dataset/testing_dataset.xlsx', usecols = ['tld', 'industry'])
# creating a new column 'predicted' and applying classify function to tld column
df_test['predicted'] = df_test['tld'].apply(classify)
df_test = df_test[df_test['predicted'] != "error in url"]
# Save the results to a csv file
df_test.to_csv('results.csv', index=False)

# Get a list of all the unique categories
categories = df_test['Category'].unique()
# Create a dictionary to store the results
results = {'Category': [], 'Accuracy': [], 'Precision': [], 'Recall': [], 'F1-Score': []}
# Iterate through each category
for category in categories:
    # Get the subset of the data for the current category
    subset = df_test[df_test['Category'] == category]
    # Compute the number of true positives
    true_positives = (subset['Category'] == subset['Predicted']).sum()
    # Compute the number of false positives
    false_positives = ((subset['Category'] != subset['Predicted']) & (subset['Predicted'] == category)).sum()
    # Compute the number of true negatives
    true_negatives = ((subset['Category'] != subset['Predicted']) & (subset['Predicted'] != category)).sum()
    # Compute the number of false negatives
    false_negatives = ((subset['Category'] == subset['Predicted']) & (subset['Predicted'] != category)).sum()
    # Compute accuracy, precision, recall and f1-score
    accuracy = (true_positives + true_negatives) / len(subset)
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1_score = 2 * (precision * recall) / (precision + recall)
    # Append the results to the dictionary
    results['Category'].append(category)
    results['Accuracy'].append(accuracy)
    results['Precision'].append(precision)
    results['Recall'].append(recall)
    results['F1-Score'].append(f1_score)

# Create a dataframe from the results dictionary
elements = pd.DataFrame(results)

