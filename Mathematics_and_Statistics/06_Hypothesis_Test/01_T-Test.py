from scipy import stats
import numpy as np

# Data (sample)
data = np.array([12, 15, 14, 10, 13, 15, 16, 14, 12, 15])

# Perform 1 sample t-test
t_statistic, p_value = stats.ttest_1samp(data, popmean=13)

print("t-statistic:", t_statistic)
print("p-value:", p_value)