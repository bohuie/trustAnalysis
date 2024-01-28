import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('/Users/jayati/trustAnalysis/output_resultwfake.csv')


formula = 'Avg_Accuracy_Rate_level1 ~ Dataliteracy * experience * knowledgelevel'
model = ols(formula, data=df).fit()


anova_table_three_way = sm.stats.anova_lm(model, typ=3)
print(anova_table_three_way)

