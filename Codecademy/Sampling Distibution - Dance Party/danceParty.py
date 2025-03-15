from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


# task 1: load in the spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")
# task 2: preview the dataset
print(spotify_data.head())
# task 3: select the relevant column
song_tempos = spotify_data["tempo"]
# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)
#The population distribution is approximately normal with a little bit of right-skewness.
# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")
#The mean is also an unbiased estimator as the mean of the sampling distribution of the mean is always approximately the same as the population mean.

# task 8: sampling distribution of the sample minimum
#Notice that the mean of the sample minimums is consistently much higher than the population minimum. Since you are looking for high-tempo songs for the party, this is actually a good thing! You will want to avoid having a lot of low-tempo songs.
# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")
#The mean of the sample variances is consistently slightly less than the population variance, meaning it is a biased estimator. However, it is super close
#We calculated the sample variance the same way we calculate population variance..
# However, the formulas for sample variance and population variance are actually distinct
#When we measure the sample variance using the same formula, it turns out that we tend to underestimate the population variance. Because of this, we divide by n-1 instead of n:
#Using this formula, sample variance becomes an unbiased estimator of the population variance.
#Using this formula, sample variance becomes an unbiased estimator of the population variance. np.var(x, ddof=1)

# task 13: calculate the population mean and standard deviation
population_mean = song_tempos.mean()
population_std = song_tempos.std()
# task 14: calculate the standard error
standard_error = population_std/(30**0.5)
# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140,population_mean,standard_error))
# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1-stats.norm.cdf(150,population_mean,standard_error))


