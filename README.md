# Sectorization
Sectorization is a Python project that aims to classify websites into different sectors. It contains several modules that perform different tasks, such as cleaning, feature engineering, and classification. Sectorization is an NLP based project that I built during my free time and before I took the NLP course, so the techniques used may not be the most advanced or optimal. However, I hope that this project can still be useful for learning and experimentation with NLP techniques for websites classification. If you have any suggestions or feedback for improving the project, please feel free to contribute. I implemented the code from scratch and I chose the Naive-Bayes classifies as my model which is a program I wrote without using a pre-built model just to practice more of what I learned from my Machine Learning course.

# Installation
To use Sectorization, you need to install Python 3.8 and some additional packages. You can install these packages using pip, as follows:
`pip install -r requirements.txt`

# Usage
Sectorization is composed of several Python files, each with a specific purpose:
1. website_count.py: This module contains a code that displays the categories I have in my dataset and their frequency.
2. clean.py: This module contains functions to request the HTML for the websites in my dataset and clean their context.
3. feature_engineering.py: This module contains functions for generating the Bag of Words of each category.
4. test.py: This module contains the Naive-Bayes classifier as function, and it classifies the test dataset and evaluates the scoring.
5. tool.py: This module contains a GUI application that takes a URL as input and displays the predicted sector based on the trained model.

To use the GUI application, simply run the following command:

# Contributing
If you'd like to contribute to Sectorization, please follow these guidelines:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Write tests for your changes to ensure that they work as expected.
3. Submit a pull request and describe your changes in detail.

# Acknowledgments
Thanks to the developers of the Python libraries used in this project.
We would like to acknowledge the help of our colleagues in providing feedback and suggestions during the development of this project.
