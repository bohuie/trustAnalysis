import pandas as pd
import numpy as np


class TrustAnalytics:
    """
    A class for analyzing the results of the Trust Viz survey.
    Jan 2024
    """

    def __init__(self):
        self.results = pd.read_csv("survey-results.csv")

    def res_cultural_background(self):
        results = self.results
        culback = (
            results["Cultural Background"]
            .str.split(",")
            .explode("Cultural Background")
            .value_counts()
        )
        # df['Cast'].str.split(',').explode('Cast').value_counts()
        return culback

    def col_team_exp_rating(self):
        """
        Takes the results from Q14 and gives a rating for team formation experience.

        """

        q14_res = self.results["Q14"]
        team_exp = []

        for i in range(len(q14_res)):
            # print(type(q14_res[i]))
            if pd.isna(q14_res[i]):
                team_exp.append("NO EXP")
            else:
                team_exp.append("EXP")

        self.results.insert(1, "team_exp_rating", team_exp)
        # print(self.results.iloc[:, [0,1,2,3,4]])

        return team_exp

    def col_data_skill_rating(self):
        """
        Takes the results of the accuracy measures and returns an accuracy rating, adding it back to `self.results`

        """
        acc_skill = self.col_accuracy_skill()
        acc_team = self.col_accuracy_team()
        acc_class = self.col_accuracy_class()

        results = self.results
        acc_rating = []

        for i in range(len(acc_skill)):
            if acc_skill[i] == 100 and acc_team[i] == 100 and acc_class[i] == 100:
                acc_rating.append("HIGH")
            else:
                acc_rating.append("LOW")
        self.results.insert(1, "data_skill_rating", acc_rating)

        # print(pd.DataFrame(acc_rating).value_counts())
        # print(self.results.iloc[:, [0,1,2,3,4]])

        return acc_rating

    def col_accuracy_skill(self):
        """
        Creates a column for accuracy in data skills, adds it to `self.results`, and returns a column of accuracy results.

        """
        results = self.results
        answers = ["4", "Math", "No", "Yes"]
        accuracy = []

        df_accuracy = results[["Q22", "Q24", "Q25", "Q26"]].copy()
        df_accuracy["Q22"] = df_accuracy["Q22"].apply(str)

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append((correct.sum() / correct.size) * 100)

        col_q26 = self.results.columns.get_loc("Q26")
        self.results.insert(col_q26 + 1, "skill_accuracy", accuracy)

        return accuracy

    def col_accuracy_team(self):
        """
        Creates a column for accuracy in team data skills, adds it to `self.results`, and returns a column of accuracy results.

        """
        results = self.results
        answers = ["Team A", "Team B"]
        accuracy = []

        df_accuracy = results[["Q29", "Q30"]].copy()

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append((correct.sum() / correct.size) * 100)

        col_q30 = self.results.columns.get_loc("Q30")
        self.results.insert(col_q30 + 1, "team_accuracy", accuracy)

        # print(self.results.iloc[:, [col_q30 - 2, col_q30 - 1, col_q30, col_q30 +1, col_q30+2]])

        return accuracy

    def col_accuracy_class(self):
        """
        Creates a column for accuracy in class data skills, adds it to `self.results`, and returns a column of accuracy results.

        """
        results = self.results
        answers = (
            "Most teams seem to have a good spread of members with different majors."
        )
        accuracy = []
        df_accuracy = results[["Q31"]].copy()

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append((correct.sum() / correct.size) * 100)

        col_q31 = self.results.columns.get_loc("Q31")
        self.results.insert(col_q31 + 1, "class_accuracy", accuracy)

        # print(self.results.iloc[:, [col_q31 - 2, col_q31 - 1, col_q31, col_q31 +1, col_q31+2]])

        return accuracy
