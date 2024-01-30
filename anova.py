import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('/Users/jayati/trustAnalysis/output_result.csv')

df['Avg_Accuracy_Rate_1_2'] = pd.to_numeric(df['Avg_Accuracy_Rate_1_2'], errors='coerce')

df = df.dropna(subset=['Avg_Accuracy_Rate_1_2'])

formula = 'Avg_Accuracy_Rate_1_2 ~ team_exp_rating* ai_exp_rating *	data_skill_rating'
model = ols(formula, data=df).fit()

print(model.summary())

means = df.groupby(['team_exp_rating','ai_exp_rating','data_skill_rating']).mean()['Avg_Accuracy_Rate_1_2']
print(means)

anova_table_three_way = sm.stats.anova_lm(model, typ=3)
print(anova_table_three_way)

