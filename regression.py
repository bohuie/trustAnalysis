import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score



df = pd.read_csv('/Users/jayati/trustAnalysis/resultswcols.csv')

questions = ["Q22", "Q24", "Q25", "Q26","Q29", "Q30","Q31"]
correct_answers = [4, "Math", "No", "Yes","Team A", "Team B","Most teams seem to have a good spread of members with different majors."]
correctness_cols = []

for i, question in enumerate(questions):
    column_name = f'Q{i+1}_Correct'
    df[column_name] = df[question] == correct_answers[i]
    correctness_cols.append(column_name)

df['CorrectAnswers'] = df[correctness_cols].sum(axis=1)
print(df['CorrectAnswers'])

categories = [
    'No experience',
    'I have been assigned to teams',
    'I have formed my own teams',
    'I have helped teachers form teams in their classroom',
    'I run classes and/or other group activities where I assign people to different teams to work together',
    'I have managed activities where I put all the people present into teams'
]

for category in categories:
    df["q13_" + category.replace(" ", "_")] = df['Q13'].apply(lambda x: 1 if category in x else 0)
experience_cols = ["q13_" + category.replace(" ", "_") for category in categories]

ai_topics = [
    "search and optimization",
    "building game bots (e.g. chess)",
    "machine learning",
    "deep learning",
    "natural language processing",
    "language models",
    "training data and testing data",
    "user modeling",
    "benchmarking",
    "simulation",
    "cross-validation",
    "none of these"
]

for topic in ai_topics:
    df["q46_" + topic.replace(" ", "_")] = df['Q46'].apply(lambda x: 1 if topic in x else 0)
ai_topic_cols = ["q46_" + topic.replace(" ", "_") for topic in ai_topics]


choices = [
    "A definition of the AI approach being used.",
    "A short blurb in plain English that explains in general how the AI works.",
    "A diagram explaining how the AI arrived at its results.",
    "A detailed explanation in plain English that explains how the AI works. Some technical terms and definitions would be good as well.",
    "A scientific reference explaining how the AI works.",
    "Testimonials from other users that support the value of the AI tool.",
    "Other"
]

for choice in choices:
    df["q38_" + choice.replace(" ", "_")] = df['Q38'].apply(lambda x: 1 if choice in x else 0)
choices_cols = ["q38_" + choice.replace(" ", "_") for choice in choices]


result_df = pd.concat([df['num'], df[experience_cols], df[ai_topic_cols], df[choices_cols],df['CorrectAnswers']], axis=1)
print(result_df)

result_df.to_csv('regressionresults.csv', index=False)

resultdf = pd.read_csv('/Users/jayati/trustAnalysis/regressionresults.csv')

#Avg_Accuracy_Rate_1_2	Avg_Accuracy_Rate_3_4	Avg_Accuracy_Rate_5_6

target_variables = ['Avg_Accuracy_Rate_1_2', 'Avg_Accuracy_Rate_3_4', 'Avg_Accuracy_Rate_5_6', 'AverageOverall']

for target_variable in target_variables:
    X = pd.concat([df[experience_cols], df[ai_topic_cols], df[choices_cols], df['CorrectAnswers']], axis=1)
    y = df[target_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)

    y_pred = regr.predict(X_test)

    print(f"\nResults for {target_variable}:")
    print('Coefficients:', regr.coef_)
    print('Intercept:', regr.intercept_)
    print('Mean squared error:', mean_squared_error(y_test, y_pred))
    print('R-squared:', r2_score(y_test, y_pred))








