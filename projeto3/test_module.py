import unittest
import time_series_visualizer as tsv
import matplotlib.pyplot as plt

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = tsv.draw_line_plot()
        self.assertIsInstance(fig, plt.Figure)
        self.assertEqual(fig.axes[0].get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        self.assertEqual(fig.axes[0].get_xlabel(), "Date")
        self.assertEqual(fig.axes[0].get_ylabel(), "Page Views")

    def test_bar_plot(self):
        fig = tsv.draw_bar_plot()
        self.assertIsInstance(fig, plt.Figure)
  
