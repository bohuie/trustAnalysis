import unittest
import pandas as pd
from trust_analytics import TrustAnalytics


class TestTrustAnalytics(unittest.TestCase):
    def setUp(self):
        self.tva = TrustAnalytics()

    def test_res_experience_table(self):
        print()
        results = self.tva.res_experience_table()
        print(results)

    def test_res_cultural_background(self):
        print()
        results = self.tva.res_cultural_background()
        # print(results)

    def test_col_ai_exp_rating(self):
        print()
        results = self.tva.col_ai_exp_rating()
        # print(results)

    def test_col_team_exp_rating(self):
        print()
        results = self.tva.col_team_exp_rating()
        # print(results)

    def test_col_data_skill_rating(self):
        print()
        results = self.tva.col_data_skill_rating()
        # print(results)

    def test_col_accuracy_skill(self):
        print()
        results = self.tva.col_accuracy_skill()
        # print(results)

    def test_col_accuracy_team(self):
        print()
        results = self.tva.col_accuracy_team()

    def test_col_accuracy_class(self):
        print()
        results = self.tva.col_accuracy_class()
