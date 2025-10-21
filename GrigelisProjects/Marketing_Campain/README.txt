In projects were used these libraries:
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import numpy as np
from scipy.stats import kruskal
from scipy.stats import shapiro
from scipy import stats
from scipy.stats import mannwhitneyu
from itertools import product
import seaborn as sns
import scipy.stats as stats
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
Fast Food Marketing Campaign A\B Test dataset*
Introduction
A fast-food chain plans to add a new item to its menu. . In order to determine which promotion has the greatest effect on sales, the new item is introduced at locations in several randomly selected markets. A different promotion is used at each location, and the weekly sales of the new item are recorded for the first four weeks. Data obtained from Kaggle database. Dataset: Fast Food Marketing Campaign A\B Test ( https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test )

Goal
Evaluate and decide which marketing strategy: Promotion 1, Promotion 2 or Promotion 3 works the best. To evaluation include factors like store size, sales, store age.

Analysis
Analysis showed that where are no significant difference in promotions if data is devided by size and age. Firstly data were analyses in big scale by using only Sales, secondly size and in third - all size and age combinations.

Results
The best performing - Promotion 1.

Marketing campaign

Suggestions for improvement
To create deeper analysis for different combination of store size, store age, promotion plot. In some combinations sales is growing week by week, while in the other drops after few weeks.

Mobile Games A/B Testing - Cookie Cats
Introduction
A/B test results of Cookie Cats to examine what happens when the first gate in the game was moved from level 30 to level 40. When a player installed the game, he or she was randomly assigned to either gate_30 or gate_40.

Goal
Determine with which level gates performs better.

Analysis
Analysis showed, that players behaviours is different and could be splited in groups. When player did not come back neither after 1 or after 7 days and players came back after 1 Gate_30 performed better. When player players came back after 1 and after 7 Gate_40 performed better. When player players came back after 7 both gates performed similar. To present more accurate and reliable recommendation additional data and more analysis needed.

Results
In general analysis represents evidence that game performs better result when first gate position is in at level 30. The recommendation is proved by calculations and tests.

Suggestions for improvement
Conduct a more detailed analysis with groups.