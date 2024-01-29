import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('/Users/jayati/trustAnalysis/output_resultwfake.csv')

# df['Avg_Accuracy_Rate_level1'] = pd.to_numeric(df['Avg_Accuracy_Rate_level1'], errors='coerce')

# df = df.dropna(subset=['Avg_Accuracy_Rate_level1'])

# formula = 'Avg_Accuracy_Rate_level1 ~ Dataliteracy * experience * knowledgelevel'
# model = ols(formula, data=df).fit()


# print(model.summary())

# means = df.groupby(['Dataliteracy', 'experience', 'knowledgelevel']).mean()['Avg_Accuracy_Rate_level1']
# print(means)


# anova_table_three_way = sm.stats.anova_lm(model, typ=3)
# print(anova_table_three_way)


import pandas as pd

# Assuming your DataFrame is named df
agg_dict = {
    'Avg_Accuracy_Rate_level1': ['count', 'mean', 'std'],
    'Avg_Accuracy_Rate_level2': ['count', 'mean', 'std'],
    'Avg_Accuracy_Rate_level3': ['count', 'mean', 'std'],
    # Add more columns as needed
}

summary_stats = df.groupby(['Dataliteracy', 'experience', 'knowledgelevel']).agg(agg_dict).reset_index()
summary_stats.columns = [
    'Dataliteracy', 'experience', 'knowledgelevel',
    'n1', 'mean1', 'stdev1',
    'n2', 'mean2', 'stdev2',
    'n3', 'mean3', 'stdev3',
    # Adjust column names based on your needs
]

# Calculate confidence intervals (CIs) for each mean
confidence_level = 0.95
z_value = 1.96  # For a 95% CI

for i in range(1, 4):  # Assuming you have three levels (adjust as needed)
    col_mean = f'mean{i}'
    col_stdev = f'stdev{i}'
    col_ci_low = f'ci_low{i}'
    col_ci_high = f'ci_high{i}'

    margin_of_error = z_value * (summary_stats[col_stdev] / (summary_stats[f'n{i}'] ** 0.5))
    summary_stats[col_ci_low] = summary_stats[col_mean] - margin_of_error
    summary_stats[col_ci_high] = summary_stats[col_mean] + margin_of_error

# Display the summary statistics
print(summary_stats)


