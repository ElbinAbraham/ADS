import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

mean = np.mean(data,axis=0)
median = np.median(data,axis=0)
std_deviation = np.std(data,axis=0)
skewness = list(3 * (mean - median) / std_deviation)

print("Karl Pearson's coefficient of skewness:", *skewness)
