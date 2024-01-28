import unittest
import pandas as pd
from trust_viz_analytics import TrustVizAnalytics


class TestTrustVizAnalytics(unittest.TestCase):
    def setUp(self):
        self.results = pd.read_csv("survey-results.csv")
        self.tva = TrustVizAnalytics()
        self.results = self.tva.clean_csv()

    def test_clean_csv(self):
        results = self.tva.clean_csv()

    def test_cultural_background(self):
        results = self.tva.cultural_background()
        # print(results)

    def test_accuracy_skill(self):
        results = self.tva.accuracy_skill()
        # print(results)

    def test_accuracy_team(self):
        results = self.tva.accuracy_team()

    def test_accuracy_class(self):
        results = self.tva.accuracy_class()

    def test_combine_accuracy(self):
        results = self.tva.combine_accuracy()
        print(results)
