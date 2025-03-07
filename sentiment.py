import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk

df = pd.read_csv("/Users/ayaan/Downloads/data-amazon/Reviews.csv")

print(df.head())