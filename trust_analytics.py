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

    """
    # Commented out for now, 2024-01-28
    def combine_accuracy(self):
        acc_skill = self.col_accuracy_skill()
        acc_team = self.col_accuracy_team()
        acc_class = self.col_accuracy_class()

        result = pd.concat(
            [
                acc_skill["skill_accuracy"],
                acc_team["team_accuracy"],
                acc_class["class_accuracy"],
            ],
            axis=1,
        )
        #result.to_csv("accuracy.csv")

        return result
    """
