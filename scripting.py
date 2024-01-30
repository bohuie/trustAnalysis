import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('/Users/jayati/trustAnalysis/survey-results.csv')

df['Accuracy_Rate1'] = 0.0
df['Accuracy_Rate2'] = 0.0
df['Accuracy_Rate3'] = 0.0
df['Accuracy_Rate4'] = 0.0
df['Accuracy_Rate5'] = 0.0
df['Accuracy_Rate6'] = 0.0

# Check if participants got both questions right and calculate accuracy rate
for index, row in df.iterrows():
    if row['Q78'] == 'I would remove Cam' and row['Q95'] == 'I would not remove anyone':
        df.at[index, 'Accuracy_Rate1'] = 100
    elif row['Q78'] == 'I would remove Cam' or row['Q95'] == 'I would not remove anyone':
        df.at[index, 'Accuracy_Rate1'] = 50
    
    if row['Q96'] == 'No, Minh should not move to Team 12' and row['Q97'] == 'Yes, Nia should move to Team 14':
        df.at[index, 'Accuracy_Rate2'] = 100
    elif row['Q96'] == 'No, Minh should not move to Team 12' or row['Q97'] == 'Yes, Nia should move to Team 14':
        df.at[index, 'Accuracy_Rate2'] = 50

    if row['Q84'] == 'I would not remove anyone' and row['Q100'] == 'I would remove Ray':
        df.at[index, 'Accuracy_Rate3'] = 100
    elif row['Q84'] == 'I would not remove anyone' or row['Q100'] == 'I would remove Ray':
        df.at[index, 'Accuracy_Rate3'] = 50

    if row['Q101'] == "It doesn't matter: the change is very minor and it may create other problems" and row['Q102'] == 'Yes, Tim should move to Team 18':
        df.at[index, 'Accuracy_Rate4'] = 100
    elif row['Q101'] == "It doesn't matter: the change is very minor and it may create other problems" or row['Q102'] == 'Yes, Tim should move to Team 18':
        df.at[index, 'Accuracy_Rate4'] = 50

    # Question 107 and 108
    if row['Q107'] == 'I would remove Val' and row['Q108'] == 'I would not remove anyone':
        df.at[index, 'Accuracy_Rate5'] = 100
    elif row['Q107'] == 'I would remove Val' or row['Q108'] == 'I would not remove anyone':
        df.at[index, 'Accuracy_Rate5'] = 50

    # Question 109 and 110
    if row['Q109'] == 'Yes, Rue should move to Team 12' and row['Q110'] == 'No, Sage should not move to Team 16':
        df.at[index, 'Accuracy_Rate6'] = 100
    elif row['Q109'] == 'Yes, Rue should move to Team 12' or row['Q110'] == 'No, Sage should not move to Team 16':
        df.at[index, 'Accuracy_Rate6'] = 50

    

df['Avg_Accuracy_Rate_1_2'] = df[['Accuracy_Rate1', 'Accuracy_Rate2']].mean(axis=1)
df['Avg_Accuracy_Rate_3_4'] = df[['Accuracy_Rate3', 'Accuracy_Rate4']].mean(axis=1)
df['Avg_Accuracy_Rate_5_6'] = df[['Accuracy_Rate5', 'Accuracy_Rate6']].mean(axis=1)

result_df = df[['num','Q78', 'Q95', 'Accuracy_Rate1', 'Q96', 'Q97', 'Accuracy_Rate2', 'Q84', 'Q100', 'Accuracy_Rate3',
                 'Q101', 'Q102', 'Accuracy_Rate4', 'Q107', 'Q108', 'Accuracy_Rate5', 'Q109', 'Q110', 'Accuracy_Rate6',
                 'Avg_Accuracy_Rate_1_2', 'Avg_Accuracy_Rate_3_4', 'Avg_Accuracy_Rate_5_6','team_exp_rating', 'ai_exp_rating', 'data_skill_rating']]
print(result_df)

result_df.to_csv('output_result.csv', index=False)
