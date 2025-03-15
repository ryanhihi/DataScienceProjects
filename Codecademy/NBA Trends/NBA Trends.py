import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts_10 = nba_2010.pts[nba_2010.fran_id == "Knicks"]
nets_pts_10 = nba_2010.pts[nba_2010.fran_id == "Nets"]
knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)
diff_means_2010 =knicks_mean_score - nets_mean_score
print(diff_means_2010)


#Overlaped Histogram
plt.hist(knicks_pts_10, alpha=0.8, density = True, label = 'knicks')
plt.hist(nets_pts_10, alpha=0.8, density = True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()

#Comparing 2014
knicks_pts_14 = nba_2014.pts[nba_2014.fran_id == "Knicks"]
nets_pts_14 = nba_2014.pts[nba_2014.fran_id == "Nets"]
knicks_mean_score14 = np.mean(knicks_pts_14)
nets_mean_score14 = np.mean(nets_pts_14)
diff_means_2014 =knicks_mean_score14 - nets_mean_score14
print(diff_means_2014)

#Side-by-side Box Plot()
plt.clf()
sns.boxplot(data = nba, x='fran_id', y='pts')
plt.show()

#Analyze the relationship between categorical Variables
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

#Covert the table into proportion
location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

#Chi_Square Statistic using expected contingency
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

#Relationship between 2 Quantitative Variables
point_diff_forecast_cov = np.cov(nba_2010.point_diff, nba_2010.forecast)
print(point_diff_forecast_cov)

point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

#Generate Scatterplot of forecast and point_diff
plt.clf()
plt.scatter('forecast','point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()
