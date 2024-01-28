import pandas as pd
import numpy as np


class TrustVizAnalytics:
    """
    A class for analyzing the results of the Trust Viz survey.
    Jan 2024
    """

    def __init__(self):
        self.results = pd.read_csv("survey-results.csv")

    def clean_csv(self):
        results = self.results
        results.dropna(subset=["Q38"], inplace=True)
        return results

    def cultural_background(self):
        results = self.results
        culback = (
            results["Cultural Background"]
            .str.split(",")
            .explode("Cultural Background")
            .value_counts()
        )
        # df['Cast'].str.split(',').explode('Cast').value_counts()
        return culback

    def accuracy_skill(self):
        results = self.results

        answers = ["4", "Math", "No", "Yes"]

        df_accuracy = results[["Q22", "Q24", "Q25", "Q26"]].copy()
        df_accuracy["Q22"] = df_accuracy["Q22"].apply(str)

        accuracy = []

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append(correct.sum() / correct.size)

        df_accuracy = df_accuracy.assign(skill_accuracy=accuracy)
        df_accuracy = df_accuracy.drop(columns=["Q22", "Q24", "Q25", "Q26"])
        df_accuracy.to_csv("accuracy_skill.csv")
        # print(df_accuracy['skill_accuracy'].value_counts())

        return df_accuracy

    def accuracy_team(self):
        results = self.results

        answers = ["Team A", "Team B"]

        df_accuracy = results[["Q29", "Q30"]].copy()
        accuracy = []

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append(correct.sum() / correct.size)

        df_accuracy = df_accuracy.assign(team_accuracy=accuracy)
        df_accuracy = df_accuracy.drop(columns=["Q29", "Q30"])
        df_accuracy.to_csv("accuracy_team.csv")
        # print(df_accuracy['team_accuracy'].value_counts())

        return df_accuracy

    def accuracy_class(self):
        results = self.results

        answers = (
            "Most teams seem to have a good spread of members with different majors."
        )

        df_accuracy = results[["Q31"]].copy()
        accuracy = []

        for index, row in df_accuracy.iterrows():
            correct = answers == row.values
            accuracy.append(correct.sum() / correct.size)

        df_accuracy = df_accuracy.assign(class_accuracy=accuracy)
        df_accuracy = df_accuracy.drop(columns=["Q31"])
        df_accuracy.to_csv("accuracy_class.csv")
        # print(df_accuracy['class_accuracy'].value_counts())

        return df_accuracy

    def combine_accuracy(self):
        acc_skill = self.accuracy_skill()
        acc_team = self.accuracy_team()
        acc_class = self.accuracy_class()

        result = pd.concat(
            [
                acc_skill["skill_accuracy"],
                acc_team["team_accuracy"],
                acc_class["class_accuracy"],
            ],
            axis=1,
        )
        result.to_csv("accuracy.csv")

        return result
