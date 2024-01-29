import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy
import numpy as np

df = pd.read_csv('/Users/jayati/trustAnalysis/output_result.csv')

columns_to_convert = ['Avg_Accuracy_Rate_1_2', 'Avg_Accuracy_Rate_3_4', 'Avg_Accuracy_Rate_5_6']
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=columns_to_convert)

grouped = df.groupby(['team_exp_rating', 'ai_exp_rating', 'data_skill_rating']).agg({
    'Avg_Accuracy_Rate_1_2': ['count', 'mean', 'std'],
    'Avg_Accuracy_Rate_3_4': ['mean', 'std'],
    'Avg_Accuracy_Rate_5_6': ['mean', 'std']
}).reset_index()

grouped.columns = ['_'.join(col).strip() if col[1] else col[0] for col in grouped.columns.values]

confidence = 0.95

print(grouped.columns)

display_columns = ['team_exp_rating', 'ai_exp_rating', 'data_skill_rating']
grouped_display = grouped[display_columns]
grouped_display.columns = ['Team Experience Rating', 'AI Experience Rating', 'Data Skill Rating']

print(grouped_display)
